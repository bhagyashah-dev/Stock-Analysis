import plotly.express as px
import plotly.graph_objects as go


# =====================================================
# Market Comparison
# =====================================================

def average_close_chart(df):

    fig = px.bar(
        df,
        x="Close",
        y="Stock",
        orientation="h",
        title="Average Closing Price by Company",
        labels={
            "Close": "Average Closing Price (₹)",
            "Stock": "Company"
        },
        hover_data={
            "Close": ":.2f"
        }
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        showlegend=False
    )

    return fig


def average_volume_chart(df):

    fig = px.bar(
        df,
        x="Volume",
        y="Stock",
        orientation="h",
        title="Average Trading Volume by Company",
        labels={
            "Volume": "Average Trading Volume",
            "Stock": "Company"
        }
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        showlegend=False
    )

    return fig


# =====================================================
# Price Analysis
# =====================================================

def closing_price_chart(df, company):

    fig = px.line(
        df,
        x="Date",
        y="Close",
        title=f"{company} Closing Price Trend"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Closing Price (₹)",
        hovermode="x unified"
    )

    return fig


def volume_trend_chart(df, company):

    fig = px.line(
        df,
        x="Date",
        y="Volume",
        title=f"{company} Trading Volume Trend"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Volume",
        hovermode="x unified"
    )

    return fig


# =====================================================
# Technical Analysis
# =====================================================

def moving_average_chart(df, company):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["Close"],
            name="Close"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["MA20"],
            name="MA20"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["MA50"],
            name="MA50"
        )
    )

    fig.update_layout(
        title=f"{company} Moving Average Analysis",
        xaxis_title="Date",
        yaxis_title="Price (₹)",
        hovermode="x unified"
    )

    return fig


# =====================================================
# Performance Analysis
# =====================================================

def average_daily_return_chart(df):

    fig = px.bar(
        df,
        x="Daily_Return",
        y="Stock",
        orientation="h",
        title="Average Daily Return by Company",
        labels={
            "Daily_Return": "Average Daily Return (%)",
            "Stock": "Company"
        }
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        showlegend=False
    )

    return fig


def total_return_chart(df):

    fig = px.bar(
        df,
        x="Total_Return",
        y="Stock",
        orientation="h",
        title="Total Return by Company",
        labels={
            "Total_Return": "Total Return (%)",
            "Stock": "Company"
        }
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        showlegend=False
    )

    return fig


def volatility_chart(df):

    fig = px.bar(
        df,
        x="Volatility",
        y="Stock",
        orientation="h",
        title="Stock Volatility",
        labels={
            "Volatility": "Volatility",
            "Stock": "Company"
        }
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        showlegend=False
    )

    return fig


# =====================================================
# Correlation Analysis
# =====================================================

def correlation_heatmap(df):

    fig = px.imshow(
        df,
        text_auto=".2f",
        aspect="auto",
        title="Correlation Heatmap"
    )

    return fig

# Daily Return

def daily_return_chart(df, company):

    fig = px.line(
        df,
        x="Date",
        y="Daily_Return",
        title=f"{company} Daily Return Trend"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Daily Return (%)",
        hovermode="x unified"
    )

    return fig

# Relationships

def open_close_chart(df, company):

    fig = px.scatter(
        df,
        x="Open",
        y="Close",
        title=f"{company} Open Price vs Closing Price",
        # trendline="ols"
    )

    fig.update_layout(
        xaxis_title="Open Price (₹)",
        yaxis_title="Closing Price (₹)"
    )

    return fig

def volume_close_chart(df, company):

    fig = px.scatter(
        df,
        x="Volume",
        y="Close",
        title=f"{company} Trading Volume vs Closing Price",
        # trendline="ols"
    )

    fig.update_layout(
        xaxis_title="Trading Volume",
        yaxis_title="Closing Price (₹)"
    )

    return fig