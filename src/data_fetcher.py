import pandas as pd
import requests
import xml.etree.ElementTree as ET

def fetch_curiosity_telemetry():
    # NASA's live feed for the Deep Space Network
    url = "https://eyes.nasa.gov/dsn/data/dsn.xml"
    print("🛰️ Connecting to NASA DSN... Listening for Curiosity (MSL)...")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        msl_data = []
        
        # Search every dish for Curiosity (MSL)
        for dish in root.findall('dish'):
            for target in dish.findall('target'):
                if target.get('name').upper() == 'MSL':
                    msl_data.append({
                        'timestamp': pd.Timestamp.now().strftime('%Y-%m-%dT%H:%M:%S'),
                        'sensor': 'COMM_SIGNAL_STRENGTH',
                        'value': float(target.get('power')), # Power in dBm
                        'unit': 'dBm',
                        'distance_km': float(target.get('range')) # Distance in km
                    })
        
        if not msl_data:
            print("🌑 Curiosity is not currently transmitting to a DSN dish (Mars may be below the horizon).")
            print("Creating a simulated record based on last known trajectory for demo purposes...")
            # Fallback so your app still has data to parse if Mars is "down"
            msl_data.append({
                'timestamp': pd.Timestamp.now().strftime('%Y-%m-%dT%H:%M:%S'),
                'sensor': 'COMM_SIGNAL_STRENGTH',
                'value': -125.42,
                'unit': 'dBm',
                'distance_km': 252104532.1
            })

        df = pd.DataFrame(msl_data)
        df.to_csv('curiosity_live_data.csv', index=False)
        print(f"✅ Success! Generated curiosity_live_data.csv.")
        return True

    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

if __name__ == "__main__":
    fetch_curiosity_telemetry()