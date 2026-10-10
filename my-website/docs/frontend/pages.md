---
sidebar_position: 1
---

# Frontend Pages

The DSU API frontend consists of HTML pages with vanilla JavaScript and CSS, providing a complete user interface for the grant management system.

## Technology Stack

- **HTML5**: Semantic markup and structure
- **CSS3**: Custom styling with responsive design
- **Vanilla JavaScript**: Client-side functionality and API integration
- **Fetch API**: Backend communication
- **localStorage**: Session management

## Page Structure

### User Interface Pages

#### 1. Sign In (`sign in.html`)
**Purpose**: User authentication and login

**Features**:
- Username and password input
- Form validation
- Error handling and display
- Redirect to profile page on successful login

**Key Elements**:
- Login form with validation
- Error message display
- Responsive design for mobile devices

#### 2. Create Account (`create account.html`)
**Purpose**: New user registration

**Features**:
- ID number, name, date of birth, and password input
- Form validation
- Duplicate username checking
- Automatic redirect to profile setup

**Key Elements**:
- Registration form with required fields
- Date picker for date of birth
- Password strength indicators
- Success/error message handling

#### 3. Profile (`profile.html`)
**Purpose**: User profile management and setup

**Features**:
- Display user information
- Update income bracket, citizenship status and date of birth
- Profile completion status
- Navigation to other sections

**Key Elements**:
- Profile information display
- Editable fields for grant eligibility
- Progress indicators
- Navigation menu

#### 4. Grant Programs (`grant programs.html`)
**Purpose**: View and apply for available grants

**Features**:
- Display eligible grants based on user profile
- Grant details and requirements
- Application submission
- Real-time eligibility checking

**Key Elements**:
- Dynamic grant listing
- Grant cards with details
- Apply buttons with confirmation
- Requirements display

#### 5. Track Grants (`track grants.html`)
**Purpose**: Monitor application status

**Features**:
- List all user's grant applications
- Application status (pending/approved)
- Application dates
- Status updates

**Key Elements**:
- Application status cards
- Color-coded status indicators
- Application history
- Real-time status updates

#### 6. Add Documents (`add docs.html`)
**Purpose**: Document upload interface

**Features**:
- File upload for identification documents
- Multiple document type support
- Upload progress indicators
- Document management

**Key Elements**:
- File input with drag-and-drop
- Document type selection
- Upload progress bar
- Document preview

#### 7. Consent Management (`consent.html`)
**Purpose**: Manage user consent preferences

**Features**:
- Display available consent scopes
- Consent form management
- Consent history
- Consent withdrawal

**Key Elements**:
- Consent scope checkboxes
- Consent form display
- Consent history table
- Consent management controls

#### 8. Payment Setup (`payment.html`)
**Purpose**: Configure payment information

**Features**:
- Payment method setup
- Wallet provider selection
- Account number input
- Payment form management

**Key Elements**:
- Payment form inputs
- Provider selection dropdown
- Account validation
- Payment history display

### Administrative Interface

#### 9. Admin Review (`admin review.html`)
**Purpose**: Administrative panel for application review

**Features**:
- View all applications
- Approve/disapprove grants
- User verification
- Application filtering

**Key Elements**:
- Application listing table
- Action buttons for approval/rejection
- User search and filtering
- Admin authentication

## Styling

### CSS Files

#### `styles.css`
**Purpose**: Main stylesheet for authentication pages

**Features**:
- Login and registration form styling
- Button and input styling
- Responsive design
- Error message styling

#### `internal styles.css`
**Purpose**: Internal dashboard styling

**Features**:
- Dashboard layout and navigation
- Card and table styling
- Status indicators
- Mobile-responsive design

## JavaScript Functionality

### API Integration
```javascript
// Example API call
async function loginUser(username, password) {
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Login error:', error);
        return { success: false, error: 'Network error' };
    }
}
```

### Session Management
```javascript
// Store user session
function setUserSession(userId) {
    localStorage.setItem('userId', userId);
    localStorage.setItem('sessionStart', Date.now());
}

// Check session validity
function isSessionValid() {
    const sessionStart = localStorage.getItem('sessionStart');
    const sessionDuration = 24 * 60 * 60 * 1000; // 24 hours
    return sessionStart && (Date.now() - sessionStart < sessionDuration);
}
```

### Form Validation
```javascript
// Validate registration form
function validateRegistration(formData) {
    const errors = [];
    
    if (!formData.id_number || formData.id_number.length < 5) {
        errors.push('ID number must be at least 5 characters');
    }
    
    if (!formData.name || formData.name.length < 2) {
        errors.push('Name must be at least 2 characters');
    }
    
    if (!isValidDate(formData.dob)) {
        errors.push('Please enter a valid date of birth');
    }
    
    return errors;
}
```

## Responsive Design

### Mobile-First Approach
- CSS Grid and Flexbox for layouts
- Media queries for different screen sizes
- Touch-friendly button sizes
- Optimized form inputs for mobile

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## User Experience Features

### Loading States
- Spinner animations during API calls
- Disabled buttons during form submission
- Progress indicators for file uploads

### Error Handling
- User-friendly error messages
- Form validation feedback
- Network error recovery
- Session timeout handling

### Navigation
- Breadcrumb navigation
- Consistent header and footer
- Quick access to common functions
- Back button functionality

## File Structure

```
frontend/
├── sign in.html
├── create account.html
├── profile.html
├── grant programs.html
├── track grants.html
├── add docs.html
├── consent.html
├── payment.html
├── admin review.html
├── styles.css
└── internal styles.css
```

## Browser Compatibility

### Supported Browsers
- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

### Required Features
- ES6+ JavaScript support
- Fetch API
- localStorage
- File API
- FormData API

## Performance Considerations

### Optimization Techniques
- Minified CSS and JavaScript
- Optimized images
- Lazy loading for large lists
- Efficient DOM manipulation

### Caching Strategy
- Browser caching for static assets
- localStorage for session data
- API response caching where appropriate

## Security Features

### Client-Side Security
- Input sanitization
- XSS prevention
- CSRF token handling
- Secure session management

### Data Protection
- No sensitive data in localStorage
- Secure API communication
- Input validation
- Error message sanitization 