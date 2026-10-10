---
sidebar_position: 1
---

# API Endpoints Reference

This document provides a complete reference for all API endpoints in the DSU API system.

## Base URL

- **Development**: `http://localhost:8000`
- **Production**: `https://dsu-api.onrender.com`

## Authentication Endpoints

### POST /login
Authenticate a user with username and password.

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "success": true,
  "id": "user_id_number"
}
```

### POST /register
Register a new user account.

**Request Body:**
```json
{
  "id_number": "string",
  "name": "string", 
  "dob": "YYYY-MM-DD",
  "password": "string"
}
```

**Response:**
```json
{
  "success": true,
  "person": {
    "id_number": "string",
    "name": "string",
    "dob": "string",
    "verified": false,
    "income_bracket": -1,
    "age": 25,
    "citizenship_status": false,
    "consents": [],
    "current_grants": [],
    "identifications": [],
    "file_ids": [],
    "payment_forms": [],
    "payment": [],
    "grant_ids": []
  }
}
```

### POST /verify_identity 
Verify user identity with biometric data.

**Request Body:**
```json
{
  "id_number": "string",
  "name": "string",
  "dob": "YYYY-MM-DD"
}
```

**Response:**
```json
{
  "status": "verified|unverified|hidden",
  "biometrics": "match|non-match"
}
```



## User Management Endpoints

### POST /get_user
Retrieve user information by ID.

**Parameters**
- `id`: "654"

**Response:**
```json
{
  "id_number": "string",
  "name": "string",
  "dob": "string",
  "verified": true,
  "income_bracket": 3,
  "age": 25,
  "citizenship_status": true,
  "consents": ["scope1", "scope2"],
  "current_grants": ["grant1", "grant2"],
  "identifications": ["doc1", "doc2"],
  "file_ids": ["file1", "file2"],
  "payment_forms": ["form1"],
  "payment": [{"provider": "string", "number": "string"}],
  "grant_ids": ["grant_id1", "grant_id2"]
}
```

### POST /delete user
Delete a user account.

**Request Body:**
```json
"user_id_string"
```

**Response:**
```json
"user removed"
```

### POST /verify user 

Verify a user account (admin function).

**Request Body:**
```json
"user_id_string"
```

**Response:**
```json
"user verified"
```


### PUT /update_user
Update user profile information.
**Parameters**
- `id`: "654"

**Request Body:**
```json
{
  name: "sillybb",
  income_bracket: "1",
  dob: "2000-02-02",
  age: "25",
  citizenship_status: true
}
```
**Response**

```json
{
  "success":true
}
```
### PUT /set user
Set specific user parameters.

**Parameters:**
- `id`: User ID
- `parameter`: Parameter name
- `value1`: Parameter value (for values with lists, seperate values with commas)

## Grant Management Endpoints

### POST /check_eligibility
Check which grants a user is eligible for.

**parameters**
- `id`: "654"

**Response:**
```json
[
  {
    "name": "Business Grant",
    "requirments": "ID, Business Statement",
    "description": "Apply for a business loan",
    "amount": "50k"
  },
  {
    "name": "Universal Income",
    "requirments": "Bank Statement",
    "description": "Receive Universal Income",
    "amount": "300"
  },
  {
    "name": "Rent Assistance",
    "requirments": "ID",
    "description": "Apply to get assistance for rent",
    "amount": "700"
  },
  {
    "name": "Education Grant",
    "requirments": "ID, Grades, Senior Certificate",
    "description": "Grant to help pay for college",
    "amount": "30k"
  }
]
```

### POST /apply
Apply for a specific grant.

**Parameters:**
- `id`: User ID
- `grant`: Grant name

**Response:**
```json
{
  "success": true,
  "message": "Application submitted successfully|you are missing ID"
}
```

### POST /get grants
Get user's grant applications and status.

**Request Body:**
```json
"user_id_string"
```

**Response:**

```json
{
  "grants": [
    {
      "application id": "30",
      "grant": "Business Grant",
      "admin_approved": "true|false",
      "approved": "2023-01-01T00:00:00Z",
      "nextPayment": "2025-07-15T08:23:04Z",
      "application_status": "true",
      "description": "apply for business loan"
    }
  ]
}
```

### GET /get all requirements
Get all possible grant requirements across all grants.

**Response:**
```json
{
  "requirements": [
    "Proof of Previous Employment",
    "Senior Certificate",
    "Business Statement",
    "Grades",
    "Bank Statement",
    "ID"
  ]
}
```

## Document Management Endpoints

### POST /enter_identification
Upload identification documents.

**Parameters:**
- `id`: User ID
- `identification`: Document type
- `image`: File upload
**Request Body:**
```json
{
"image": "File upload"
}
```
**Response:**
```json
{
  "success": true
}
```

### GET /recieve_docs
Retrieve user documents.

**Parameters:**
- `id`: User ID

**Response:**
```json
{
  "documents": [
    {
      "files":["46.jpg"],
      "docs": ["Bank Statement"]
    }
  ]
}
```

## Consent Management Endpoints

### GET /consent_scopes
Get available consent scopes.

**Response:**
```json
{
  "scope": [
    "Send photos",
    "See ID",
    "Use my data to support application"
  ]
}
```

### GET /get_consent
Get user consent status.

**Parameters:**
- `id`: User ID

**Response:**
```json
{
  "scope": ["scope1", "scope2"]
}
```

### POST /record_consent
Record user consent.

**Request Body:**
```json
{
  "id_number": "65434",
  "consent_given": true,
  "scope": [
    "See ID"
  ],
  "remove_scope": [
    "Send photos",
    "Use my data to support application"
  ]
}
```
**Response:**
```json
{
    "form": {
        "id_number": "123",
        "consent_given": true,
        "scope": [
            "Send photos",
            "Use my data to support application"
        ],
        "remove_scope": [
            "See ID"
        ],
        "birthday": "2025-07-08T08:37:14Z"
    },
    "id": "38"
}
```


### POST /retrieve_consent_form
Get consent form for user.

**Request Body:**
```json
"user_id_string"
```
**Response**
```json
{
  "id_number": "12345",
  "consent_given": true,
  "scope": [
    "Send photos",
    "See ID",
    "Message my business"
  ],
  "remove_scope": [
    "Use my data to support application"
  ],
  "date": "2025-06-26T10:30:55Z"
}
```

## Payment Management Endpoints

### POST /set_payment
Set payment information.

**Request Body:**
```json
{
  "id_number": "string",
  "wallet_provider": "string",
  "wallet_number": "string"
}
```
**Response**
```json
{
  "form": {
    "id_number": "123",
    "wallet_provider": "amex",
    "wallet_number": "124",
    "birthday": "2025-07-08T08:39:41Z"
  },
  "id": "7"
}
```


### POST /retrieve_pay_form
Get payment form for user.

**Request Body:**
```json
"user_id_string"
```
**Response**
```json
{
  "id_number": "123",
  "wallet_provider": "amex",
  "wallet_number": "124",
  "birthday": "2025-07-08T08:41:12Z"
}
```

### GET /get_payment
Get user's payment details.

**Parameters:**
- `ids`: User ID

**Response:**
```json
{
  "payment_info": [
    {
      "provider": "string",
      "number": "string",
      "date_added": "2023-01-01T00:00:00Z"
    }
  ]
}
```

## Administrative Endpoints

### GET /admin/get_all_applications
Get all applications (password protected).

**Parameters:**
- `password`: Admin password

**Response:**
```json
{
    "users": [
        {
            "id_number": "12345",
            "name": "william",
            "dob": "1900-03-04",
            "current_grants": []
        },
        {
            "id_number": "456",
            "name": "Sage A",
            "dob": "2002-03-23",
            "current_grants": [
                {
                    "grant_name": "Universal Income",
                    "grant_id": "27",
                    "grant_details": {
                        "grant": "Universal Income",
                        "submission date": "2025-07-02T14:46:36Z",
                        "machine_time": 1751467596.0790663,
                        "approved": true
                    }
                }
            ]
        },
        {
            "id_number": "123",
            "name": "billy",
            "dob": "2000-02-02",
            "current_grants": [
                {
                    "grant_name": "Rent Assistance",
                    "grant_id": "31",
                    "grant_details": {
                        "grant": "Rent Assistance",
                        "submission date": "2025-07-08T08:23:04Z",
                        "machine_time": 1751962984.4618962,
                        "approved": true
                    }
                }
            ]
        }
    ],
    "approved": true
}
```

### POST /admin/approve_grant
Approve a grant application.

**Request Body:**
```json
{
  "user_id": "456",
  "grant_id": "27"
}
```
**response**
```json
{"success":true,"message":"Grant approved."}
```

### POST /admin/disapprove_grant
Disapprove a grant application.

**Request Body:**
```json
{
  "user_id": "string", 
  "grant_id": "string"
}
```

## Error Responses

All endpoints may return error responses in the following format:

```json
{
  "success": false,
  "error": "Error description"
}
```

Common error scenarios:
- User not found
- Invalid credentials
- Missing required fields
- File upload failures
- Database errors 