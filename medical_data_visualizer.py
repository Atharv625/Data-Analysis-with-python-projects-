import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    df = pd.read_csv("medical.csv")
    
    # Calculate BMI and determine overweight status
    df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = (df['BMI'] > 25).astype(int)
    df.drop(columns=['BMI'], inplace=True)
    
    # Normalize cholesterol and glucose values (0 = good, 1 = bad)
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
    
    return df

def draw_cat_plot():
    df = load_data()
    
    # Convert data into long format
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Group and count occurrences
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Create the categorical plot
    g = sns.catplot(
        x="variable", y="total", hue="value", col="cardio",
        data=df_cat, kind="bar", height=5, aspect=1
    )
    
    fig = g.fig
    return fig

def draw_heat_map():
    df = load_data()
    
    # Clean the data based on given conditions
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Compute the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', linewidths=0.5)
    
    return fig
