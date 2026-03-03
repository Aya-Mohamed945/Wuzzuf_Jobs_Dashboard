```markdown
# 📊 Wuzzuf Jobs Data Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 **Project Overview**
An interactive dashboard that analyzes the Egyptian and international data job market by scraping and visualizing job postings from Wuzzuf, Egypt's leading job platform.

### 🎯 **Key Features**
- **Live Web Scraping**: Collect real-time job data from Wuzzuf.net
- **Multi-source Data**: Use existing CSV, scrape fresh data, or upload your own
- **Interactive Visualizations**: Built with Plotly for rich, responsive charts
- **Arabic Text Support**: Full translation of Arabic job listings to English
- **Comprehensive Analysis**: Job titles, locations, work modes, employment types, and skills

---

## 🚀 **Live Demo**
👉 **[Click here to view the live dashboard](https://wuzzufjobsdashboard-fkgmjbotfp8dubuumexhu3.streamlit.app/)** 👈

---

## 📊 **Dashboard Sections**

### 1️⃣ **Job Distribution**
- Top 5 most demanded job titles
- Work modes breakdown (On-site, Remote, Hybrid)
- Employment types distribution

### 2️⃣ **Geographic Analysis**
- Jobs per city in Egypt
- International job distribution
- Interactive world map with log scale
- Remote opportunities by location

### 3️⃣ **Employment Details**
- Top companies hiring
- Employment types analysis
- Job market insights

### 4️⃣ **Skills Analysis**
- Top 20 most requested skills
- Skill frequency visualization
- Market trend identification

---

## 🔧 **Tech Stack**

| Purpose | Tools/Libraries |
|---------|-----------------|
| **Web Scraping** | `requests`, `BeautifulSoup4` |
| **Data Processing** | `pandas`, `numpy` |
| **Visualizations** | `plotly`, `matplotlib` |
| **Dashboard** | `streamlit` |
| **Deployment** | Streamlit Cloud |

---

## 📦 **Installation & Local Setup**

### ✅ **Prerequisites**
Make sure you have the following installed:
- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **Git** ([Download Git](https://git-scm.com/downloads))

### 🚀 **Step-by-Step Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aya-Mohamed945/Wuzzuf_Jobs_Dashboard.git
   cd Wuzzuf_Jobs_Dashboard
(Optional but recommended) Create a virtual environment

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Install required packages

bash
pip install -r requirements.txt
Run the app locally

bash
streamlit run streamlit_app.py
Open in browser

The app will automatically open at: http://localhost:8501

If not, copy and paste this link manually

⚠️ Common Issues & Solutions
Problem	Solution
pip not recognized	Reinstall Python and check "Add Python to PATH"
streamlit not found	Run pip install streamlit manually
Port 8501 already in use	Run: streamlit run streamlit_app.py --server.port 8502
🎉 Done! The dashboard is now running on your local machine.

🗂️ Project Structure
text
Wuzzuf_Jobs_Dashboard/
│
├── streamlit_app.py          # Main dashboard application
├── scraper.py                 # Web scraping functions
├── data_cleaning.py           # Data cleaning and translation
├── visualizations.py           # All visualization functions
├── requirements.txt           # Project dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
📈 Key Insights
Insight	Finding
Market Concentration	75%+ of Egyptian jobs in Cairo/Giza
Work Culture	87.6% on-site, minimal remote/hybrid
Top Demands	Data Entry > Accountant > Data Analyst > Data Scientist
International Reach	Opportunities in US, UK, UAE, Libya
Remote Work	6.4% of total jobs, concentrated in Cairo
🛠️ How to Use
Option 1: Use Existing Data
Select "📁 Use existing CSV" from sidebar

Dashboard loads immediately

Option 2: Scrape Fresh Data
Select "🆕 Scrape fresh data from Wuzzuf"

Click "Start Scraping" (takes 2-3 minutes)

New data appears automatically

Option 3: Upload Your Own CSV
Select "📤 Upload your own CSV file"

Ensure your CSV has required columns:

job_title, companies, locations

employment_types, work_modes, skills

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

📄 License
This project is MIT licensed.

👩‍💻 Author
Aya Mohamed
https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white

⭐ Show your support
Give a ⭐️ if this project helped you!

text

---

## 🚀 **بعد ما تحطي الكود:**

في Terminal:
```bash
git add README.md
git commit -m "Update README with improved installation guide"
git push
وبعد شوية التحديث يظهر على GitHub ✨

الـ README دلوقتي:

✅ واضح وسهل

✅ فيه خطوات التثبيت بالتفصيل

✅ فيه troubleshooting

✅ شكله جميل ومنظم

أخيريني لو عايزة تعدلي حاجة تانية! 😊


