# Masto2X: Mastodon to X (Twitter) Cross-Poster 🔄

<div align="center">

<!-- Animated gradient title badge -->
![Masto2X](https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=6366F1&background=FFFFFF00&center=true&vCenter=true&multiline=true&width=500&height=80&lines=Masto2X+Cross-Poster;Seamless+Social+Bridge)

<!-- Dynamic stats and info badges -->
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://python.org)
[![Version](https://img.shields.io/github/v/release/mirsadra/masto2x?style=for-the-badge&logo=github&color=6366F1)](https://github.com/mirsadra/masto2x/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-success?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/mirsadra/masto2x?style=for-the-badge&logo=github&color=gold)](https://github.com/mirsadra/masto2x/stargazers)

<!-- Interactive social follow badges -->
[![Follow on Mastodon](https://img.shields.io/badge/Follow-Mastodon-6364FF?style=for-the-badge&logo=mastodon&logoColor=white)](https://mastodon.social/@mirsadra)
[![Follow on X](https://img.shields.io/badge/Follow-X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/Mirsadraa)

<!-- Dynamic activity and health badges -->
[![GitHub last commit](https://img.shields.io/github/last-commit/mirsadra/masto2x?style=for-the-badge&logo=github&color=FF6B6B)](https://github.com/mirsadra/masto2x/commits)
[![Downloads](https://img.shields.io/github/downloads/mirsadra/masto2x/total?style=for-the-badge&logo=download&color=4ECDC4)](https://github.com/mirsadra/masto2x/releases)
[![Issues](https://img.shields.io/github/issues/mirsadra/masto2x?style=for-the-badge&logo=github&color=FFA07A)](https://github.com/mirsadra/masto2x/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/mirsadra/masto2x?style=for-the-badge&logo=github&color=98D8C8)](https://github.com/mirsadra/masto2x/pulls)

<!-- Code quality and CI badges -->
[![CodeFactor](https://img.shields.io/codefactor/grade/github/mirsadra/masto2x?style=for-the-badge&logo=codefactor&color=A8E6CF)](https://www.codefactor.io/repository/github/mirsadra/masto2x)
[![CI Status](https://img.shields.io/github/actions/workflow/status/mirsadra/masto2x/ci.yml?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/mirsadra/masto2x/actions)

<!-- Beautiful platform support badges -->
[![Supported Platforms](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/mirsadra/masto2x)
[![Python Versions](https://img.shields.io/pypi/pyversions/masto2x?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/masto2x/)

<!-- Animated feature highlights -->
![Features](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=4000&pause=500&color=9333EA&background=FFFFFF00&center=true&vCenter=true&width=600&height=50&lines=✨+Auto+Cross-Posting;🔄+Real-time+Sync;🛡️+Privacy+First;⚡+Lightning+Fast)

<!-- Eye-catching visual separator -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<!-- Interactive platform showcase -->
<table>
<tr>
<td align="center">
<img src="https://cdn.iconscout.com/icon/free/png-512/free-mastodon-icon-svg-png-download-10919004.png?f=webp&w=512" width="60" height="60" alt="Mastodon"/>
<br><strong>From Mastodon</strong>
</td>
<td align="center">
<img src="https://www.svgrepo.com/show/365082/arrow-right-thin.svg" width="80" height="40" alt="Arrow"/>
</td>
<td align="center">
<img src="https://img.icons8.com/fluency/96/000000/twitterx.png" width="60" height="60" alt="X"/>
<br><strong>To X (Twitter)</strong>
</td>
</tr>
</table>

</div>

---

A lightweight Python application that automatically syncs your Mastodon posts to your X (formerly Twitter) account. Perfect for maintaining presence across both platforms without manual cross-posting.

## ✨ Features

- **🔄 Automatic Syncing**: Checks for new Mastodon posts and cross-posts to X
- **🖼️ Media Support**: Handles images attached to Mastodon posts (up to 4 images)
- **🏷️ Hashtag Preservation**: Converts Mastodon tags to X hashtags
- **📝 Content Cleaning**: Intelligently formats HTML content for X
- **⚡ Lightweight**: Simple Python script with minimal dependencies
- **🔒 Self-Hosted**: Your data remains under your control
- **⏰ Scheduling Ready**: Easy to set up with cron or similar schedulers

## 📋 Prerequisites

Before installing Masto2X, make sure you have:

- Python 3.7 or higher
- A Mastodon account
- An X Developer account (for API access)
- Basic command-line knowledge

## 🚀 Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/yourusername/masto2x.git
   cd masto2x
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .masto2x-venv
   ```

3. **Activate the virtual environment**

   On **Windows**:
   ```bash
   .masto2x-venv\Scripts\activate
   ```

   On **macOS/Linux**:
   ```bash
   source .masto2x-venv/bin/activate
   ```

4. **Install required dependencies**
   ```bash
   pip install tweepy feedparser requests beautifulsoup4
   ```

## ⚙️ Configuration

1. **Set up X API Access**  
   - Apply for a developer account at [developer.twitter.com](https://developer.twitter.com)  
   - Create a new Project with Read/Write permissions  
   - Navigate to your Project > Settings > User authentication set up  
   - Set OAuth 1.0a with Read/Write permissions  
   - For callback URL, use your Mastodon instance URL  
   - Generate API keys and access tokens  

2. **Create `config.json`**  
   Create a `config.json` file in the project directory:

   ```json
   {
     "mastodon_rss": "https://mastodon.social/@yourusername.rss",
     "api_key": "YOUR_API_KEY",
     "api_secret": "YOUR_API_SECRET",
     "access_token": "YOUR_ACCESS_TOKEN",
     "access_secret": "YOUR_ACCESS_SECRET"
   }
   ```

3. **Initialize `last_post.json`**
   ```json
   {}
   ```

## 🎯 Usage

### Manual Run
```bash
python mastodon_to_x.py
```

### Automated Scheduling
Set up a cron job to run the script periodically:

```bash
# Run every 15 minutes
*/15 * * * * cd /path/to/masto2x && ./.masto2x-venv/bin/python mastodon_to_x.py
```

## 📁 Project Structure

```
masto2x/
│
├─ .masto2x-venv/        # virtual environment
├─ config.json           # store your API keys and settings
├─ mastodon_to_x.py      # main script
└─ last_post.json        # keeps track of last posted Mastodon toot
```

## 🔧 Troubleshooting

### Common Issues

**API Authentication Errors**
- Verify your X API keys have write permissions
- Check that your access tokens are valid

**RSS Feed Not Loading**
- Ensure your Mastodon RSS URL is correct
- Verify your Mastodon profile is public

**Character Limit Issues**
- Mastodon allows 500 characters while X limits to 280
- Long posts will be automatically truncated

**Media Upload Failures**
- Check internet connection for image downloads
- Verify X API media permissions

## 💰 Alternative Services

| Service | Price | Limitations |
|---------|-------|-------------|
| dlvr.it | $8.29/month | Unlimited posts |
| CircleBoom | $5.99-$17/month | Free tier: 3 posts/day |
| SocialOomph | $15/month | No RSS in free tier |
| Hootsuite RSS AutoPublisher | $5.99/month | App subscription required |

## 🤝 Support & Contributing

### ☕ Buy Me a Coffee
If this tool has saved you time, consider supporting its development:

<p align="left"> <a href="https://www.buymeacoffee.com/mirsadra" target="_blank"> <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="40"> </a> </p>

### ⭐ Give a Star
If you find this useful, please give it a star! ⭐ It helps others discover the project.

### 🐛 Report Issues & Contributions
Found a bug or have a feature request? Please open an issue or submit a pull request!

We welcome contributions for:
- Support for more social media platforms (Bluesky, Threads, etc.)
- Improved error handling
- Additional features

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- Mastodon API team for the RSS feed format
- X API for posting capabilities
- Python community for excellent libraries

_Disclaimer: This tool is not affiliated with, endorsed by, or connected to Mastodon gGmbH or X Corp. Use at your own risk. API limitations and changes may affect functionality._

<p align="center"> <strong>Happy Cross-Posting! 🚀</strong> </p>
