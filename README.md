# 🌍 Global VAT Monitor

**Enterprise Distance Selling & Nexus Threshold Analytics**

A powerful Streamlit application designed to help businesses monitor VAT compliance across EU markets, track distance selling thresholds, and identify registration requirements.

## 📋 Features

- **Real-time Compliance Monitoring**: Track sales against configurable VAT thresholds
- **Interactive Dashboard**: Visual analytics with Altair charts
- **What-If Scenario Planning**: Adjust thresholds to simulate different regulatory environments
- **Risk Analysis**: Automatic identification of breached and at-risk markets
- **Data Export**: Generate compliance reports for tax filing teams
- **CSV Upload**: Support for custom sales data analysis

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ra[YOUR_USERNAME]/vat-compliance-monitor.git
cd vat-compliance-monitor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📊 Usage

### Demo Mode
- Launch the app without uploading a CSV to see demo data
- Adjust the threshold slider in the sidebar to simulate different scenarios

### Custom Data Analysis
1. Prepare a CSV file with columns: `Country`, `Sales_EUR`, `Transactions`, `Last_Audit`
2. Click "📂 Upload Monthly Sales CSV" 
3. Select your CSV file
4. View compliance analysis and export reports

## 🏗️ Project Structure

```
GLOBAL VAT MONITOR/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore rules
└── runtime.txt           # Python version (for Azure)
```

## 🌐 Deployment

### GitHub
```bash
git add .
git commit -m "Deploy VAT Monitor"
git push origin main
```

### Microsoft Azure

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed Azure deployment instructions.

Quick deploy using Azure Web App:
```bash
az webapp up --name vat-monitor --runtime "PYTHON:3.11" --sku B1
```

## 🔧 Configuration

### Environment Variables (Optional)

Create a `.env` file for custom configurations:
```
THRESHOLD_DEFAULT=10000
DATA_REFRESH_INTERVAL=3600
```

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For questions or issues, please open an issue on GitHub.

---

**Built with ❤️ using Streamlit**
