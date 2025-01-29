import openai
import pandas as pd
from jinja2 import Template
import pdfkit

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

def generate_financial_summary(data):
    """Use AI to generate financial insights from data."""
    prompt = f"""
    Here is the financial data:

    {data.to_string()}

    Provide an executive summary of key trends and insights.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def create_report(summary):
    """Generate a financial report using Jinja2 templates."""
    template_text = """
    <html>
    <head><title>Financial Report</title></head>
    <body>
    <h1>Automated Financial Report</h1>
    <p>{{ summary }}</p>
    </body>
    </html>
    """
    template = Template(template_text)
    report_html = template.render(summary=summary)

    # Save as PDF
    pdfkit.from_string(report_html, "outputs/reports/financial_report.pdf")

if __name__ == "__main__":
    df = pd.read_csv("data/processed/financial_data.csv")
    summary = generate_financial_summary(df)
    create_report(summary)
    print("Financial report generated successfully!")