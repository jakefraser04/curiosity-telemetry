# Curiosity Telemetry Parser

A command-line interface (CLI) tool designed to process and analyze live communication and health telemetry from the Mars Science Laboratory (MSL) rover, Curiosity, via NASA's Deep Space Network (DSN).

## What it does
This application connects to NASA's live Deep Space Network (DSN) feed to track active communications between Earth and the Curiosity rover. It features a robust 3-tier data pipeline to ensure the tool is functional regardless of Martian orbital position:

1. **Live XML Parsing:** Ingests NASA's DSN XML stream to identify MSL signal strength and distance in real-time.
2. **Persistent Caching:** If Curiosity is "below the horizon," the tool automatically retrieves the last successfully recorded data point from a local cache.
3. **Simulated Fallback:** Provides a randomized statistical baseline for initial setup and stress-testing anomaly detection.

## Installation
Ensure you have Python 3.10+ installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jakefraser04/curiosity-telemetry.git
   cd curiosity-telemetry
   ```

2. **Create and activate a virtual environment:**
```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage
Run the tool using the --fetch flag to pull live data directly from NASA, or provide a local CSV file path. Use the --anomalies flag to trigger safety checks.
```bash
python src/main.py --fetch --anomalies
```

## Examples

1. Basic Health Report
```bash
python src/main.py telemetry_sample.csv
```
**Output:** Provides a breakdown of average, minimum, and maximum values for every sensor detected in the file.

2. Anomoly Detection
```bash
python src/main.py telemetry_sample.csv --anomalies
```
**Output:**
If any sensor readings exceed safety thresholds (e.g., Battery Temp < -40°C), the tool prints a specific warning list with timestamps for mission control review.
