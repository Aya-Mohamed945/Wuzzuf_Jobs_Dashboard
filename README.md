# 📊 Wuzzuf Jobs Data Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Project Overview

An interactive dashboard that analyzes the Egyptian and international data job market by scraping and visualizing job postings from Wuzzuf, Egypt's leading job platform.

---

## 🎯 Key Features

- **Live Web Scraping**: Collect real-time job data from Wuzzuf.net  
- **Multi-source Data**: Use existing CSV, scrape fresh data, or upload your own  
- **Interactive Visualizations**: Built with Plotly for rich, responsive charts  
- **Arabic Text Support**: Full translation of Arabic job listings to English  
- **Comprehensive Analysis**: Job titles, locations, work modes, employment types, and skills  

---
## 📸 **Screenshots**

| Top Jobs Dashboard | Geographic Analysis |
|--------------------|---------------------|
| ![Top Jobs](https://i.postimg.cc/QCBjT6Vf/Screenshot-2026-03-03-235804.png) | ![Map](https://i.postimg.cc/HW5YdNDx/Screenshot-2026-03-04-000314.png) |

| Work Modes | Skills Analysis |
|------------|-----------------|
| ![Work Modes](https://i.postimg.cc/4dk05B8b/Screenshot-2026-03-04-000438.png) | ![Skills](https://i.postimg.cc/254Gzmwc/Screenshot-2026-03-04-000620.png) |

---
## 🚀 Live Demo

👉 **[Click here to view the live dashboard](https://wuzzufjobsdashboard-fkgmjbotfp8dubuumexhu3.streamlit.app/)** 👈

---

## 📊 Dashboard Sections

### 1️⃣ Job Distribution
- Top 5 most demanded job titles  
- Work modes breakdown (On-site, Remote, Hybrid)  
- Employment types distribution  

### 2️⃣ Geographic Analysis
- Jobs per city in Egypt  
- International job distribution  
- Interactive world map with log scale  
- Remote opportunities by location  

### 3️⃣ Employment Details
- Top companies hiring  
- Employment types analysis  
- Job market insights  

### 4️⃣ Skills Analysis
- Top 20 most requested skills  
- Skill frequency visualization  
- Market trend identification  

---

## 🔧 Tech Stack

| Purpose | Tools/Libraries |
|----------|----------------|
| Web Scraping | `requests`, `BeautifulSoup4` |
| Data Processing | `pandas`, `numpy` |
| Visualizations | `plotly`, `matplotlib` |
| Dashboard | `streamlit` |
| Deployment | Streamlit Cloud |

---

## 📦 Installation & Local Setup

### Prerequisites

- Python 3.8 or higher  
- Git  

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Aya-Mohamed945/Wuzzuf_Jobs_Dashboard.git
cd Wuzzuf_Jobs_Dashboard
```

---

### 2️⃣ (Optional) Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the App

```bash
streamlit run streamlit_app.py
```

---

### 5️⃣ Open in Browser

The app will automatically open at:

```
http://localhost:8501
```

If it doesn't open automatically, paste the link manually into your browser.

---

## ⚠️ Common Issues

| Problem | Solution |
|----------|----------|
| `pip` not recognized | Reinstall Python and check **"Add to PATH"** |
| `streamlit` not found | Run `pip install streamlit` |
| Port 8501 already in use | Run `streamlit run streamlit_app.py --server.port 8502` |

---

## 🗂️ Project Structure

```text
Wuzzuf_Jobs_Dashboard/
│
├── streamlit_app.py        # Main dashboard
├── scraper.py              # Web scraping logic
├── data_cleaning.py        # Data cleaning & preprocessing
├── visualizations.py       # Charts & graphs
├── requirements.txt        # Dependencies
├── .gitignore              # Git ignored files
└── README.md               # Documentation
```

---

## 📈 Key Insights

| Insight | Finding |
|----------|----------|
| Market Concentration | 75%+ of jobs in Cairo & Giza |
| Work Culture | 87.6% On-site roles |
| Top Demands | Data Entry > Accountant > Data Analyst |
| International Reach | US, UK, UAE, Libya |
| Remote Work | 6.4% of total jobs |

---

## 🛠️ How to Use

### Option 1: Use Existing Data
Select **📁 Use existing CSV** from the sidebar.

### Option 2: Scrape Fresh Data
Select **🆕 Scrape fresh data**  
Click **Start Scraping** (takes 2–3 minutes)

### Option 3: Upload Your Own CSV
Select **📤 Upload CSV**

Required columns:

```
job_title
companies
locations
employment_types
work_modes
skills
```

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork the repository and submit a pull request.

---

## 👩‍💻 Author

**Aya Mohamed**

[![GitHub](www.linkedin.com/in/aya-abd-elazim-94a256347)

[![LinkedIn](https://www.linkedin.com/in/aya-abd-elazim-94a256347/?isSelfProfile=true)

---

## ⭐ Show Your Support

If this project helped you, please give it a ⭐ on GitHub!
