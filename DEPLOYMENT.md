# DSU API Deployment Guide

This guide explains how to deploy the DSU API with integrated documentation.

## Prerequisites

Before deploying, ensure you have the following installed:

- **Python 3.8+**
- **Node.js 16+**
- **npm** (comes with Node.js)
- **pip** (Python package manager)

## Quick Deployment

### Option 1: Automated Deployment (Recommended)

Use the automated deployment script:

```bash
python deploy.py
```

This script will:
1. Check all dependencies
2. Install Python requirements
3. Build the documentation
4. Start the FastAPI server

### Option 2: Test Before Deployment

Test the documentation setup before deploying:

```bash
python test-docs.py
```

This script will:
1. Check all dependencies
2. Build the documentation
3. Copy to backend
4. Test the server endpoints
5. Verify documentation accessibility

### Option 3: Manual Deployment

If you prefer to deploy manually, follow these steps:

#### Step 1: Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### Step 2: Build Documentation
```bash
cd my-website
npm install
npm run build
cd ..
```

#### Step 3: Copy Documentation to Backend
```bash
python build-docs.py
```

#### Step 4: Start the Server
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Accessing the Application

Once deployed, you can access:

- **API Documentation**: http://localhost:8000/docs
- **API Endpoints**: http://localhost:8000
- **Health Check**: http://localhost:8000/health
- **Uploaded Files**: http://localhost:8000/uploads

## Verifying Documentation Access

### Check Documentation Status
Visit the root endpoint to see if documentation is available:
```bash
curl http://localhost:8000/
```

Expected response:
```json
{
  "message": "DSU API - Digital Services Unit Grant Management System",
  "version": "1.0.0",
  "endpoints": {
    "api": "/",
    "documentation": "/docs",
    "uploads": "/uploads",
    "health": "/health"
  },
  "status": "running"
}
```

### Health Check
Check the health endpoint for documentation status:
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "documentation": "available",
  "timestamp": "2023-01-01T00:00:00Z"
}
```

### Direct Documentation Access
Visit the documentation directly:
- **Documentation**: http://localhost:8000/docs/
- **Documentation Assets**: http://localhost:8000/docs/assets/

## Production Deployment

### Using Render

1. **Connect your repository** to Render
2. **Create a new Web Service**
3. **Configure the build command**:
   ```bash
   pip install -r backend/requirements.txt && cd my-website && npm install && npm run build && cd .. && python build-docs.py
   ```
4. **Configure the start command**:
   ```bash
   cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

### Using Heroku

1. **Create a `Procfile`** in the root directory:
   ```
   web: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

2. **Create a `build.sh`** script:
   ```bash
   #!/bin/bash
   pip install -r backend/requirements.txt
   cd my-website
   npm install
   npm run build
   cd ..
   python build-docs.py
   ```

3. **Deploy using Heroku CLI**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## Environment Variables

For production deployment, consider setting these environment variables:

- `DATABASE_URL`: Database connection string (if using external database)
- `SECRET_KEY`: Secret key for JWT tokens
- `ADMIN_PASSWORD`: Admin password for administrative functions
- `CORS_ORIGINS`: Allowed CORS origins

## File Structure After Deployment

```
dsu-api/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── docs/           # Built documentation (copied from my-website/build)
│   ├── uploads/        # Uploaded files
│   ├── people/         # User database
│   ├── logins/         # Authentication database
│   ├── grants/         # Grant applications database
│   ├── consents/       # Consent forms database
│   └── payments/       # Payment information database
├── my-website/         # Docusaurus documentation source
├── frontend/           # Frontend HTML files
├── build-docs.py       # Documentation build script
├── deploy.py           # Automated deployment script
└── DEPLOYMENT.md       # This file
```

## Troubleshooting

### Common Issues

#### Documentation Not Loading
- Ensure `my-website/build` directory exists
- Check that `backend/docs` directory was created
- Verify the FastAPI server mounted the documentation correctly

#### Build Failures
- Check Node.js and npm versions
- Ensure all dependencies are installed
- Check for any build errors in the console

#### Server Not Starting
- Verify Python dependencies are installed
- Check if port 8000 is available
- Ensure all database directories exist

### Error Messages

#### "Documentation not found"
- Run `python build-docs.py` to build and copy documentation
- Check that the build process completed successfully

#### "Module not found"
- Install Python dependencies: `pip install -r backend/requirements.txt`
- Check that all required packages are in requirements.txt

#### "Permission denied"
- Ensure you have write permissions to the project directory
- On Linux/Mac, you may need to use `sudo` for some operations

## Development vs Production

### Development
- Use `uvicorn main:app --reload` for auto-reload
- Documentation is served from `my-website/build`
- Debug mode enabled

### Production
- Use `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Documentation is copied to `backend/docs`
- Debug mode disabled
- Use proper WSGI server (Gunicorn recommended)

## Security Considerations

- Change default admin password
- Configure CORS properly for production
- Use HTTPS in production
- Implement proper authentication
- Secure file uploads
- Regular database backups

## Monitoring and Maintenance

- Monitor server logs
- Check disk space for uploads
- Regular database maintenance
- Update dependencies regularly
- Monitor API usage and performance 