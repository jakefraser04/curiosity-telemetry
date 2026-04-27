import pandas as pd

def load_telemetry(file_path):
    """Loads CSV and returns a DataFrame."""
    return pd.read_csv(file_path)

def analyze_health(df):
    """Returns a dictionary of mean, min, and max values per sensor."""
    return df.groupby('sensor')['value'].agg(['mean', 'min', 'max']).to_dict('index')

def find_anomalies(df, threshold=-40.0):
    """Flags any temperature readings below the safety threshold."""
    temp_data = df[df['sensor'] == 'BATTERY_TEMP']
    return temp_data[temp_data['value'] < threshold]