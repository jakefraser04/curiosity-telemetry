AI Collaboration Log (AGENTS.md)
Overview of AI Use
I collaborated with Gemini (Google) to architect and troubleshoot a CLI application that parses Mars rover telemetry. The AI acted as a technical consultant for API integration and a debugging partner for environment-specific issues (Linux/GitHub Actions vs. Windows/Local).

Where AI Helped
API Architecture: Provided the logic for connecting to NASA’s DSN (Deep Space Network) XML feed and parsing the complex tree structure into a usable CSV.

CI/CD Troubleshooting: Resolved a "Process completed with exit code 5" error in GitHub Actions by identifying pathing issues and recommending the addition of __init__.py files and the python -m pytest command.

Resiliency Logic: Drafted a fallback mechanism to handle real-world "line-of-sight" issues when the Curiosity rover is not actively transmitting to a DSN station.

Where I Led
Project Integrity: I steered the project back to the Curiosity (MSL) mission when technical hurdles made switching to an asteroid API tempting. I insisted on maintaining the original project scope to match the repository branding.

Feature Specification: I defined the requirement for a --fetch flag and an --anomalies flag to ensure the tool felt like a professional utility rather than just a script.

Logic Verification: I manually verified that the signal strength thresholds (-130 dBm) were scientifically appropriate for the Deep Space Network's operational limits.

Key Learnings
This project highlighted the gap between "perfect" code and "real-world" connectivity. Dealing with ConnectionResetError and 404s taught me that robust applications need built-in fallbacks. I also gained a much deeper understanding of the Python Module Search Path and how package imports function differently across different operating systems.