# **Real-time Automated Financial Report Generation & Analysis**

## **Project Overview**
This project automates financial report generation and analysis using **Generative AI**. It fetches real-time financial data, processes it, performs financial analysis, and generates **automated AI-powered financial reports**.

### **Key Features**
- Fetch real-time financial data using **Yahoo Finance API**.
- Clean and preprocess financial data.
- Perform **technical and fundamental analysis** on stock data.
- Generate AI-powered **financial reports** using OpenAI's **GPT**.
- Visualize stock performance with **interactive charts**.
- Deploy a **real-time financial dashboard** using **Streamlit**.

---

## **Project Structure**
```
financial_report_automation/
│── data/                         # Raw and processed financial data
│   ├── raw/                      # Raw stock market data
│   ├── processed/                 # Cleaned and processed data
│
│── models/                        # Trained AI/NLP models
│   ├── financial_nlp_model.pkl    # AI model for financial analysis
│
│── notebooks/                     # Jupyter notebooks for development & testing
│   ├── data_preprocessing.ipynb   # Data processing workflow
│   ├── financial_analysis.ipynb   # Financial analysis implementation
│   ├── report_generation.ipynb    # Automated report generation
│
│── scripts/                        # Python scripts for automation
│   ├── data_preprocessing.py      # Fetch & preprocess stock data
│   ├── financial_analysis.py      # Perform financial analysis
│   ├── generate_report.py         # Generate AI-powered reports
│   ├── real_time_dashboard.py     # Real-time dashboard (Streamlit)
│
│── templates/                      # Report templates
│   ├── financial_report_template.txt
│
│── outputs/                        # Generated reports (PDF, HTML, text)
│   ├── reports/                    # Saved AI-generated financial reports
│
│── requirements.txt                # Python dependencies
│── README.md                       # Project documentation
│── config.py                        # Configuration settings
│── app.py                           # Main application script
```

---

## **Installation & Setup**
### **1. Clone the Repository**
```bash
git clone https://github.com/phanideva/gen_ai_financial_report_generator.git
cd financial-report-ai
```

### **2. Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **How to Use the Project**
### **1. Fetch and Preprocess Financial Data**
```bash
python scripts/data_preprocessing.py
```
> Fetches real-time stock market data from **Yahoo Finance** and preprocesses it.

### **2. Perform Financial Analysis**
```bash
python scripts/financial_analysis.py
```
> Analyzes stock trends, computes moving averages, and generates **insights**.

### **3. Generate AI-powered Financial Reports**
```bash
python scripts/generate_report.py
```
> Uses **OpenAI GPT** to generate **AI-based insights** and formats reports in **PDF**.

### **4. Run the Real-time Dashboard**
```bash
streamlit run scripts/real_time_dashboard.py
```
> Launches a **real-time financial dashboard** to visualize stock trends and AI-generated insights.

### **5. Run the Entire Pipeline with One Command**
```bash
python app.py
```
> Automates the entire workflow, from **data collection** to **report generation**.

---

## **Example Output**
- **Stock Trend Analysis Graph** 📊
- **AI-Generated Financial Summary** 📄
- **Automated Financial Report (PDF)** 📑

---

## **Configuration**
Modify **`config.py`** to set API keys and paths:
```python
# OpenAI API Key (Replace with your actual API key)
OPENAI_API_KEY = "your_openai_api_key"

# Paths
DATA_PATH = "data/processed/financial_data.csv"
REPORT_OUTPUT_PATH = "outputs/reports/financial_report.pdf"
```

---

## **Future Enhancements**
✅ **AI-based predictive analytics**  
✅ **Integration with company earnings reports (SEC, financial news)**  
✅ **Real-time stock alerts and notifications**  

---

## **License**
This project is **open-source**.

---

## **Author**
👤 **Phaneendra Devabhakthuni**  
📧 **phanisaisri@gmail.com**  
🔗 **[LinkedIn](https://www.linkedin.com/in/phanideva96/)**  