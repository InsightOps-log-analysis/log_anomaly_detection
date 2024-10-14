import pandas as pd

def load_data(file_path):
    """Load the log data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Perform data cleaning on the DataFrame."""
    df.dropna(inplace=True)  # Drop rows with NaN values
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert timestamp to datetime
    print(df.head())  # Print the first few rows of the cleaned DataFrame
    return df
