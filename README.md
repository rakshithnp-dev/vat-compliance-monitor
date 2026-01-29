# 🇪🇺 Global VAT Compliance Monitor

A regulatory compliance dashboard designed to monitor EU Value Added Tax (VAT) thresholds in real-time. It distinguishes between B2C distance selling rules and B2B reverse charge mechanisms to flag registration risks.

### 🌟 Features

* **Real-time Threshold Tracking:** Monitors sales velocity against the €10,000 EU-wide threshold.
* **B2B Logic Engine:** Automatically applies "Reverse Charge" rules (0% tax) for validated B2B transactions.
* **Geospatial Risk Map:** Interactive choropleth map visualizing exposure across Germany, France, Italy, and Spain.
* **Live Alerts:** Instant "Registration Required" warnings when thresholds are breached.

### 🚀 Live Demo

🔗 **Deployed on Azure:** https://vat-monitor-app-hscga8hjb6bxfhd0.centralindia-01.azurewebsites.net/

### 📋 Prerequisites

* Python 3.10 or higher
* pip (Python package manager)

### 🛠️ Local Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/vat-compliance-monitor.git](https://github.com/YOUR_USERNAME/vat-compliance-monitor.git)
    cd vat-compliance-monitor
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application**
    ```bash
    streamlit run app.py
    ```

### 🎯 Usage

1.  **Upload Data:** Drag and drop the provided `simple_vat.csv` sample file.
2.  **Analyze Risk:** Watch the "VAT Liability" cards update instantly based on the Country Code.
3.  **Visual Inspection:** Hover over the map to see specific sales volumes per jurisdiction.

### 🏗️ Project Structure

```text
vat-monitor/
├── app.py                 # Main Streamlit dashboard logic
├── utils.py               # Helper functions for tax calculations
├── requirements.txt       # Dependencies (pandas, plotly, streamlit)
├── assets/                # Images and sample data
└── README.md              # Documentation
