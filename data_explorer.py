# Project: Python Data Explorer - v1.0
# Python Data Explorer
# Author: Warny Palhares
#
# Description:
# A simple command-line tool to perform a basic exploratory data analysis (EDA) on a CSV file.
# The tool provides summary statistics and generates visualizations to help understand the dataset.
#
# How to run:
# 1. Make sure you have the required libraries installed (pandas, matplotlib, seaborn).
# 2. Run the script from your terminal: python data_explorer.py
# 3. Follow the on-screen prompts.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def print_welcome_message():
    """Imprime uma mensagem de boas-vindas ao utilizador."""
    print("=============================================")
    print("===      Python Data Explorer Tool        ===")
    print("=============================================")
    print("Esta ferramenta irá realizar uma análise básica no seu ficheiro CSV.\n")

def get_csv_filepath():
    """Pede ao utilizador para inserir o caminho para o ficheiro CSV e valida-o."""
    while True:
        filepath = input("Por favor, insira o caminho completo para o seu ficheiro CSV: ")
        if os.path.exists(filepath) and filepath.endswith('.csv'):
            return filepath
        else:
            print("Erro: Ficheiro não encontrado ou não é um CSV. Por favor, verifique o caminho e tente novamente.\n")

def load_data(filepath):
    """Carrega o ficheiro CSV para um DataFrame do pandas."""
    try:
        print(f"\nA carregar dados de {filepath}...")
        df = pd.read_csv(filepath)
        print("Dados carregados com sucesso!")
        return df
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
        return None

def show_basic_info(df):
    """Imprime informações básicas sobre o DataFrame."""
    print("\n--- 1. Informações Básicas ---")
    print("\nFormato do dataset (Linhas, Colunas):", df.shape)
    print("\nPrimeiras 5 linhas do dataset:")
    print(df.head())
    print("\nTipos de dados de cada coluna:")
    df.info()

def show_summary_statistics(df):
    """Imprime estatísticas de resumo para as colunas numéricas."""
    print("\n--- 2. Estatísticas de Resumo (para colunas numéricas) ---")
    print(df.describe())

def generate_visualizations(df, filepath):
    """Gera e guarda visualizações básicas para os dados."""
    print("\n--- 3. A gerar Visualizações ---")
    
    output_dir = "analysis_plots"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"Os gráficos serão guardados na pasta '{output_dir}'.")

    numerical_df = df.select_dtypes(include=['number'])

    if not numerical_df.empty:
        plt.figure(figsize=(12, 8))
        sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Mapa de Calor de Correlação das Colunas Numéricas')
        heatmap_path = os.path.join(output_dir, 'correlation_heatmap.png')
        plt.savefig(heatmap_path)
        plt.close()
        print(f"- Mapa de calor de correlação guardado em {heatmap_path}")

    for col in numerical_df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribuição de {col}')
        hist_path = os.path.join(output_dir, f'hist_{col}.png')
        plt.savefig(hist_path)
        plt.close()
    print(f"- Histogramas para todas as colunas numéricas guardados.")

    categorical_df = df.select_dtypes(include=['object', 'category'])
    if not categorical_df.empty:
        for col in categorical_df.columns:
            if df[col].nunique() < 20:
                plt.figure(figsize=(12, 7))
                sns.countplot(y=df[col], order=df[col].value_counts().index)
                plt.title(f'Contagem de Categorias em {col}')
                plt.tight_layout()
                count_path = os.path.join(output_dir, f'count_{col}.png')
                plt.savefig(count_path)
                plt.close()
        print(f"- Gráficos de contagem para colunas categóricas guardados.")
    
    print("\nVisualizações geradas com sucesso!")

def main():
    """Função principal para executar o explorador de dados."""
    print_welcome_message()
    filepath = get_csv_filepath()
    df = load_data(filepath)
    
    if df is not None:
        show_basic_info(df)
        show_summary_statistics(df)
        generate_visualizations(df, filepath)
        print("\n=============================================")
        print("===        Análise Concluída!             ===")
        print("=============================================")

if __name__ == "__main__":
    main()

