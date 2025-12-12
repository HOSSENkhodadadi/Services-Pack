# 🚀 Vercel Deployment Guide

Your Django backend is now configured for Vercel deployment!

## ✅ What Was Configured

1. **vercel.json** - Deployment configuration for Vercel
2. **build_files.sh** - Build script to collect static files
3. **settings.py** - Updated for production (static files, CORS)
4. **wsgi.py** - Already configured with `app` variable for Vercel
5. **.gitignore** - Excludes build artifacts

## 📋 Deployment Steps

### Option 1: Deploy via Vercel CLI (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Navigate to backend folder:**
   ```bash
   cd backend
   ```

3. **Deploy:**
   ```bash
   vercel
   ```
   
   Follow the prompts:
   - Set up and deploy? **Y**
   - Which scope? Select your account
   - Link to existing project? **N**
   - What's your project's name? **services-pack-backend**
   - In which directory is your code located? **.**
   - Want to override settings? **N**

4. **Deploy to production:**
   ```bash
   vercel --prod
   ```

### Option 2: Deploy via Vercel Dashboard

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Configure for Vercel deployment"
   git push
   ```

2. **Import to Vercel:**
   - Go to https://vercel.com/new
   - Import your GitHub repository
   - **Important:** Set **Root Directory** to `backend`
   - Click "Deploy"

## ⚙️ Environment Variables

After deployment, add these environment variables in Vercel Dashboard:

1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add:
   - `SECRET_KEY` = Generate a new secret key (don't use the default!)
   - `DEBUG` = `False`

To generate a secure secret key:
```python
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## 🗄️ Database Configuration

**Important:** Vercel doesn't support SQLite in production!

### Quick Solution: Vercel Postgres (Recommended)

1. In your Vercel project dashboard, go to "Storage"
2. Create a new Postgres database
3. Vercel will automatically add the database URL to your environment variables
4. Update your `settings.py` to use the database URL:

```python
import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

5. Add to `requirements.txt`:
```
dj-database-url
psycopg2-binary
```

### Alternative Solutions:

- **Supabase:** Free PostgreSQL database - https://supabase.com
- **Railway:** Free tier with PostgreSQL - https://railway.app
- **Neon:** Serverless PostgreSQL - https://neon.tech

## 🌐 Frontend Deployment

Your frontend needs to be deployed separately. Two options:

### Option A: Deploy Frontend to Vercel

1. Create a new Vercel project for the `frontend` folder
2. Update `chatbot.js` with your backend URL:

```javascript
const API_URL = 'https://your-backend.vercel.app/api/chatbot/';
```

### Option B: Use the frontend from Django (current setup)

The frontend is currently served by Django, which works but isn't optimal for Vercel.

## 🔧 Post-Deployment Configuration

1. **Update CORS settings:**
   
   In `settings.py`, add your frontend URL:
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://your-frontend.vercel.app",
   ]
   
   # Remove this in production:
   # CORS_ALLOW_ALL_ORIGINS = True
   ```

2. **Update ALLOWED_HOSTS:**
   ```python
   ALLOWED_HOSTS = [
       '.vercel.app',
       'your-custom-domain.com',  # if you have one
   ]
   ```

3. **Set DEBUG to False in production:**
   Add environment variable: `DEBUG=False`

## 🧪 Testing Your Deployment

After deployment, test these URLs:

- `https://your-app.vercel.app/` - Homepage
- `https://your-app.vercel.app/api/health/` - Health check
- `https://your-app.vercel.app/chatbot.html` - Chatbot page
- `https://your-app.vercel.app/admin/` - Admin panel

## 🐛 Common Issues & Solutions

### Issue: "Application Error" or 500 errors

**Solution:** Check Vercel logs
- Go to your project → Deployments → Click on deployment → View Function Logs
- Look for Python errors

### Issue: Static files not loading (CSS/JS missing)

**Solution:** 
```bash
# Run locally to test
python manage.py collectstatic --noinput

# Verify staticfiles_build/static folder is created
```

### Issue: CORS errors in browser

**Solution:** Update CORS settings in settings.py
```python
CORS_ALLOW_ALL_ORIGINS = True  # Temporary for testing
```

### Issue: Database errors

**Solution:** SQLite doesn't work on Vercel. Set up PostgreSQL (see Database Configuration above)

### Issue: Groq API key not working

**Solution:** Add as environment variable in Vercel:
- Go to Settings → Environment Variables
- Add: `GROQ_API_KEY` = your-api-key
- Update code to use: `os.environ.get('GROQ_API_KEY')`

## 📝 Checklist Before Deploying

- [ ] All changes committed to Git
- [ ] `build_files.sh` is executable (`chmod +x build_files.sh`)
- [ ] `requirements.txt` includes all dependencies
- [ ] Secret key will be changed in production
- [ ] Database plan decided (Vercel Postgres, Supabase, etc.)
- [ ] API keys will be added as environment variables

## 🎉 After Successful Deployment

1. **Test all features:**
   - Homepage loads
   - Chatbot works
   - API endpoints respond
   - Static files load

2. **Update frontend API URL** (if deploying frontend separately)

3. **Set up custom domain** (optional):
   - Go to Project Settings → Domains
   - Add your domain

4. **Monitor logs:**
   - Check Vercel dashboard for errors
   - Set up error tracking (Sentry, etc.)

## 📚 Additional Resources

- Vercel Python Documentation: https://vercel.com/docs/frameworks/python
- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- Vercel Environment Variables: https://vercel.com/docs/projects/environment-variables

---

**Need help?** Check the Vercel logs or raise an issue!

Good luck with your deployment! 🚀
