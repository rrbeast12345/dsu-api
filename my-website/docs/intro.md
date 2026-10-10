---
sidebar_position: 1
---

# DSU API - Digital Services Unit Grant Management System

## Project Overview

The DSU API is a web-based demonstration system for managing government grant applications. It provides a complete solution for citizens to apply for various grant programs, submit required documents, and track their applications. The system also includes an administrative interface for reviewing and approving applications.

## Architecture

### Backend (FastAPI)
- **Framework**: FastAPI with Python
- **Database**: Python shelve (persistent key-value storage)
- **Authentication**: Simple username/password system
- **File Storage**: Local file system for document uploads
- **API**: RESTful endpoints

### Frontend (HTML/CSS/JavaScript)
- **Technology**: Vanilla HTML, CSS, and JavaScript
- **UI Framework**: Custom CSS with responsive design
- **API Integration**: Fetch API for backend communication
- **Authentication**: localStorage for session management

## Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Backend Setup

1. **Install Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Run the Server**
   ```bash
   uvicorn main:app --reload
   ```
   
   The API will be available at `http://localhost:8000`

3. **Production Deployment**
   The current configuration points to `https://dsu-api.onrender.com` for production

### Frontend Setup

The frontend files are located in `backend/frontend for replit/` and can be served statically or through the FastAPI server.
For running locally, use the files in the `frontend` folder.

## Available Grant Programs

The system supports five grant programs:

1. **Business Grant** - $50,000 for business development
2. **Social Security** - $10,000 for seniors (65+)
3. **Universal Income** - $300 monthly support
4. **Rent Assistance** - $700 for housing support
5. **Education Grant** - $30,000 for educational expenses

## Next Steps

- [API Endpoints](/docs/api/endpoints) - Complete API reference
- [Database Structure](/docs/database/structure) - Data models and storage
- [Frontend Pages](/docs/frontend/pages) - User interface documentation
- [Security Considerations](/docs/security/overview) - Security and best practices
