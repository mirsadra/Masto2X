import json
import feedparser
import tweepy
import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tempfile

print("🚀 Starting Mastodon to X script...")

# === Load config ===
with open("config.json", "r") as f:
    config = json.load(f)

MASTODON_RSS = config["mastodon_rss"]
print(f"🔍 RSS URL: {MASTODON_RSS}")

# === Load last posted ID ===
STATE_FILE = "last_post.json"
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        state = json.load(f)
        last_post_id = state.get("last_id")
else:
    last_post_id = None

print(f"🔍 Last posted ID: {last_post_id}")

# === Setup X Client (v2 API, OAuth 1.0a User Context) ===
client = tweepy.Client(
    consumer_key=config["api_key"],
    consumer_secret=config["api_secret"],
    access_token=config["access_token"],
    access_token_secret=config["access_secret"]
)

# === Setup API v1.1 for media upload ===
api_v1 = tweepy.API(tweepy.OAuth1UserHandler(
    config["api_key"],
    config["api_secret"],
    config["access_token"],
    config["access_secret"]
))

def clean_html_content(html_content):
    """Extract clean text from HTML content"""
    if not html_content:
        return ""
    
    print(f"🔍 HTML input length: {len(html_content)}")
    print(f"🔍 HTML input: {repr(html_content[:500])}")
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for a_tag in soup.find_all('a', href=True):
        # Replace the entire <a> tag with just the URL
        a_tag.replace_with(a_tag['href'])
    
    # Extract text and preserve basic structure
    text = soup.get_text(separator='\n\n', strip=True)
    
    print(f"🔍 After BeautifulSoup: {repr(text[:500])}")
    
    # Clean up extra whitespace and newlines
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)  # Remove excessive newlines
    text = re.sub(r'[ \t]+', ' ', text)  # Normalize spaces
    
    # Convert Mastodon tag URLs back to hashtags
    text = re.sub(r'https://mastodon\.social/tags/(\w+)', r'#\1', text)
    
    # Fix hashtag spacing (remove spaces in hashtags)
    text = re.sub(r'#\s+(\w+)', r'#\1', text)
    
    # Put all hashtags on the same line with spaces between them
    # Find all hashtags and join them with spaces
    hashtags = re.findall(r'#\w+', text)
    if hashtags:
        # Remove individual hashtag lines
        text = re.sub(r'\n\n#\w+', '', text)
        text = re.sub(r'\n#\w+', '', text)
        # Add all hashtags at the end on one line
        hashtag_line = ' '.join(hashtags)
        text = f"{text.rstrip()}\n{hashtag_line}"
    
    print(f"🔍 Final cleaned text: {repr(text)}")
    
    return text.strip()

def extract_images_from_entry(entry):
    """Extract image URLs from RSS entry"""
    images = []
    
    # Check for enclosures (common in RSS feeds)
    if hasattr(entry, 'enclosures'):
        for enclosure in entry.enclosures:
            if enclosure.type and enclosure.type.startswith('image/'):
                images.append(enclosure.href)
    
    # Check for media content
    if hasattr(entry, 'media_content'):
        for media in entry.media_content:
            if media.get('type', '').startswith('image/'):
                images.append(media['url'])
    
    # Parse content for img tags
    content_fields = ['content', 'summary', 'description']
    for field in content_fields:
        if hasattr(entry, field):
            content = getattr(entry, field)
            if isinstance(content, list) and len(content) > 0:
                content = content[0].value
            elif isinstance(content, str):
                pass
            else:
                continue
                
            soup = BeautifulSoup(content, 'html.parser')
            img_tags = soup.find_all('img')
            for img in img_tags:
                src = img.get('src')
                if src:
                    images.append(src)
    
    return images

def download_image(url):
    """Download image and return temporary file path"""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        # Get file extension from URL or content type
        parsed_url = urlparse(url)
        ext = os.path.splitext(parsed_url.path)[1]
        if not ext:
            content_type = response.headers.get('content-type', '')
            if 'jpeg' in content_type or 'jpg' in content_type:
                ext = '.jpg'
            elif 'png' in content_type:
                ext = '.png'
            elif 'gif' in content_type:
                ext = '.gif'
            elif 'webp' in content_type:
                ext = '.webp'
            else:
                ext = '.jpg'  # default
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
            for chunk in response.iter_content(chunk_size=8192):
                tmp_file.write(chunk)
            return tmp_file.name
            
    except Exception as e:
        print(f"❌ Error downloading image {url}: {e}")
        return None

def upload_media_to_x(image_paths):
    """Upload images to X and return media IDs"""
    media_ids = []
    
    for image_path in image_paths:
        try:
            media = api_v1.media_upload(image_path)
            media_ids.append(media.media_id)
            print(f"✅ Uploaded image: {image_path}")
        except Exception as e:
            print(f"❌ Error uploading image {image_path}: {e}")
        finally:
            # Clean up temporary file
            try:
                os.unlink(image_path)
            except:
                pass
    
    return media_ids

# === Fetch Mastodon feed ===
print(f"🔍 Fetching feed from: {MASTODON_RSS}")
feed = feedparser.parse(MASTODON_RSS)
print(f"🔍 Feed entries found: {len(feed.entries)}")

if feed.entries:
    latest_entry = feed.entries[0]
    entry_id = latest_entry.id
    print(f"🔍 Latest entry ID: {entry_id}")
    print(f"🔍 Last posted ID: {last_post_id}")

    # Debug: Show all available fields in the entry
    print(f"🔍 Available fields: {list(latest_entry.keys())}")
    
    # Robust content extraction with debugging
    if "title" in latest_entry:
        raw_content = latest_entry.title
        print(f"🔍 Using title content")
    elif "summary" in latest_entry:
        raw_content = latest_entry.summary
        print(f"🔍 Using summary content")
    elif "content" in latest_entry and len(latest_entry.content) > 0:
        raw_content = latest_entry.content[0].value
        print(f"🔍 Using content[0].value")
    else:
        raw_content = "New post (no text)"
        print(f"🔍 Using fallback content")

    print(f"🔍 Raw content length: {len(raw_content)}")
    print(f"🔍 Raw content preview: {raw_content[:200]}...")

    # Clean HTML content
    text_content = clean_html_content(raw_content)
    
    print(f"🔍 Cleaned content length: {len(text_content)}")
    print(f"🔍 Cleaned content: {text_content}")
    
    # It's designed for an X Premium, so use the full content without trimming
    text = text_content

    if entry_id != last_post_id:
        print("📝 New Mastodon toot found. Processing...")
        
        # Extract and download images
        image_urls = extract_images_from_entry(latest_entry)
        media_ids = []
        
        if image_urls:
            print(f"🖼️  Found {len(image_urls)} image(s). Downloading...")
            downloaded_images = []
            
            # Download up to 4 images (X limit)
            for url in image_urls[:4]:
                downloaded_path = download_image(url)
                if downloaded_path:
                    downloaded_images.append(downloaded_path)
            
            if downloaded_images:
                media_ids = upload_media_to_x(downloaded_images)
        
        # Post tweet with or without media
        try:
            print(f"🔍 Final text to post: {repr(text)}")
            if media_ids:
                response = client.create_tweet(text=text, media_ids=media_ids)
                print(f"✅ Posted with {len(media_ids)} image(s):", response)
            else:
                response = client.create_tweet(text=text)
                print("✅ Posted (text only):", response)
            
            # Update last posted ID
            with open(STATE_FILE, "w") as f:
                json.dump({"last_id": entry_id}, f)
                
        except Exception as e:
            print(f"❌ Error posting to X: {e}")
    else:
        print("No new posts.")
else:
    print("❌ No entries found in RSS feed.")