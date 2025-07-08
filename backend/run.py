#!/usr/bin/env python3
"""
Simple startup script for the FastAPI server
"""
import uvicorn
import os
from main import app

if __name__ == "__main__":
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get("PORT", 8000))
    
    # Only use reload in development
    reload = os.environ.get("ENVIRONMENT", "production") == "development"
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=reload,
        log_level="info"
    ) 