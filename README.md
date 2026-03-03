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
👉 **[Click here to view the live dashboard](https://wuzzufjobsdashboard.streamlit.app)** 👈

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

1. **Clone the repository**
```bash
git clone https://github.com/Aya-Mohamed945/Wuzzuf_Jobs_Dashboard.git
cd Wuzzuf_Jobs_Dashboard