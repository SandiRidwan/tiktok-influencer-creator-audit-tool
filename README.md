# 🚀 TikTok Influencer Audit Tool

![Python](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Apify](https://img.shields.io/badge/Apify-API-FF671E?style=for-the-badge&logo=apify&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

An automated **End-to-End Pipeline** that scrapes TikTok profiles, calculates real-time engagement via the **Sonic Score Formula**, and syncs everything directly to Google Sheets. 

---

## 📸 Dashboard Preview
| Influencer | Followers | Sonic Score | Status | Cost Est. | ROI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **@mrbeast** | 124.7M | 1,744,520 | 🔥 Viral | Rp 261M | High |
| **@gadgetin** | 2.5M | 1,266,047 | 🔥 Viral | Rp 189M | High |

---

## ✨ Key Features
* **🎯 Sonic Score Engine:** Proprietary formula weighing Shares (5x), Saves (4x), Comments (2x), Likes (1x), and Views (0.1x).
* **🕵️‍♂️ Browser-Level Scraping:** Uses Playwright/Cheerio via Apify to bypass TikTok's heavy masking.
* **📧 Email Extractor:** Automatically pulls business emails from influencer bios.
* **📊 Live Sheets Sync:** No more manual data entry. Everything is updated via Google Sheets API.
* **🛡️ Production Ready:** Fully supports Environment Variables for secure public repository hosting.

---

## 🛠️ The Tech Stack
* **Core:** Python 3.9+
* **Scraper Engine:** [Apify](https://apify.com/) (TikTok Profile Scraper)
* **Data Handling:** Pandas, NumPy
* **Database/UI:** Google Sheets API (via `gspread`)
* **Security:** `python-dotenv` & GitHub Secrets

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/sonic-audit-tool.git](https://github.com/YOUR_USERNAME/sonic-audit-tool.git)
   cd sonic-audit-tool
   
2. Install Dependencies

Bash
pip install -r requirements.txt

3.Configure Environment Variables
  Create a .env file in the root directory: 
  APIFY_TOKEN=your_apify_token_here
  SPREADSHEET_ID=your_google_sheets_id_here

4. Add Google Credentials
   Place your credentials.json from Google Cloud Console into the root folder.

5. Run the Engine
   bash
   python main.py

🧪 The Sonic FormulaThe "Sonic Score" is calculated based on the median performance of the last 15 videos:
    $$Sonic Score = (Shares \times 5) + (Saves \times 4) + (Comments \times 2) + (Likes \times 1) + (Views \times 0.1)$$

🔐 Security Notice
This repository is configured to ignore sensitive files like credentials.json and .env via .gitignore.

For Public Deployment: If deploying via GitHub Actions, ensure you map your secrets to:

APIFY_TOKEN

SPREADSHEET_ID

GOOGLE_APPLICATION_CREDENTIALS_JSON (The full content of your JSON key)

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

👨‍💻 Author
Sandi

GitHub: @sandi-dev

Project: Influencer Audit Automation

⭐ If you find this tool useful, please give it a star!
