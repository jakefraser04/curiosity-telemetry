import pandas as pd

def load_telemetry(file_path):
    """Loads CSV and returns a DataFrame."""
    return pd.read_csv(file_path)

def analyze_health(df):
    """Returns a dictionary of mean, min, and max values per sensor."""
    return df.groupby('sensor')['value'].agg(['mean', 'min', 'max']).to_dict('index')

def find_anomalies(df, threshold=-0.9):
    """Flags any readings below the safety threshold (normalized scale)."""
    # Check both Battery and Power sensors
    anomalies = df[df['value'] < threshold]
    return anomalies