import pytest
import pandas as pd
from src.parser import analyze_health, find_anomalies

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'sensor': ['BATTERY_TEMP', 'BATTERY_TEMP', 'POWER_OUTPUT'],
        'value': [20.0, -50.0, 100.0],
        'timestamp': ['T1', 'T2', 'T3']
    })

def test_load_telemetry_error():
    """Test 1: Verify error handling for missing files."""
    with pytest.raises(Exception):
        from src.parser import load_telemetry
        load_telemetry("non_existent_file.csv")

def test_analyze_health_averages(sample_df):
    """Test 2: Verify mean calculation."""
    health = analyze_health(sample_df)
    assert health['BATTERY_TEMP']['mean'] == -15.0

def test_analyze_health_min_max(sample_df):
    """Test 3: Verify range detection."""
    health = analyze_health(sample_df)
    assert health['BATTERY_TEMP']['min'] == -50.0
    assert health['BATTERY_TEMP']['max'] == 20.0

def test_anomaly_detection_true(sample_df):
    """Test 4: Verify that anomalies are caught."""
    anomalies = find_anomalies(sample_df, threshold=-40.0)
    assert len(anomalies) == 1

def test_anomaly_detection_none(sample_df):
    """Test 5: Verify no anomalies found when within limits."""
    anomalies = find_anomalies(sample_df, threshold=-60.0)
    assert len(anomalies) == 0