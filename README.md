Python Data Explorer
📖 Overview
Python Data Explorer is a simple yet powerful command-line tool designed to perform a preliminary Exploratory Data Analysis (EDA) on any given CSV dataset. The primary goal of this project is to automate the initial steps of data analysis, providing a quick overview of the dataset's structure, statistical properties, and relationships between variables.

This project was developed as a key component of my personal portfolio as I transition my career into the fields of Artificial Intelligence and Data Science. It serves as a practical application of foundational Python skills for data manipulation and visualization.

✨ Features
Data Loading: Securely loads data from a user-specified CSV file path.

Basic Information: Displays the dataset's shape (rows and columns), the first 5 rows (.head()), and a summary of data types for each column (.info()).

Summary Statistics: Generates descriptive statistics for all numerical columns (.describe()), including count, mean, standard deviation, and quartiles.

Automated Visualizations: Automatically generates and saves key visualizations to a new analysis_plots directory:

A correlation heatmap for all numerical features to visualize relationships.

Histograms for each numerical column to understand their distributions.

Count plots for categorical columns (with low cardinality) to show frequency distributions.

🛠️ Technologies Used
Language: Python 3

Core Libraries:

Pandas: For data loading, manipulation, and analysis.

Matplotlib: For creating static, animated, and interactive visualizations.

Seaborn: For making attractive and informative statistical graphics.

🚀 How to Run
Clone the repository:

git clone [https://github.com/it-warny/python-data-explorer.git](https://github.com/it-warny/python-data-explorer.git)
cd python-data-explorer

Install dependencies:
Make sure you have Python 3 installed. Then, install the required libraries using the requirements.txt file.

pip install -r requirements.txt

Execute the script:
Run the script from your terminal.

python data_explorer.py

Follow the prompts:
The script will ask you to provide the full path to the CSV file you wish to analyze. Once provided, the analysis will run, and the generated plots will be saved in the analysis_plots folder.
