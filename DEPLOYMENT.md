# 🚀 Deployment Guide - Global VAT Monitor

This guide covers deploying the Global VAT Monitor to GitHub and Microsoft Azure.

---

## 📦 Part 1: GitHub Deployment

### Step 1: Verify Your Git Repository

Check if you're connected to GitHub:
```bash
git remote -v
```

You should see your GitHub repository URL.

### Step 2: Commit All Changes

1. Check the status:
```bash
git status
```

2. Add all files:
```bash
git add .
```

3. Commit your changes:
```bash
git commit -m "feat: Complete VAT Monitor application with documentation"
```

4. Push to GitHub:
```bash
git push origin main
```

### Step 3: Verify on GitHub

1. Go to your GitHub repository in a browser
2. Verify all files are uploaded:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `DEPLOYMENT.md`
   - `.gitignore`
   - `runtime.txt`

---

## ☁️ Part 2: Microsoft Azure Deployment

### Prerequisites

Before deploying to Azure, ensure you have:

1. **Azure Account**: Create one at [azure.microsoft.com](https://azure.microsoft.com)
2. **Azure CLI**: Install from [docs.microsoft.com/cli/azure/install-azure-cli](https://docs.microsoft.com/cli/azure/install-azure-cli)

### Deployment Options

There are **3 main ways** to deploy to Azure:

---

### ✅ **Option 1: Azure App Service (Recommended for Streamlit)**

#### Method A: Deploy from GitHub (Easiest)

1. **Login to Azure Portal**
   - Go to [portal.azure.com](https://portal.azure.com)

2. **Create a Web App**
   - Click "Create a resource" → "Web App"
   - Fill in the details:
     - **Resource Group**: Create new (e.g., `vat-monitor-rg`)
     - **Name**: `vat-monitor-app` (must be globally unique)
     - **Publish**: Code
     - **Runtime stack**: Python 3.11
     - **Region**: Choose closest to you
     - **Pricing Plan**: B1 (Basic) - ~$13/month

3. **Configure Deployment**
   - In the new Web App, go to "Deployment Center"
   - Choose **GitHub** as the source
   - Authorize Azure to access your GitHub
   - Select your repository and branch (main)
   - Save

4. **Configure Startup Command**
   - Go to "Configuration" → "General settings"
   - Set **Startup Command** to:
     ```bash
     python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0
     ```

5. **Access Your App**
   - Your app will be available at: `https://vat-monitor-app.azurewebsites.net`

#### Method B: Deploy using Azure CLI

```bash
# Login to Azure
az login

# Create a resource group
az group create --name vat-monitor-rg --location eastus

# Create an App Service plan
az appservice plan create --name vat-monitor-plan --resource-group vat-monitor-rg --sku B1 --is-linux

# Create a Web App
az webapp create --resource-group vat-monitor-rg --plan vat-monitor-plan --name vat-monitor-app --runtime "PYTHON:3.11"

# Deploy from local Git
az webapp deployment source config-local-git --name vat-monitor-app --resource-group vat-monitor-rg

# Configure Streamlit startup
az webapp config set --resource-group vat-monitor-rg --name vat-monitor-app --startup-file "python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0"

# Deploy your code (add Azure as Git remote and push)
git remote add azure <DEPLOYMENT_URL_FROM_PREVIOUS_COMMAND>
git push azure main
```

---

### ✅ **Option 2: Azure Container Instances**

1. **Create a Dockerfile** (already provided in this guide)
2. **Build and deploy**:
```bash
az login
az group create --name vat-monitor-rg --location eastus

# Build and deploy container
az container create \
  --resource-group vat-monitor-rg \
  --name vat-monitor-container \
  --image <YOUR_DOCKER_IMAGE> \
  --dns-name-label vat-monitor \
  --ports 8501
```

---

### ✅ **Option 3: Azure Static Web Apps + Backend API**

For a more scalable architecture, you can:
1. Convert Streamlit to a FastAPI backend
2. Create a React/Next.js frontend
3. Deploy using Azure Static Web Apps

*(This is more complex and suitable for production-grade applications)*

---

## 🐳 Docker Deployment (For Container-based options)

If you choose Container Instances or AKS, you'll need a Dockerfile.

**Dockerfile** (create this file):
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and test locally:
```bash
docker build -t vat-monitor .
docker run -p 8501:8501 vat-monitor
```

---

## 🔒 Environment Variables & Secrets

### For Azure App Service:

1. Go to your Web App in Azure Portal
2. Navigate to "Configuration" → "Application settings"
3. Add new application settings:
   - `THRESHOLD_DEFAULT=10000`
   - Any API keys or secrets

### For Streamlit Secrets:

Create `.streamlit/secrets.toml` (excluded from Git):
```toml
[api]
key = "your-api-key"
```

In Azure, add these as environment variables.

---

## 📊 Monitoring & Scaling

### Enable Application Insights

1. In Azure Portal, go to your Web App
2. Click "Application Insights" → "Turn on"
3. Monitor:
   - Performance metrics
   - Error logs
   - User analytics

### Auto-scaling

1. Go to "Scale out (App Service plan)"
2. Configure rules based on:
   - CPU percentage
   - Memory usage
   - Request count

---

## 🔧 Troubleshooting

### Common Issues:

**1. App not starting:**
- Check logs: `az webapp log tail --name vat-monitor-app --resource-group vat-monitor-rg`
- Verify startup command is correct

**2. Module not found:**
- Ensure `requirements.txt` is properly formatted and deployed

**3. Port binding errors:**
- Streamlit must listen on port 8000 (or the port Azure assigns via `$PORT` env variable)
- Update startup command if needed

### View Logs:

```bash
# Stream logs
az webapp log tail --name vat-monitor-app --resource-group vat-monitor-rg

# Download logs
az webapp log download --name vat-monitor-app --resource-group vat-monitor-rg
```

---

## 💰 Cost Estimation

### Azure Pricing (Approximate):

| Service | Tier | Monthly Cost |
|---------|------|--------------|
| App Service | B1 (Basic) | ~$13 |
| App Service | S1 (Standard) | ~$70 |
| Container Instances | 1 vCPU, 1.5GB | ~$30 |
| Static Web Apps | Free tier | $0 |

**Recommendation**: Start with B1 App Service for testing, then scale as needed.

---

## 🎯 Best Practices

1. **Use GitHub Actions** for CI/CD
2. **Enable HTTPS** (automatically enabled on Azure)
3. **Set up custom domain** (optional)
4. **Configure backup** for production
5. **Use slots** for staging/production deployments

---

## 📞 Next Steps

After deployment:

1. ✅ Test the application thoroughly
2. ✅ Configure custom domain (optional)
3. ✅ Set up monitoring and alerts
4. ✅ Enable auto-scaling if needed
5. ✅ Configure SSL certificate (auto-handled by Azure for .azurewebsites.net)

---

## 🔗 Useful Resources

- [Azure App Service Python Documentation](https://docs.microsoft.com/azure/app-service/quickstart-python)
- [Streamlit Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud/get-started)
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/)

---

**Need Help?** Open an issue on GitHub or contact Azure Support.
