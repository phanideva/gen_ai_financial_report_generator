import os
import subprocess

def run_pipeline():
    """Execute the full financial report generation pipeline."""
    print("Fetching and preprocessing data...")
    subprocess.run(["python", "scripts/data_preprocessing.py"])

    print("Performing financial analysis...")
    subprocess.run(["python", "scripts/financial_analysis.py"])

    print("Generating AI-powered financial report...")
    subprocess.run(["python", "scripts/generate_report.py"])

    print("Running real-time financial dashboard...")
    subprocess.run(["streamlit", "run", "scripts/real_time_dashboard.py"])

if __name__ == "__main__":
    run_pipeline()