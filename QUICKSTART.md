# 🚀 Quick Start Guide - Deploy to GitHub & Azure

## ✅ Step 1: Push to GitHub

Run these commands in your terminal:

```bash
# Add all new files
git add .

# Commit with a message
git commit -m "feat: Add deployment documentation and configuration files"

# Push to GitHub
git push origin main
```

## ✅ Step 2: Verify on GitHub

1. Open your browser and go to: https://github.com/ra[YOUR_USERNAME]/vat-compliance-monitor
2. You should see all these files:
   - ✅ app.py
   - ✅ requirements.txt
   - ✅ README.md
   - ✅ DEPLOYMENT.md
   - ✅ Dockerfile
   - ✅ runtime.txt
   - ✅ .gitignore
   - ✅ .github/workflows/azure-deploy.yml

## ✅ Step 3: Deploy to Azure (Choose One Option)

### Option A: Deploy via Azure Portal (Easiest - No CLI needed)

1. **Go to Azure Portal**: https://portal.azure.com
2. **Create Web App**:
   - Click "Create a resource"
   - Search for "Web App" and click Create
   - Fill in:
     - **Resource Group**: Create new → `vat-monitor-rg`
     - **Name**: `vat-monitor-[yourname]` (must be unique globally)
     - **Publish**: Code
     - **Runtime stack**: Python 3.11
     - **Operating System**: Linux
     - **Region**: Your closest region
     - **Pricing**: B1 Basic (~$13/month)
   - Click "Review + Create" → "Create"

3. **Connect to GitHub**:
   - After creation, go to your Web App
   - Click "Deployment Center" in the left menu
   - Select **GitHub** as Source
   - Authorize Azure to access GitHub
   - Select:
     - Organization: Your GitHub username
     - Repository: vat-compliance-monitor
     - Branch: main
   - Click "Save"

4. **Configure Streamlit**:
   - Go to "Configuration" → "General settings"
   - Under "Startup Command", enter:
     ```
     python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0 --server.headless=true
     ```
   - Click "Save"

5. **Access Your App**:
   - Wait 3-5 minutes for deployment
   - Your app will be at: `https://vat-monitor-[yourname].azurewebsites.net`

---

### Option B: Deploy via Azure CLI (Faster if you have CLI)

**Prerequisites**: Install Azure CLI first
- Windows: Download from https://aka.ms/installazurecliwindows
- Or use: `winget install -e --id Microsoft.AzureCLI`

**Commands**:

```bash
# 1. Login to Azure
az login

# 2. Create resource group
az group create --name vat-monitor-rg --location eastus

# 3. Create App Service plan
az appservice plan create --name vat-monitor-plan --resource-group vat-monitor-rg --sku B1 --is-linux

# 4. Create Web App
az webapp create --resource-group vat-monitor-rg --plan vat-monitor-plan --name vat-monitor-[yourname] --runtime "PYTHON:3.11"

# 5. Configure GitHub deployment
az webapp deployment source config --name vat-monitor-[yourname] --resource-group vat-monitor-rg --repo-url https://github.com/[YOUR_USERNAME]/vat-compliance-monitor --branch main --manual-integration

# 6. Set startup command
az webapp config set --resource-group vat-monitor-rg --name vat-monitor-[yourname] --startup-file "python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0 --server.headless=true"

# 7. Stream logs (optional - to see deployment progress)
az webapp log tail --name vat-monitor-[yourname] --resource-group vat-monitor-rg
```

---

### Option C: Automated CI/CD with GitHub Actions

**This option automatically deploys whenever you push to GitHub!**

1. **Create Web App** (follow Option A or B above first)

2. **Get Publish Profile**:
   - In Azure Portal, go to your Web App
   - Click "Get publish profile" (download button at top)
   - This downloads a `.PublishSettings` file

3. **Add to GitHub Secrets**:
   - Go to your GitHub repo
   - Click "Settings" → "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Name: `AZURE_WEBAPP_PUBLISH_PROFILE`
   - Value: Paste the entire contents of the `.PublishSettings` file
   - Click "Add secret"

4. **Update Workflow File**:
   - The workflow is already in `.github/workflows/azure-deploy.yml`
   - Edit line 10 and replace `vat-monitor-app` with your actual app name

5. **Push and Deploy**:
   ```bash
   git add .
   git commit -m "feat: Configure GitHub Actions deployment"
   git push origin main
   ```
   
6. **Monitor Deployment**:
   - Go to your GitHub repo → "Actions" tab
   - Watch the deployment progress
   - Once complete, visit your Azure URL!

---

## 🧪 Step 4: Test Your Deployment

After deployment, visit your app URL and verify:
- ✅ App loads without errors
- ✅ Sidebar works with threshold slider
- ✅ Charts display correctly
- ✅ File upload functionality works
- ✅ CSV export works

---

## 🔍 Troubleshooting

### App not loading?

**Check logs**:
```bash
az webapp log tail --name vat-monitor-[yourname] --resource-group vat-monitor-rg
```

**Common fixes**:
1. Verify startup command is set correctly
2. Check that Python 3.11 runtime is selected
3. Ensure requirements.txt is in the root directory
4. Wait 5-10 minutes for first deployment

### Still having issues?

Check the full troubleshooting guide in `DEPLOYMENT.md`

---

## 📞 Need Help?

- **Azure Issues**: Check Azure Portal logs
- **GitHub Issues**: Open an issue in your repository
- **General Questions**: See `DEPLOYMENT.md` for detailed documentation

---

## 🎉 Success Checklist

- [ ] Code pushed to GitHub
- [ ] Azure Web App created
- [ ] GitHub connected to Azure (or CLI deployment complete)
- [ ] Startup command configured
- [ ] App is accessible via Azure URL
- [ ] All features working correctly

---

**Congratulations! Your VAT Monitor is now live! 🚀**
