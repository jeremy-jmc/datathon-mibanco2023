import matplotlib.pyplot as plt
import pandas as pd

def do_hist(df: pd.DataFrame, col: str, type='numeric'):
    if type == 'numeric':
        nan_count = df[col].isna().sum()
        plt.hist(df[col], color='skyblue', edgecolor='black')
        plt.text(0.8, 0.8, f'NaN: {nan_count}', transform=plt.gca().transAxes, color='red')
        plt.show()
    elif type == 'categorical':
        nan_count = df[col].isna().sum()
        counts = df[col].value_counts()
        plt.bar(counts.index, counts.values, color='skyblue', edgecolor='black')
        plt.text(0.8, 0.8, f'NaN: {nan_count}', transform=plt.gca().transAxes, color='red')
        plt.xticks(rotation=90)
        plt.show()