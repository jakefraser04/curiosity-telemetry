# AI Collaboration Log (AGENTS.md)

## **Project Lead: Jake Fraser**
**Collaborator:** Gemini (Google)

## **Overview**
I utilized Gemini as a technical consultant and pair-programmer to build a robust CLI tool that interfaces with NASA's Deep Space Network (DSN). My role was to define the project scope, make executive decisions on data fallback strategies, and lead the debugging process for environment-specific issues.

## **Where AI Helped**
* **API Ingestion:** Provided the initial logic for parsing NASA’s DSN XML feed.
* **Refactoring:** Assisted in modularizing the code into a professional `src/` and `tests/` structure.
* **CI/CD Configuration:** Helped troubleshoot GitHub Actions pathing issues (exit code 5) by suggesting the use of `python -m pytest`.

## **Where I Led (Key Engineering Decisions)**
* **The 3-Tier Data Strategy:** I directed the AI to implement a specific hierarchy for data reliability: **Live API -> Local Cache -> Randomized Simulation**. This ensures the tool is functional even when Mars is out of line-of-sight.
* **Defensive Programming:** After encountering a `NoneType` error from the live NASA feed, I identified the need for a guard clause to handle empty `power` attributes, preventing application crashes during live transmissions.
* **UX & Accessibility:** I made the call to remove Unicode emojis to ensure the CLI remains compatible with older Windows terminal encodings (CP1252), prioritizing broad user accessibility over aesthetics.
* **Simulation Design:** I specified that simulated data should not be a static number, but a distribution of 10 records with random noise to better test the statistical analysis functions of the parser.

## **Key Learnings**
This project taught me that "real" data is messy. Building a tool that talks to a spacecraft millions of miles away requires more than just logic; it requires a strategy for handling connectivity gaps and hardware-specific limitations. I gained significant experience in state management and cross-platform Python deployment.