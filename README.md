# Curiosity Telemetry Parser

A command-line interface (CLI) tool designed to process and analyze health telemetry from the Mars Science Laboratory (MSL) rover, Curiosity. This tool parses sensor data to provide health summaries and detect critical safety anomalies.

## What it does
This application ingests telemetry logs (currently supporting CSV format) containing rover sensor readings like battery temperature, power output, and signal strength. It calculates key performance metrics (mean, min, max) and flags readings that fall outside of safe operating limits, which is vital for maintaining the rover's longevity in the harsh Martian environment.

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
Run the tool by passing a telemetry file path. Use the --anomalies flag to trigger safety checks.
```bash
python src/main.py telemetry_sample.csv --anomalies
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
