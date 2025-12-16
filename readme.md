# PharmaSage AI – Agentic Drug Repurposing Intelligence

## Overview
PharmaSage AI is a **conceptual agentic AI platform** for drug repurposing analysis.
It demonstrates architecture, flow, and UI wireframes using Streamlit.

This repository is intended for **hackathon / academic / prototype submission**.

---

## Features
- Agent-based architecture (Literature, Clinical, Patent, Market)
- Orchestrator-driven workflow
- Evidence scoring & ranking
- Interactive dashboard wireframe
- Sample visualizations

---

## Repository Structure
├── app.py # Streamlit dashboard wireframe
├── architecture.md # System architecture diagram (Mermaid)
├── flowchart.md # Workflow flowchart (Mermaid)
├── requirements.txt # Python dependencies
├── README.md

## Demo Instructions

1. Clone the repository:
git clone <repo_url>
cd <repo_folder> 

2. Install dependencies: 
pip install -r requirements.txt

3. Run the dashboard:
streamlit run app.py

4. In the sidebar:
Enter Molecule Name (e.g., Metformin, Aspirin)
Enter Research Objective
Click Run Analysis (if using button)

5. Observe:
Table & charts update dynamically based on molecule input
Agent execution status updates
Download dummy PDF report

