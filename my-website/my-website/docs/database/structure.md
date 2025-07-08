---
sidebar_position: 1
---

# Database Structure

The DSU API system uses Python's `shelve` module for data persistence, providing a simple key-value storage solution. The system is organized into multiple database files, each handling specific aspects of the application.

## Database Overview

The system uses the following shelve databases located in the `backend/` directory:

- `/people/` - User information and profiles
- `/logins/` - Authentication credentials
- `/grants/` - Grant applications and status
- `/consents/` - User consent forms and preferences
- `/payments/` - Payment form information
- `/uploads/` - Document storage (file system)

## People Database (`/people/`)

### Structure
- **Key**: ID number (string)
- **Value**: Person object

### Person Object Attributes

```python
class Person:
    def __init__(self, id_number, name, dob):
        self.id_number = id_number          # Unique identifier
        self.name = name                    # Full name
        self.dob = dob                      # Date of birth (YYYY-MM-DD)
        self.verified = False               # Verification status
        self.income_bracket = -1            # Income level (1-5, -1 = not set)
        self.age = get_age(dob)             # Calculated age
        self.citizenship_status = False     # Citizenship status
        self.consents = set()               # Set of granted consents
        self.consent_forms = []             # List of consent form IDs
        self.payment = []                   # Payment information
        self.payment_forms = []             # Payment form IDs
        self.current_grants = []            # List of active grants
        self.identifications = []           # Documents uploaded by user
        self.grant_ids = []                 # IDs for each grant in database
        self.file_ids = []                  # IDs of uploaded files
```

### Income Brackets
- **1**: Lowest income level
- **2**: Low income level  
- **3**: Medium income level
- **4**: High income level
- **5**: Highest income level

## Logins Database (`/logins/`)

### Structure
- **Key**: Username (string)
- **Value**: `[id_number, password]`

### Example
```python
{
    "john_doe": ["123456789", "password"],
    "jane_smith": ["987654321", "password"]
}
```

## Grants Database (`/grants/`)

### Structure
- **Key**: Grant ID (string)
- **Value**: Grant application details

### Grant Application Object
```python
{
    'grant': 'Rent Assistance', 
    'submission date': '2025-07-08T08:23:04Z',
    'machine_time': 1751962984.4618962,
    'approved': True|False}
```

## Consents Database (`/consents/`)

### Structure
- **Key**: Form ID (string)
- **Value**: Consent information

### Consent Form Object
```python
{
    'id_number': '65434',
    'consent_given': True,
    'scope': ['See ID'],
    'remove_scope': ['Send photos', 'Use my data to support application'],
    'birthday': '2025-07-08T09:00:38Z'}
```

## Payments Database (`/payments/`)

### Structure
- **Key**: Form ID (string)
- **Value**: Payment details

### Payment Form Object
```python
{
    'id_number': '123',
    'wallet_provider': 'amex',
    'wallet_number': '124',
    'birthday': '2025-07-08T08:41:12Z'
}
```

## Uploads Directory (`/uploads/`)

### Structure
- **Location**: `backend/uploads/`
- **Content**: Physical files (images, documents)
- **File Naming**: Generated unique IDs
- **Supported Formats**: Images (JPG, PNG, etc.)

### File Storage
```python
# Example file structure
uploads/
├── 30.jpg
├── 31.jpg
├── 32.jpg
└── uploads.pkl  # ID for next file name
```

## Data Relationships

### User to Grants
- One user can have multiple grants
- Relationship maintained through `grant_ids` array in Person object
- Grant details stored separately in grants database

### User to Documents
- One user can have multiple documents
- Relationship maintained through `file_ids` array in Person object
- Physical files stored in uploads directory

### User to Consents
- One user can have multiple consent forms
- Relationship maintained through `consent_forms` array in Person object
- Consent details stored separately in consents database

### User to Payments
- One user can have multiple payment methods
- Relationship maintained through `payment_forms` array in Person object
- Payment details stored separately in payments database

## Database Operations

### Reading Data
```python
import shelve

# Open database
with shelve.open('people/people') as db:
    # Check if key exists
    if 'user_id' in db:
        user = db['user_id']
        print(user.name)
```

### Writing Data
```python
import shelve

# Open database
with shelve.open('people/people') as db:
    # Store data
    db['user_id'] = person_object
    
    # Update existing data
    user = db['user_id']
    user.verified = True
    db['user_id'] = user
```

### Deleting Data
```python
import shelve

# Open database
with shelve.open('people/people') as db:
    # Delete key
    if 'user_id' in db:
        del db['user_id']
```

## Backup and Recovery

### Backup Files
Each shelve database creates backup files:
- `.bak` - Backup file
- `.dat` - Data file
- `.dir` - Directory file

### Recovery Process
1. Stop the application
2. Copy backup files to restore directory
3. Restart the application

## Performance Considerations

### Advantages
- Simple setup and maintenance
- No external database server required
- Automatic serialization of Python objects
- Built-in backup mechanism

### Limitations
- Single-threaded access (no concurrent writes)
- Limited query capabilities
- File size grows with data
- No built-in indexing

### Best Practices
- Use separate databases for different data types
- Implement proper error handling
- Regular backup procedures
- Monitor file sizes
- Consider migration to SQLite for larger datasets 