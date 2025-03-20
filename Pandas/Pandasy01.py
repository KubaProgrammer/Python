import argparse
import pandas as pd

def load_data(input_file):
    """Wczytuje plik CSV lub Excel."""
    if input_file.endswith('.csv'):
        return pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        return pd.read_excel(input_file)
    else:
        raise ValueError("Nieobsługiwany format pliku. Użyj CSV lub Excel.")

def filter_by_age(df, age_range):
    """Filtruje dane na podstawie przedziału wieku."""
    if age_range:
        try:
            min_age, max_age = map(int, age_range.split('-'))
            return df[(df["Age"] >= min_age) & (df["Age"] <= max_age)]
        except ValueError:
            raise ValueError("Niepoprawny format zakresu wieku. Użyj formatu 'min-max', np. '30-40'.")
    return df

def save_data(df, output_file, file_format):
    """Zapisuje dane do pliku CSV lub Excel."""
    if output_file:
        if file_format == 'csv':
            df.to_csv(output_file, index=False)
        elif file_format == 'excel':
            df.to_excel(output_file, index=False)
        print(f"Dane zapisano do {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Analiza danych pasażerów Titanica.")
    parser.add_argument('-i', '--input', type=str, required=True, help="Ścieżka do pliku wejściowego (CSV lub Excel)")
    parser.add_argument('-o', '--output', type=str, help="Ścieżka do pliku wyjściowego")
    parser.add_argument('-f', '--format', type=str, choices=['csv', 'excel'], default='csv', help="Format pliku wyjściowego")
    parser.add_argument('--age_range', type=str, help="Zakres wieku do filtrowania, np. '30-40'")
    parser.add_argument('-v', '--verbosity', action='store_true', help="Włącz szczegółowy tryb działania")
    
    args = parser.parse_args()
    
    df = load_data(args.input)
    if args.verbosity:
        print("Załadowano dane:")
        print(df.head())
    
    df_filtered = filter_by_age(df, args.age_range)
    if args.verbosity:
        print("Po filtrowaniu:")
        print(df_filtered.head())
    
    save_data(df_filtered, args.output, args.format)
    
if __name__ == "__main__":
    main()
