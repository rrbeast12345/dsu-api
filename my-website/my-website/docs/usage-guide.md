---
sidebar_position: 2
---

# Usage Guide

This guide provides step-by-step instructions for using the DSU API system, both for citizens applying for grants and administrators managing applications.

## For Citizens

### 1. Account Creation

#### Step 1: Access Registration Page
- Navigate to `create account.html`
- Ensure you have your ID number ready

#### Step 2: Complete Registration Form
- **ID Number**: Enter your government-issued ID number (minimum 5 digits)
- **Full Name**: Enter your complete legal name
- **Date of Birth**: Select your date of birth using the date picker
- **Password**: Create a strong password (minimum 8 characters)

#### Step 3: Submit Registration
- Click "Create Account" button
- If successful, you'll be redirected to the profile page
- If username already exists, you'll need to choose a different name

### 2. Profile Setup

#### Step 1: Complete Profile Information
- **Income Bracket**: Select your income level (1-5)
  - 1: Lowest income level
  - 2: Low income level
  - 3: Medium income level
  - 4: High income level
  - 5: Highest income level

- **Citizenship Status**: Indicate if you are a citizen
- **Age**: Automatically calculated from date of birth

#### Step 2: Save Profile
- Click "Update Profile" to save changes
- Profile completion is required for grant eligibility

### 3. Document Upload

#### Step 1: Access Document Upload
- Navigate to `add docs.html`
- Ensure you have digital copies of required documents

#### Step 2: Upload Documents
- **Document Type**: Select the type of document (ID, Business Statement, etc.)
- **File Selection**: Choose the file from your device
- **Upload**: Click "Upload Document" button

#### Supported Document Types:
- **ID**: Government-issued identification
- **Business Statement**: Business registration or plan
- **Proof of Previous Employment**: Employment history
- **Bank Statement**: Financial institution statement
- **Grades**: Academic transcripts
- **Senior Certificate**: High school completion certificate

### 4. Grant Application

#### Step 1: Check Eligibility
- Navigate to `grant programs.html`
- System automatically checks your eligibility based on profile
- Only eligible grants will be displayed

#### Step 2: Review Grant Details
Each grant shows:
- **Grant Name**: Type of grant
- **Amount**: Grant value
- **Requirements**: Documents needed
- **Description**: Purpose and details

#### Step 3: Apply for Grants
- Click "Apply" button for desired grants
- Confirm application submission
- Multiple grants can be applied for simultaneously

### 5. Track Applications

#### Step 1: Monitor Status
- Navigate to `track grants.html`
- View all your applications and their current status

#### Status Types:
- **Pending**: Application under review
- **Approved**: Grant approved and processing
- **Disapproved**: Application rejected

#### Step 2: Check Details
- Click on applications to view details
- Monitor for status updates

### 6. Consent Management

#### Step 1: Access Consent Page
- Navigate to `consent.html`
- Review available consent scopes

#### Step 2: Manage Consents
- **Data Sharing**: Consent to share data with government agencies
- **Marketing Communications**: Receive promotional materials
- **Third Party Access**: Allow third-party service providers

#### Step 3: Update Preferences
- Check/uncheck consent options
- Click "Update Consents" to save changes

### 7. Payment Setup

#### Step 1: Access Payment Page
- Navigate to `payment.html`
- Prepare your payment method information

#### Step 2: Add Payment Method
- **Wallet Provider**: Select your payment provider
- **Account Number**: Enter your account/wallet number
- **Save**: Click "Add Payment Method"

#### Step 3: Manage Payment Methods
- View existing payment methods
- Add multiple payment options
- Remove outdated payment methods

## For Administrators

### 1. Access Admin Panel

#### Step 1: Navigate to Admin Page
- Access `admin review.html`
- Enter admin password when prompted

#### Step 2: Authentication
- Use the configured admin password
- Session will be maintained for admin functions

### 2. Review Applications

#### Step 1: View All Applications
- Admin panel displays all user applications
- Applications are organized by user and grant type

#### Step 2: Filter and Search
- Use search functionality to find specific users
- Filter by application status
- Sort by application date

### 3. Process Applications

#### Step 1: Review Application Details
- Click on applications to view full details
- Check uploaded documents
- Verify user information

#### Step 2: Make Decisions
- **Approve**: Grant the application
  - Click "Approve" button
  - Application status changes to approved
  - User is notified of approval

- **Disapprove**: Reject the application
  - Click "Disapprove" button
  - Application status changes to disapproved
  - User is notified of rejection

#### Step 3: Verify Users
- Access user verification functions
- Mark users as verified when identity is confirmed
- Update user status in the system

## System Navigation

### User Dashboard Flow
```
Sign In → Profile → Grant Programs → Track Grants
    ↓
Add Docs ← Consent ← Payment
```

### Admin Dashboard Flow
```
Admin Login → Review Applications → Process Decisions
    ↓
User Verification ← Application Management
```

## Troubleshooting

### Common Issues

#### Registration Problems
- **Username Already Exists**: Choose a different username
- **Invalid ID Number**: Ensure ID number is at least 5 digits
- **Invalid Date**: Use the date picker for correct format

#### Login Issues
- **Incorrect Password**: Check password spelling and case
- **User Not Found**: Verify username is correct
- **Session Expired**: Re-login to continue

#### Document Upload Problems
- **File Too Large**: Compress or resize images
- **Invalid File Type**: Use supported image formats (JPG, PNG)
- **Upload Failed**: Check internet connection and try again

#### Grant Application Issues
- **No Eligible Grants**: Complete profile information first
- **Application Failed**: Ensure all required documents are uploaded
- **Duplicate Application**: Check if already applied for the grant

### Error Messages

#### Authentication Errors
- `"User not found"`: Username doesn't exist
- `"Invalid password"`: Password is incorrect
- `"Session expired"`: Need to re-authenticate

#### Application Errors
- `"User not eligible"`: Profile incomplete or requirements not met
- `"Already applied"`: Grant application already submitted
- `"Documents missing"`: Required documents not uploaded

#### System Errors
- `"Server error"`: Contact system administrator
- `"Network error"`: Check internet connection
- `"Database error"`: System maintenance required

## Best Practices

### For Citizens
1. **Complete Profile**: Fill all required information for eligibility
2. **Upload Documents**: Provide clear, legible document images
3. **Monitor Status**: Regularly check application progress
4. **Keep Information Updated**: Update contact and payment information
5. **Read Requirements**: Understand grant requirements before applying

### For Administrators
1. **Regular Reviews**: Process applications promptly
2. **Document Verification**: Thoroughly review uploaded documents
3. **Consistent Decisions**: Apply criteria consistently
4. **User Communication**: Provide clear feedback on decisions
5. **System Monitoring**: Monitor for system issues or errors

## Support and Contact

### Technical Support
- **Email**: support@dsu-api.com
- **Phone**: +1-555-0123
- **Hours**: Monday-Friday, 9 AM - 5 PM

### User Guides
- **Video Tutorials**: Available on the help page
- **FAQ**: Common questions and answers
- **Live Chat**: Available during business hours

### System Status
- **Status Page**: https://dsu-api.com/status
- **Maintenance Notices**: Posted 24 hours in advance
- **Emergency Updates**: Real-time notifications 