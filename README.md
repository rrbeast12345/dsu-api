# DSU API - Digital Services Unit Grant Management System

## Project Overview

The DSU API is a web-based system for managing government grant applications. It provides a complete solution for citizens to apply for various grant programs, submit required documents, and track their applications. The system also includes an administrative interface for reviewing and approving applications.

## Architecture

### Backend (FastAPI)
- **Framework**: FastAPI with Python
- **Database**: Python shelve (persistent key-value storage)
- **Authentication**: Simple username/password system
- **File Storage**: Local file system for document uploads
- **API**: RESTful endpoints with CORS support

### Frontend (HTML/CSS/JavaScript)
- **Technology**: Vanilla HTML, CSS, and JavaScript
- **UI Framework**: Custom CSS with responsive design
- **API Integration**: Fetch API for backend communication
- **Authentication**: localStorage for session management

## Installation and Setup

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

## Database Structure

The system uses Python's `shelve` module for data persistence with the following databases:

### `/people/` - User Information
- **Key**: ID number (string)
- **Value**: Person object with attributes:
  - `id_number`: Unique identifier
  - `name`: Full name
  - `dob`: Date of birth
  - `verified`: Verification status
  - `income_bracket`: Income level (1-5)
  - `age`: Calculated age
  - `citizenship_status`: Boolean
  - `current_grants`: List of active grants
  - `consents`: Set of granted consents
  - `payment`: Payment information
  - `identifications`: Document IDs

### `/logins/` - Authentication
- **Key**: Username (string)
- **Value**: `[id_number, password]`

### `/grants/` - Grant Applications
- **Key**: Grant ID (string)
- **Value**: Grant application details

### `/consents/` - User Consents
- **Key**: User ID (string)
- **Value**: Consent information

### `/payments/` - Payment Information
- **Key**: User ID (string)
- **Value**: Payment details

### `/uploads/` - Document Storage
- Directory containing uploaded documents (images)

## Available Grant Programs

The system supports five grant programs:

1. **Business Grant**
   - Income bracket: ≤3
   - Age requirement: ≥18
   - Citizenship required: Yes
   - Amount: $50,000
   - Requirements: ID, Business Statement

2. **Social Security**
   - Income bracket: ≤5
   - Age requirement: ≥65
   - Citizenship required: Yes
   - Amount: $10,000
   - Requirements: ID, Proof of Previous Employment

3. **Universal Income**
   - Income bracket: ≤5
   - Age requirement: ≥18
   - Citizenship required: Yes
   - Amount: $300
   - Requirements: Bank Statement

4. **Rent Assistance**
   - Income bracket: ≤1
   - Age requirement: ≥8
   - Citizenship required: No
   - Amount: $700
   - Requirements: ID

5. **Education Grant**
   - Income bracket: ≤3
   - Age requirement: ≥18
   - Citizenship required: Yes
   - Amount: $30,000
   - Requirements: ID, Grades, Senior Certificate

## API Endpoints

### Authentication
- `POST /login` - User authentication
- `POST /register` - User registration
- `POST /verify_identity` - Identity verification

### User Management
- `POST /get_user` - Retrieve user information
- `POST /delete user` - Delete user account
- `POST /verify user` - Verify user account
- `PUT /update_user` - Update user profile
- `PUT /set user` - Set specific user parameters

### Grant Management
- `POST /check_eligibility` - Check grant eligibility
- `POST /apply` - Apply for a grant
- `POST /get grants` - Get user's grant applications
- `GET /get all requirements` - Get all grant requirements

### Document Management
- `POST /enter_identification` - Upload identification documents
- `GET /recieve_docs` - Retrieve user documents

### Consent Management
- `GET /consent_scopes` - Get available consent scopes
- `GET /get_consent` - Get user consent status
- `POST /record_consent` - Record user consent
- `POST /retrieve_consent_form` - Get consent form

### Payment Management
- `POST /set_payment` - Set payment information
- `POST /retrieve_pay_form` - Get payment form
- `GET /get_payment` - Get payment details

### Admin Endpoints
- `GET /admin/get_all_applications` - Get all applications (password protected)
- `POST /admin/approve_grant` - Approve grant application
- `POST /admin/disapprove_grant` - Disapprove grant application

## Frontend Pages

### User Interface
- **`sign in.html`** - User authentication page
- **`create account.html`** - User registration
- **`profile.html`** - User profile management
- **`grant programs.html`** - View and apply for grants
- **`track grants.html`** - Track application status
- **`add docs.html`** - Document upload interface
- **`consent.html`** - Consent management
- **`payment.html`** - Payment information setup

### Administrative Interface
- **`admin review.html`** - Admin panel for reviewing applications

### Styling
- **`styles.css`** - Main stylesheet
- **`internal styles.css`** - Internal dashboard styling

## Usage Guide

### For Citizens

1. **Account Creation**
   - Visit `create account.html`
   - Provide ID number, name, date of birth, and password
   - Complete identity verification

2. **Profile Setup**
   - Update income bracket and citizenship status
   - Upload required identification documents
   - Set up payment information

3. **Grant Application**
   - Check eligibility on `grant programs.html`
   - Apply for eligible grants
   - Track application status on `track grants.html`

4. **Document Management**
   - Upload supporting documents via `add docs.html`
   - Manage consent preferences

### For Administrators

1. **Access Admin Panel**
   - Navigate to `admin review.html`
   - Enter admin password
   - Review pending applications

2. **Application Review**
   - View all user applications
   - Approve or disapprove grants
   - Monitor application status

## Security Considerations

- **Authentication**: Basic username/password system
- **Data Storage**: Local file system and shelve databases
- **CORS**: Enabled for cross-origin requests
- **Admin Access**: Password-protected admin endpoints

## Development Notes

- The system uses FastAPI for high-performance API development
- Database operations use Python's built-in shelve module
- File uploads are handled through FastAPI's file handling
- Frontend uses vanilla JavaScript for simplicity
- The system is designed for deployment on platforms like Render

## Future Enhancements

Consider implementing:
- JWT-based authentication
- Database migration to PostgreSQL/MySQL
- Enhanced security measures
- Mobile-responsive design improvements
- Real-time notifications
- Document verification automation 