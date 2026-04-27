import argparse
from parser import load_telemetry, analyze_health, find_anomalies

def main():
    parser = argparse.ArgumentParser(description="Curiosity Rover Telemetry Parser")
    parser.add_argument("file", help="Path to the telemetry CSV file")
    parser.add_argument("--anomalies", action="store_true", help="Check for safety violations")
    args = parser.parse_args()

    try:
        data = load_telemetry(args.file)
        print(f"\n--- Telemetry Report: {args.file} ---")
        
        health = analyze_health(data)
        for sensor, stats in health.items():
            print(f"{sensor:15} | Avg: {stats['mean']:>7.2f} | Range: [{stats['min']}, {stats['max']}]")

        if args.anomalies:
            anomalies = find_anomalies(data)
            if not anomalies.empty:
                print("\n[!] WARNING: Anomalies Detected!")
                print(anomalies[['timestamp', 'sensor', 'value']])
            else:
                print("\n[+] All systems within safe operating limits.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()