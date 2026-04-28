import argparse
import sys
import os

# This ensures the script can find its sibling files (like data_fetcher.py)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# We are importing from YOUR file name: data_fetcher
from parser import load_telemetry, analyze_health, find_anomalies
from data_fetcher import fetch_curiosity_telemetry

def main():
    parser = argparse.ArgumentParser(description="Curiosity Telemetry Parser")
    parser.add_argument("file", nargs='?', help="Path to the telemetry CSV file")
    parser.add_argument("--fetch", action="store_true", help="Fetch LIVE Curiosity comms telemetry")
    parser.add_argument("--anomalies", action="store_true", help="Check for signal anomalies")
    args = parser.parse_args()

    # If the user uses the --fetch flag, we run the logic from data_fetcher.py
    if args.fetch:
        if fetch_curiosity_telemetry():
            args.file = 'curiosity_live_data.csv'
        else:
            return

    if not args.file:
        print("Error: Please provide a file or use --fetch to get live data.")
        return

    try:
        data = load_telemetry(args.file)
        print(f"\n--- Curiosity Live Report: {args.file} ---")
        
        health = analyze_health(data)
        print(f"{'SENSOR':20} | {'AVG':>10} | {'MIN':>10} | {'MAX':>10}")
        print("-" * 56)
        
        for sensor, stats in health.items():
            print(f"{sensor:20} | {stats['mean']:>10.2f} | {stats['min']:>10.2f} | {stats['max']:>10.2f}")

        if args.anomalies:
            # -130 dBm is the standard threshold for a weak signal in deep space
            anomalies = find_anomalies(data, threshold=-130.0) 
            if not anomalies.empty:
                print("\n[!] WEAK SIGNAL DETECTED!")
                print(anomalies[['timestamp', 'value']])
            else:
                print("\n[+] Signal strength is within safe mission parameters.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()