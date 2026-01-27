# ✅ Azure Deployment Requirements Checklist

## 📋 Pre-Deployment Requirements

### 1. GitHub Requirements
- [x] Git repository initialized
- [x] Remote repository connected to GitHub
- [x] README.md created
- [x] .gitignore configured
- [ ] All code committed and pushed to GitHub
- [ ] Repository is accessible (public or private with Azure access)

### 2. Application Requirements
- [x] `app.py` - Main Streamlit application
- [x] `requirements.txt` - Python dependencies (streamlit, pandas, altair)
- [x] `runtime.txt` - Python version specification (python-3.11)
- [x] `.gitignore` - Excludes unnecessary files
- [x] `Dockerfile` - For container deployments (optional)

### 3. Azure Requirements

#### Account & Billing
- [ ] Azure account created (https://azure.microsoft.com)
- [ ] Valid payment method added
- [ ] Subscription activated (Free tier available for 12 months)
- [ ] Resource group created or planned

#### Access & Tools
- [ ] **Option A**: Access to Azure Portal (browser-based)
  - No installation needed
  - Web interface at https://portal.azure.com
  
- [ ] **Option B**: Azure CLI installed (for command-line deployment)
  - Windows: Download from https://aka.ms/installazurecliwindows
  - Verify: Run `az --version`
  - Login: Run `az login`

### 4. Configuration Requirements

#### Required Settings for Azure App Service
- [ ] App name decided (must be globally unique)
  - Example: `vat-monitor-yourcompany`
  - Will create URL: `https://vat-monitor-yourcompany.azurewebsites.net`
  
- [ ] Region selected
  - Recommended: 
    - US: East US, West US 2
    - Europe: West Europe, North Europe
    - Asia: Southeast Asia, East Asia
  
- [ ] Pricing tier planned
  - **Free (F1)**: $0/month - Basic testing, auto-sleeps, limited resources
  - **Basic (B1)**: ~$13/month - Production-ready, always on, 1.75GB RAM
  - **Standard (S1)**: ~$70/month - Auto-scaling, staging slots, 1.75GB RAM
  - **Recommended**: Start with B1, scale as needed

#### Startup Command
The following command must be configured in Azure:
```bash
python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0 --server.headless=true
```

### 5. Network & Security Requirements
- [ ] HTTPS enabled (automatic on Azure)
- [ ] Firewall rules configured (if needed)
- [ ] CORS settings (if connecting to external APIs)
- [ ] Environment variables/secrets defined (if any)

### 6. Performance & Monitoring
- [ ] Plan decided: How much traffic do you expect?
  - Low (<100 users/day): Free or B1 tier
  - Medium (100-1000 users/day): B1 or S1 tier
  - High (>1000 users/day): S1+ with auto-scaling

- [ ] Monitoring enabled (optional but recommended)
  - Application Insights
  - Log Analytics
  - Alerts configured

---

## 🔧 Technical Specifications

### Current Application Stack
| Component | Technology | Version |
|-----------|-----------|---------|
| Language | Python | 3.11 |
| Framework | Streamlit | Latest |
| Data Processing | Pandas | Latest |
| Visualization | Altair | Latest |
| Server | Gunicorn/Streamlit | Built-in |

### Azure App Service Specifications
| Resource | Free Tier | Basic (B1) | Standard (S1) |
|----------|-----------|------------|---------------|
| vCPU | Shared | 1 | 1 |
| RAM | 1 GB | 1.75 GB | 1.75 GB |
| Storage | 1 GB | 10 GB | 50 GB |
| Auto-scale | ❌ | ❌ | ✅ |
| Custom domain | ❌ | ✅ | ✅ |
| SSL | Free (Let's Encrypt) | Free | Free |
| Deployment slots | ❌ | ❌ | ✅ (5 slots) |
| Monthly cost | $0 | ~$13 | ~$70 |

---

## 🚀 Deployment Methods Comparison

### Method 1: Azure Portal + GitHub (Recommended for beginners)
**Pros:**
- ✅ No command-line knowledge needed
- ✅ Visual interface
- ✅ Easy GitHub integration
- ✅ Built-in CI/CD

**Cons:**
- ❌ Slower for repeated deployments
- ❌ Less control over advanced settings

**Time to deploy**: 10-15 minutes

---

### Method 2: Azure CLI (Recommended for developers)
**Pros:**
- ✅ Fast deployment
- ✅ Scriptable and repeatable
- ✅ Full control
- ✅ Can be automated

**Cons:**
- ❌ Requires CLI installation
- ❌ Learning curve for Azure commands

**Time to deploy**: 5-10 minutes

---

### Method 3: GitHub Actions (Recommended for teams)
**Pros:**
- ✅ Fully automated
- ✅ Deploy on every push
- ✅ Version controlled
- ✅ Professional workflow

**Cons:**
- ❌ Requires initial setup
- ❌ Needs publish profile secret

**Time to deploy**: 15 minutes (setup) + 5 minutes (each deployment)

---

### Method 4: Docker + Container Instances
**Pros:**
- ✅ Consistent environment
- ✅ Works anywhere
- ✅ Easy to scale

**Cons:**
- ❌ Requires Docker knowledge
- ❌ More complex setup
- ❌ Higher cost for similar resources

**Time to deploy**: 20-30 minutes

---

## 📊 Resource Requirements Check

### Minimum Requirements (Your App)
- **Storage**: ~50 MB (the app itself)
- **RAM**: ~200-500 MB (Streamlit + Pandas + Your app)
- **CPU**: Minimal (unless processing large CSV files)

### Recommended Azure Configuration
- **Tier**: B1 Basic
- **Scaling**: Manual initially, auto-scaling if traffic grows
- **Region**: Closest to your users

---

## 🔍 Pre-Flight Checklist

Before clicking "Deploy", verify:

1. **Code Quality**
   - [ ] App runs locally without errors
   - [ ] All dependencies in requirements.txt
   - [ ] No hardcoded sensitive data (API keys, passwords)
   - [ ] CSV upload/download tested locally

2. **Git Repository**
   - [ ] Latest code committed
   - [ ] Pushed to GitHub
   - [ ] No large files (>100MB) in repo

3. **Azure Setup**
   - [ ] Account created and verified
   - [ ] Payment method added (even for free tier)
   - [ ] Subscription active

4. **Documentation**
   - [ ] README.md complete
   - [ ] DEPLOYMENT.md reviewed
   - [ ] QUICKSTART.md understood

---

## 🎯 Post-Deployment Testing

After deployment, test these features:

### Functional Tests
- [ ] Homepage loads
- [ ] Sidebar configuration works
- [ ] Threshold slider updates dashboard
- [ ] Demo data displays correctly
- [ ] Charts render (bar chart, donut chart)
- [ ] CSV file upload works
- [ ] CSV export/download works
- [ ] All tabs accessible (Dashboard, Report, Export)

### Performance Tests
- [ ] Page loads in <5 seconds
- [ ] No console errors (F12 developer tools)
- [ ] Mobile responsive (if needed)

### Security Tests
- [ ] HTTPS enabled (check for 🔒 in browser)
- [ ] No sensitive data exposed
- [ ] Environment variables working (if any)

---

## 💰 Cost Estimation

### Development/Testing Phase
- **Free tier**: $0/month (limited, sleeps after inactivity)
- **B1 Basic**: ~$13/month (recommended)

### Production Phase
- **B1 Basic**: ~$13/month (low traffic, <100 users/day)
- **S1 Standard**: ~$70/month (medium traffic, auto-scaling)
- **P1V2 Premium**: ~$160/month (high traffic, enterprise)

### Additional Costs (Optional)
- **Custom domain**: Free (you own the domain) or ~$12/year
- **Application Insights**: Free tier available, ~$2.88/GB after
- **Storage**: Included in plan
- **Bandwidth**: First 100GB free, then ~$0.05/GB

**Recommendation**: Start with B1 Basic ($13/month) for testing and production

---

## 🔐 Security Checklist

- [ ] HTTPS enabled (automatic)
- [ ] Authentication configured (if needed)
  - Azure AD
  - Custom auth
- [ ] API keys stored in Azure App Settings (not in code)
- [ ] CORS configured (if calling from other domains)
- [ ] IP restrictions (if needed for internal apps)
- [ ] Managed Identity enabled (for accessing Azure resources)

---

## 📞 Support Resources

### If you need help:

1. **Azure Documentation**
   - App Service: https://docs.microsoft.com/azure/app-service/
   - Python on Azure: https://docs.microsoft.com/azure/developer/python/

2. **Streamlit Documentation**
   - Deployment: https://docs.streamlit.io/deploy
   - Configuration: https://docs.streamlit.io/library/advanced-features/configuration

3. **Community Support**
   - Azure Forums: https://learn.microsoft.com/answers/
   - Stack Overflow: Tag with `azure-app-service` and `streamlit`

4. **Official Support**
   - Azure Support: Portal → "Help + support"
   - Free tier includes billing support

---

## ✅ Final Checklist Before Deployment

Review this list one final time:

### GitHub
- [ ] All files committed
- [ ] Pushed to main branch
- [ ] Repository accessible

### Files Present
- [ ] app.py
- [ ] requirements.txt
- [ ] runtime.txt
- [ ] README.md
- [ ] .gitignore
- [ ] Dockerfile (optional)

### Azure Preparation
- [ ] Account ready
- [ ] Subscription active
- [ ] App name decided
- [ ] Pricing tier selected
- [ ] Region selected

### Configuration
- [ ] Startup command noted
- [ ] Environment variables listed (if any)
- [ ] Secrets prepared (if any)

---

## 🎉 You're Ready!

All requirements are met! Proceed to `QUICKSTART.md` for deployment steps.

**Estimated total time**: 15-30 minutes for first deployment

**Good luck! 🚀**
