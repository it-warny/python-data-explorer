<div align="center">
<h1 align="center">Python Data Explorer</h1>
<strong>An automated command-line tool for Exploratory Data Analysis (EDA) on CSV files.</strong>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Pandas-Library-green?style=for-the-badge&logo=pandas" alt="Pandas">
  <img src="https://img.shields.io/badge/Seaborn-Library-orange?style=for-the-badge&logo=seaborn" alt="Seaborn">
</div>

<br>

<p align="center">
  <a href="#-about-the-project">About</a> •
  <a href="#-key-features">Features</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-usage-example">Usage</a>
</p>

---

## 🚀 About The Project

Welcome to the Python Data Explorer! This tool was developed as a key portfolio project to showcase foundational data science skills. It addresses a common and crucial task for any data professional: performing an initial **Exploratory Data Analysis (EDA)**.

Instead of manually writing the same code to inspect every new dataset, this script automates the process, providing a comprehensive overview of any CSV file in seconds. It's a practical demonstration of leveraging Python for efficiency and data-driven insights.



## ✨ Key Features

-   **Automated EDA:** Runs a full preliminary analysis with a single command.
-   **Key Insights:** Provides instant information on shape, data types, and missing values.
-   **Statistical Summary:** Automatically calculates descriptive statistics for all numerical columns.
-   **Smart Visualizations:** Generates and saves essential plots to a dedicated folder:
    -   **Correlation Heatmap** to identify relationships.
    -   **Histograms** to view data distribution.
    -   **Count Plots** for categorical data.

## 🛠️ Built With

This project was built using the core libraries of the Python Data Science ecosystem:

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)

## 🏁 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3 installed on your system.

### Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone [https://github.com/it-warny/python-data-explorer.git](https://github.com/it-warny/python-data-explorer.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd python-data-explorer
    ```
3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage Example

1.  Run the script from your terminal:
    ```bash
    python data_explorer.py
    ```
2.  When prompted, enter the full path to the CSV file you want to analyze.
3.  The script will print the analysis directly to your terminal and save the generated graphs in a new `analysis_plots` folder in the same directory.

<br>

---
<p align="center">
  Developed by <a href="https://www.linkedin.com/in/it-warny/">Warny Palhares</a>
</p>


---