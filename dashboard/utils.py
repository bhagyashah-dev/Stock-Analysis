import pandas as pd


# Load Dataset

import streamlit as st

@st.cache_data
def load_data(filepath="data/Sensex30_Master_Cleaned.csv"):
    df = pd.read_csv(filepath)
    
    # Data Cleaning Again
    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)
    return df

@st.cache_data
def load_multiple_data(files):
    required_columns = {"Date", "Open", "High", "Low", "Close", "Volume"}
    dfs = []

    for file in files:
        df = pd.read_csv(file)

        # PROPER DATA MERGING & CLEANING (like done manually in notebook for sensex30)

        df.columns = df.columns.str.strip() # Remove extra spaces from column names
        
        # Yahoo Finance exported files 
        if "Price" in df.columns and "Date" not in df.columns:   
            df.rename(columns={"Price": "Date"}, inplace=True) # Rename first column to Date
            df = df.iloc[2:].reset_index(drop=True) # Remove first two metadata rows

        # Check required columns
        missing = required_columns - set(df.columns)
        if missing:
            st.error(f"❌ {file.name} is missing required columns: {', '.join(sorted(missing))}")
            st.stop()

        # Create Stock column from filename if missing
        if "Stock" not in df.columns:
            df["Stock"] = file.name.replace(".csv", "").strip()

        df["Stock"] = df["Stock"].astype(str).str.strip() # Remove extra spaces from Stock names
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce") # Convert Date column  
        df.dropna(subset=["Date"], inplace=True) # Remove rows with invalid dates

        # Convert numeric columns
        numeric_columns = ["Open", "High", "Low", "Close", "Volume"]
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df.dropna(subset=["Open", "High", "Low", "Close", "Volume"],inplace=True) # Remove rows with missing values
        df.drop_duplicates(inplace=True) # Remove duplicate rows
        dfs.append(df)

    master_df = pd.concat(dfs, ignore_index=True) # Merge all files
    master_df.sort_values(["Stock", "Date"], inplace=True) # Sort data
    master_df.reset_index(drop=True, inplace=True) # Reset index

    return master_df



# Apply Filters

def filter_data(df, company, date_range):
    filtered_df = df.copy()

    if company != "All Companies":
        filtered_df = filtered_df[filtered_df["Stock"] == company]

    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[(filtered_df["Date"] >= pd.to_datetime(start_date))&(filtered_df["Date"] <= pd.to_datetime(end_date))]

    return filtered_df


# Dataset Overview KPIs

def get_dataset_overview(df):
    return {
        "total_companies": df["Stock"].nunique(), 
        "total_records": len(df), 
        "trading_days": df["Date"].nunique(), 
        "years_covered": round((df["Date"].max()-df["Date"].min()).days / 365, 1), 
        "start_date": df["Date"].min().date(), 
        "end_date": df["Date"].max().date()
    }


# Company KPIs

def get_company_kpis(df):
    return {
        "latest_close": df["Close"].iloc[-1], 
        "highest_close": df["Close"].max(), 
        "lowest_close": df["Close"].min(), 
        "average_volume": df["Volume"].mean()
    }


# Average Closing Price

def get_average_close(df):
    return (
        df.groupby("Stock", as_index=False)["Close"].mean().sort_values("Close", ascending=False)
    )


# Average Trading Volume

def get_average_volume(df):
    return (
        df.groupby("Stock", as_index=False)["Volume"].mean().sort_values("Volume", ascending=False)
    )


# Average Daily Return

def get_average_daily_return(df):
    return (
        df.groupby("Stock", as_index=False)["Daily_Return"].mean().sort_values("Daily_Return", ascending=False)
    )


# Total Return

def get_total_return(df):
    performance = (
        df.groupby("Stock").agg(First_Close=("Close", "first"), Last_Close=("Close", "last"))
    )

    performance["Total_Return"] = ((performance["Last_Close"]-performance["First_Close"])/performance["First_Close"]) * 100
    performance.reset_index(inplace=True) #since stock is an index (as_index=False not written) 
    performance.sort_values("Total_Return", ascending=False, inplace=True)
    return performance


# Volatility

def get_volatility(df):
    volatility = (
        df.groupby("Stock", as_index=False)["Daily_Return"].std()
    )

    volatility.rename(columns={"Daily_Return": "Volatility"}, inplace=True)
    volatility.sort_values("Volatility", ascending=False, inplace=True)
    return volatility


# Correlation Matrix

def get_correlation(df):
    close_prices = df.pivot(index="Date", columns="Stock", values="Close")
    return close_prices.corr()