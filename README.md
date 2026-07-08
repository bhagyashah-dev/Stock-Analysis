# 📈 Sensex 30 Analytics Dashboard with Analyse your own Stocks Feature

An end-to-end data analytics project that explores the historical performance of the Top 30 S&P BSE Sensex companies using Python, Exploratory Data Analysis (EDA), and an interactive Streamlit dashboard.

In addition to analyzing the built-in Sensex dataset, the dashboard also allows users to upload and analyze their own stock market datasets with automatic preprocessing, feature engineering, and interactive visualizations.

The project demonstrates the complete data analytics workflow—from collecting and preprocessing stock market data to engineering financial features, performing statistical analysis, and building an interactive dashboard for financial data exploration.

---

# 📌 Project Overview

This project analyzes approximately **21,700+ historical stock market records** of the Top 30 S&P BSE Sensex companies over a period of nearly **3 years**.

The dashboard provides two analysis modes:

- 🏠 **Sensex 30 Dashboard** – Explore the preloaded Sensex dataset.
- 📂 **Upload Your Dataset** – Upload one or more stock CSV files and perform the same financial analysis on your own data.

---

# 🚀 Features

## 📊 Exploratory Data Analysis (EDA)

- Dataset overview
- Data cleaning & preprocessing
- Missing value analysis
- Duplicate removal
- Feature engineering
- Univariate analysis
- Bivariate analysis
- Time-series analysis
- Correlation analysis
- Volatility analysis
- Moving Average analysis
- Stock performance analysis

---

## ⚙️ Financial Features Engineered

The following financial features are generated automatically:

- Daily Return (%)
- 20-Day Moving Average (MA20)
- 50-Day Moving Average (MA50)
- Total Return (%)

---

# 💻 Interactive Streamlit Dashboard

## 🏠 Home – Sensex 30 Dashboard

### 🌍 All Companies Dashboard

#### Dataset Overview

- Total Companies
- Total Records
- Trading Days
- Years Covered

#### Market Comparison

- Average Closing Price
- Average Trading Volume

#### Performance Analysis

- Average Daily Return
- Total Return
- Stock Volatility

#### Correlation Analysis

- Correlation Heatmap

---

### 🏢 Company-wise Dashboard

#### Key Performance Indicators

- Latest Closing Price
- Highest Closing Price
- Lowest Closing Price
- Average Trading Volume

#### 📈 Price Analysis

- Closing Price Trend
- Trading Volume Trend

#### 📊 Technical Analysis

- 20-Day Moving Average
- 50-Day Moving Average

#### 📉 Return Analysis

- Daily Return Trend

#### 🔍 Relationship Analysis

- Open Price vs Closing Price
- Trading Volume vs Closing Price

#### 📋 Dataset Explorer

- Interactive filtered dataset
- Download filtered dataset as CSV

---

## 📂 Upload Your Dataset

Users can upload **one or more stock CSV files** and receive the same analysis available in the Sensex dashboard.

### Supported Features

- Upload multiple company CSV files
- Automatic dataset merging
- Automatic Stock column creation from filenames
- Automatic data cleaning
- Automatic feature engineering
- Company-wise analysis
- Market-wide analysis
- Interactive filtering
- Download filtered dataset

### Supported File Types

- Yahoo Finance CSV exports
- Custom stock datasets

### Automatic Data Cleaning

The application automatically performs:

- Cleaning Yahoo Finance metadata rows
- Column validation
- Date conversion
- Numeric data type conversion
- Missing value removal
- Duplicate removal
- Automatic Stock column generation (if missing)
- Dataset merging
- Sorting by Company and Date

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---

# 📷 Dashboard Preview

## 🔍 Your Stocks Dataset Analysis

<p align="center">
  <a href="assets/dashboard%20(6).png">
    <img src="assets/dashboard%20(6).png" width="90%">
  </a>
</p>

---

## 📈 All Companies Dashboard

<p align="center">
  <a href="assets/dashboard%20(1).png">
    <img src="assets/dashboard%20(1).png" width="48%">
  </a>

  <a href="assets/dashboard%20(2).png">
    <img src="assets/dashboard%20(2).png" width="48%">
  </a>
</p>

---

## 📊 Individual Company Dashboard

<p align="center">
  <a href="assets/dashboard%20(3).png">
    <img src="assets/dashboard%20(3).png" width="48%">
  </a>

  <a href="assets/dashboard%20(4).png">
    <img src="assets/dashboard%20(4).png" width="48%">
  </a>
</p>

---

## 🔍 Relationship Analysis

<p align="center">
  <a href="assets/dashboard%20(5).png">
    <img src="assets/dashboard%20(5).png" width="90%">
  </a>
</p>

---

# 📂 Project Structure

```
Stock Analysis/
│
├── dashboard/
│   ├── app.py
│   ├── charts.py
│   ├── utils.py
│   └── pages/
│       └── 1_📂_Analyze_Your_Dataset.py
│
├── notebooks/
│   └── EDA.ipynb
│
├── data/
│   └── Sensex30_Master_Cleaned.csv
│
├── assets/
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Key Analysis Performed

- Historical stock price analysis
- Trading volume analysis
- Daily return analysis
- Total return comparison
- Volatility comparison
- Correlation analysis
- Moving Average trend analysis
- Company-wise performance comparison
- Interactive dashboard development
- Automatic multi-file dataset processing

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Move into the project directory

```bash
cd your-repository-name
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run dashboard/app.py
```

---

# 📈 Future Improvements

- Portfolio performance analysis
- Candlestick charts
- Company comparison dashboard
- Risk-adjusted return metrics
- Live stock market integration
- News sentiment analysis
- Machine Learning price prediction
- Cloud deployment

---

This project was built during my **Summer Internship at Elite TechnoCrats**.

---

# 👨‍💻 Author

**Bhagya Shah**

Computer Science & Business Systems (CSBS) Undergraduate

Passionate about Data Analytics, Backend Development, and Full Stack Development.

---

## ⭐ If you found this project helpful, consider giving it a star!