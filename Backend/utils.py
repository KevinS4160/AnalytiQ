import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

UPLOAD_FOLDER = "uploads"

def load_dataframe(file_path):
    """Loads CSV or JSON into a DataFrame."""
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".json"):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format")

def save_plot(fig, filename):
    """Saves plot to a file and returns its path."""
    file_path = os.path.join(UPLOAD_FOLDER, f"{filename}.png")
    fig.savefig(file_path)
    plt.close(fig)
    return file_path

def generate_heatmap(df):
    """ Generates and saves a correlation heatmap. """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    return save_plot(fig, "heatmap")

def generate_histogram(df, column):
    """ Generates and saves a histogram for a specific column. """
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    return save_plot(fig, f"histogram_{column}")

def generate_3d_scatter(df, x, y, z):
    """ Generates a 3D scatter plot. """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(df[x], df[y], df[z], c="r", marker="o")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    return save_plot(fig, "scatter_3d")

def generate_line_plot(df, x, y):
    """ Generates a line plot. """
    fig, ax = plt.subplots()
    sns.lineplot(x=df[x], y=df[y], ax=ax)
    return save_plot(fig, f"lineplot_{x}_{y}")

def generate_box_plot(df, column):
    """ Generates a box plot. """
    fig, ax = plt.subplots()
    sns.boxplot(y=df[column], ax=ax)
    return save_plot(fig, f"boxplot_{column}")

def generate_pair_plot(df):
    """ Generates a pair plot. """
    pairplot = sns.pairplot(df)
    return save_plot(pairplot.fig, "pairplot")

def generate_bar_chart(df, category, value):
    """ Generates a bar chart comparing categories. """
    fig, ax = plt.subplots()
    sns.barplot(x=df[category], y=df[value], ax=ax)
    return save_plot(fig, f"barchart_{category}_{value}")

def generate_density_plot(df, column):
    """ Generates a density plot (KDE plot). """
    fig, ax = plt.subplots()
    sns.kdeplot(df[column], fill=True, ax=ax)
    return save_plot(fig, f"densityplot_{column}")

def process_data(file_path: str):
    """ Reads CSV/JSON and returns summary statistics & missing values. """
    df = load_dataframe(file_path)  # Load the data properly
    summary = df.describe().to_dict()
    missing_values = df.isnull().sum().to_dict()
    return {"summary": summary, "missing_values": missing_values, "columns": list(df.columns)}
