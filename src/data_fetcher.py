import pandas as pd
import requests
import xml.etree.ElementTree as ET
import os
import random

def fetch_curiosity_telemetry():
    url = "https://eyes.nasa.gov/dsn/data/dsn.xml"
    cache_file = 'last_known_state.csv'
    output_file = 'curiosity_live_data.csv'
    
    print("Connecting to NASA DSN... Listening for Curiosity (MSL)...")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        msl_data = []
        
        for dish in root.findall('dish'):
            for target in dish.findall('target'):
                if target.get('name', '').upper() == 'MSL':
                    power_raw = target.get('power')
                    if power_raw and power_raw.strip():
                        msl_data.append({
                            'timestamp': pd.Timestamp.now().strftime('%Y-%m-%dT%H:%M:%S'),
                            'sensor': 'COMM_SIGNAL_STRENGTH',
                            'value': float(power_raw),
                            'unit': 'dBm',
                            'status': 'LIVE'
                        })
        
        # --- HIERARCHY 1: LIVE DATA ---
        if msl_data:
            df = pd.DataFrame(msl_data)
            df.to_csv(cache_file, index=False)
            df.to_csv(output_file, index=False)
            print("SUCCESS: Real-time telemetry captured from NASA DSN.")
            return True
        
        # --- HIERARCHY 2: CACHED DATA ---
        elif os.path.exists(cache_file):
            print("\n--- Mission Status: Offline ---")
            print("Curiosity is out of sight. Accessing last known transmission...")
            df = pd.read_csv(cache_file)
            df['status'] = 'CACHED'
            df.to_csv(output_file, index=False)
            print(f"SUCCESS: Loaded historical data from {df['timestamp'].iloc[0]}.")
            return True
            
        # --- HIERARCHY 3: SIMULATED DATA (CLEAR ANNOUNCEMENT) ---
        else:
            print("\n--- Mission Status: No Data Found ---")
            print("1. LIVE: No active MSL transmission detected on the DSN.")
            print("2. CACHE: No 'last_known_state.csv' found in local storage.")
            print("\nPROCEEDING: Generating a varied simulated baseline for testing...")
            
            simulated_records = []
            base_signal = -125.0
            for i in range(10):
                noise = random.uniform(-2.0, 2.0)
                # 10% chance for an anomaly
                value = -140.0 if random.random() < 0.1 else base_signal + noise
                
                simulated_records.append({
                    'timestamp': pd.Timestamp.now().strftime('%Y-%m-%dT%H:%M:%S'),
                    'sensor': 'COMM_SIGNAL_STRENGTH',
                    'value': round(value, 2),
                    'unit': 'dBm',
                    'status': 'SIMULATED'
                })
            
            df = pd.DataFrame(simulated_records)
            df.to_csv(output_file, index=False)
            print(f"SUCCESS: {len(df)} simulated records generated.")
            return True

    except Exception as e:
        if os.path.exists(cache_file):
            pd.read_csv(cache_file).to_csv(output_file, index=False)
            print(f"NETWORK ERROR: {e}. Using cached data.")
            return True
        print(f"FATAL ERROR: {e}")
        return False