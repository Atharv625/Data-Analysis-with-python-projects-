import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data():
    df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)
    lower_bound = df["value"].quantile(0.025)
    upper_bound = df["value"].quantile(0.975)
    df = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]
    return df

def draw_line_plot():
    df = load_and_clean_data()
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.savefig("line_plot.png")
    return fig

def draw_bar_plot():
    df = load_and_clean_data()
    df["year"] = df.index.year
    df["month"] = df.index.month
    df_bar = df.groupby(["year", "month"]).mean().unstack()
    
    fig = df_bar.plot(kind="bar", figsize=(12, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.savefig("bar_plot.png")
    return fig

def draw_box_plot():
    df = load_and_clean_data()
    df["year"] = df.index.year
    df["month"] = df.index.strftime("%b")
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x="year", y="value", data=df, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(x="month", y="value", data=df, ax=axes[1], order=month_order)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    plt.savefig("box_plot.png")
    return fig
