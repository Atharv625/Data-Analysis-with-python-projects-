import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")
    
    # Line of best fit for entire dataset
    slope, intercept, _, _, _ = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label="Best Fit (1880-2050)")
    
    # Line of best fit from year 2000 onward
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = stats.linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, intercept_recent + slope_recent * years_recent, 'g', label="Best Fit (2000-2050)")
    
    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()

if __name__ == "__main__":
    draw_plot()