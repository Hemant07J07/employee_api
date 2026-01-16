# 🎤 API Presentation & Demo Script

## **PRESENTATION STRUCTURE**

---

## **PART 1: INTRODUCTION (30 seconds)**

### What to Say:
> "Good morning everyone! Today I'm demonstrating our **Employee Management API** - a RESTful API built with Django that handles complete CRUD operations for employee records. This API showcases authentication with JWT tokens, proper HTTP status codes, error handling, and follows REST best practices."

**Key Points to Highlight:**
- ✅ CRUD Operations (Create, Read, Update, Delete)
- ✅ JWT Authentication
- ✅ RESTful Design Principles
- ✅ Proper Error Handling
- ✅ Pagination & Filtering

---

## **PART 2: AUTHENTICATION (1-2 minutes)**

### Demo Script:
> "First, let's authenticate with the API. We need to get a JWT token by sending a POST request with our credentials. Watch as we send the request..."

### **STEP 1: Get JWT Token**

**Copy and paste EXACTLY:**
```powershell
$headers = @{'Content-Type' = 'application/json'}
$body = @{username='hdube'; password='Hdubey156@'} | ConvertTo-Json
$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/token/" -Method POST -Headers $headers -Body $body
$token = ($response.Content | ConvertFrom-Json).access
Write-Host "✅ Authentication Successful!"
Write-Host "Access Token: $token"
```

### Expected Output:
```
✅ Authentication Successful!
Access Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY4NTg1MjE3LCJpYXQiOjE3Njg1ODQ5MTcsImp0aSI6IjI4Y2U4NzZhZjg2MjQ4MzRiZGY4NjUyYzcyOTE0OTBlIiwidXNlcl9pZCI6IjIifQ.2eOnW44aB2x41DUut5_-9xNHjRGB1Wof_hwUlYFmXBA
```

### What to Say:
> "As you can see, we received a 200 OK status with a JWT token. This token is now stored in the `$token` variable. We'll add this token to the Authorization header for all subsequent requests to authenticate our API calls."

---

## **PART 3: ENDPOINT DEMONSTRATIONS**

### What to Say:
> "Now let's demonstrate all five CRUD endpoints. I'll show you how to create employees, list them, retrieve individual records, update details, and delete records."

---

## **ENDPOINT 1: CREATE EMPLOYEE (POST) - 2 minutes**

### Demo Script:
> "Let's create a new employee with valid data. Notice we're using the Authorization header with our token..."

### **STEP 2: Create Employee (Success Case)**

**Copy and paste:**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"  # Replace with token from Step 1
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}
$body = @{
    name = 'John Doe'
    email = 'john.doe@example.com'
    department = 'Engineering'
    role = 'Developer'
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/" -Method POST -Headers $headers -Body $body
$response.Content | ConvertFrom-Json
```

### Expected Output:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "Engineering",
    "role": "Developer",
    "created_at": "2026-01-16T10:30:45Z",
    "updated_at": "2026-01-16T10:30:45Z"
}
```

### Response Status: ✅ **201 Created**

### What to Say:
> "Excellent! The employee was created successfully with status code 201 - Created. The API returned the complete employee record with an auto-generated ID and timestamps."

---

### **STEP 3: Create Employee (Duplicate Email Error)**

### Demo Script:
> "Now let's demonstrate error handling. What happens if we try to create another employee with the same email address?"

**Copy and paste:**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"  # Use same token
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}
$body = @{
    name = 'Jane Smith'
    email = 'john.doe@example.com'  # Same email - intentional!
    department = 'Sales'
    role = 'Manager'
} | ConvertTo-Json

try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/" -Method POST -Headers $headers -Body $body
} catch {
    $errorResponse = $_.Exception.Response.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($errorResponse)
    $errorContent = $reader.ReadToEnd()
    Write-Host "❌ Error Response:"
    $errorContent | ConvertFrom-Json
}
```

### Expected Output:
```json
{
    "email": [
        "employee with this email already exists."
    ]
}
```

### Response Status: ❌ **400 Bad Request**

### What to Say:
> "Notice the API correctly rejects this request with a 400 Bad Request status. The email field must be unique. The API returns a clear error message so the client knows exactly what went wrong. This is proper REST API error handling."

---

## **ENDPOINT 2: LIST EMPLOYEES (GET) - 2 minutes**

### Demo Script:
> "Now let's retrieve all employees with pagination and filtering capabilities..."

### **STEP 4: List All Employees (with Pagination)**

**Copy and paste:**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"  # Use same token
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/" -Method GET -Headers $headers
$employees = $response.Content | ConvertFrom-Json

Write-Host "✅ Total Employees: $($employees.Count)"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
$employees | ForEach-Object {
    Write-Host "ID: $($_.id) | Name: $($_.name) | Email: $($_.email) | Dept: $($_.department) | Role: $($_.role)"
}
```

### Expected Output:
```
✅ Total Employees: 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ID: 1 | Name: John Doe | Email: john.doe@example.com | Dept: Engineering | Role: Developer
```

### Response Status: ✅ **200 OK**

### What to Say:
> "Perfect! We received all employees with status 200 OK. The API supports pagination - you can add `?page=1&limit=10` to the URL for larger datasets. Next, let's filter by department..."

---

### **STEP 5: Filter Employees by Department**

**Copy and paste:**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"  # Use same token
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

# Create more employees first (optional - for better demo)
$depts = @(
    @{name='Alice Johnson'; email='alice@example.com'; department='Engineering'; role='DevOps'},
    @{name='Bob Wilson'; email='bob@example.com'; department='Sales'; role='Manager'},
    @{name='Carol White'; email='carol@example.com'; department='Engineering'; role='QA'}
)

foreach ($emp in $depts) {
    $body = $emp | ConvertTo-Json
    Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/" -Method POST -Headers $headers -Body $body | Out-Null
}

Write-Host "✅ Added sample employees"
```

**Now filter by Engineering:**
```powershell
$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/?department=Engineering" -Method GET -Headers $headers
$filtered = $response.Content | ConvertFrom-Json

Write-Host "✅ Engineering Department Employees:"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
$filtered | ForEach-Object {
    Write-Host "ID: $($_.id) | $($_.name) | Role: $($_.role)"
}
```

### Expected Output:
```
✅ Engineering Department Employees:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ID: 1 | John Doe | Role: Developer
ID: 3 | Alice Johnson | Role: DevOps
ID: 5 | Carol White | Role: QA
```

### Response Status: ✅ **200 OK**

### What to Say:
> "Excellent! The filtering is working perfectly. We queried `/api/employees/?department=Engineering` and got only the Engineering team members. This demonstrates powerful query parameter support for searching and filtering data."

---

## **ENDPOINT 3: RETRIEVE SINGLE EMPLOYEE (GET by ID) - 2 minutes**

### Demo Script:
> "Let's retrieve a specific employee by their ID, and then I'll show you what happens when we request a non-existent employee..."

### **STEP 6: Get Single Employee (Success - 200 OK)**

**Copy and paste:**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"  # Use same token
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/1/" -Method GET -Headers $headers
$employee = $response.Content | ConvertFrom-Json

Write-Host "✅ Employee Details Found (ID: 1):"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host "Name: $($employee.name)"
Write-Host "Email: $($employee.email)"
Write-Host "Department: $($employee.department)"
Write-Host "Role: $($employee.role)"
Write-Host "Created: $($employee.created_at)"
```

### Expected Output:
```
✅ Employee Details Found (ID: 1):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name: John Doe
Email: john.doe@example.com
Department: Engineering
Role: Developer
Created: 2026-01-16T10:30:45Z
```

### Response Status: ✅ **200 OK**

### What to Say:
> "Perfect! We retrieved the employee record for ID 1 with detailed information. Now watch what happens when we request an employee that doesn't exist..."

---

### **STEP 7: Get Non-Existent Employee (404 Error)**

**Copy and paste:**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"  # Use same token
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/999/" -Method GET -Headers $headers
} catch {
    Write-Host "❌ Error Status: $($_.Exception.Response.StatusCode)"
    $errorResponse = $_.Exception.Response.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($errorResponse)
    $errorContent = $reader.ReadToEnd()
    Write-Host "Error Details: $errorContent"
}
```

### Expected Output:
```
❌ Error Status: NotFound
Error Details: {"detail":"Not found."}
```

### Response Status: ❌ **404 Not Found**

### What to Say:
> "As expected, requesting a non-existent employee (ID 999) returns a 404 Not Found status. The API properly communicates that the resource doesn't exist. This is exactly how REST APIs should behave!"

---

## **ENDPOINT 4: UPDATE EMPLOYEE (PUT) - 2 minutes**

### Demo Script:
> "Now let's update an employee's information. I'll change John Doe's department and role, and the API will return the updated record..."

### **STEP 8: Update Employee (PUT)**

**Copy and paste:**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"  # Use same token
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

$body = @{
    name = 'John Doe'
    email = 'john.doe@example.com'
    department = 'Sales'
    role = 'Senior Manager'
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/1/" -Method PUT -Headers $headers -Body $body
$updatedEmployee = $response.Content | ConvertFrom-Json

Write-Host "✅ Employee Updated Successfully (ID: 1):"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host "Name: $($updatedEmployee.name)"
Write-Host "Email: $($updatedEmployee.email)"
Write-Host "Department: $($updatedEmployee.department) ← CHANGED from Engineering"
Write-Host "Role: $($updatedEmployee.role) ← CHANGED from Developer"
Write-Host "Updated: $($updatedEmployee.updated_at)"
```

### Expected Output:
```
✅ Employee Updated Successfully (ID: 1):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name: John Doe
Email: john.doe@example.com
Department: Sales ← CHANGED from Engineering
Role: Senior Manager ← CHANGED from Developer
Updated: 2026-01-16T10:35:20Z
```

### Response Status: ✅ **200 OK**

### What to Say:
> "Excellent! The update was successful with status 200 OK. Notice the `updated_at` timestamp changed, and the department and role fields now reflect the new values. The API validates all data before updating, ensuring data integrity."

---

## **ENDPOINT 5: DELETE EMPLOYEE (DELETE) - 1 minute**

### Demo Script:
> "Finally, let's demonstrate the delete operation. I'll delete an employee, and the API will confirm with a 204 No Content status..."

### **STEP 9: Delete Employee**

**Copy and paste:**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"  # Use same token
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/5/" -Method DELETE -Headers $headers
Write-Host "✅ Delete Operation Result:"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host "Status Code: $($response.StatusCode)"
Write-Host "Status Description: $($response.StatusDescription)"
Write-Host "Employee ID 5 has been permanently deleted"
```

### Expected Output:
```
✅ Delete Operation Result:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status Code: 204
Status Description: No Content
Employee ID 5 has been permanently deleted
```

### Response Status: ✅ **204 No Content**

### What to Say:
> "Perfect! The delete operation returned 204 No Content - the standard HTTP response for successful deletion. Notice there's no response body because the resource no longer exists. Let's verify it's gone by trying to retrieve it..."

---

### **STEP 10: Verify Deletion (Attempt to Retrieve Deleted Employee)**

**Copy and paste:**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"  # Use same token
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/5/" -Method GET -Headers $headers
} catch {
    Write-Host "✅ Verification Complete:"
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    Write-Host "Status: $($_.Exception.Response.StatusCode)"
    Write-Host "Result: Employee ID 5 no longer exists (as expected!)"
}
```

### Expected Output:
```
✅ Verification Complete:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: NotFound
Result: Employee ID 5 no longer exists (as expected!)
```

### Response Status: ❌ **404 Not Found**

### What to Say:
> "Excellent! The deleted employee now returns 404 Not Found, confirming the deletion was successful. This completes our full CRUD demonstration!"

---

## **PART 4: SUMMARY (1 minute)**

### What to Say:

> "Let's recap what we've demonstrated today:
> 
> ✅ **Authentication**: We obtained a JWT token and used it for secure API access.
> 
> ✅ **Create (POST)**: We created employees and saw proper error handling for duplicate emails (400 Bad Request).
> 
> ✅ **Read (GET)**: We listed all employees, filtered by department, and retrieved individual records by ID.
> 
> ✅ **Update (PUT)**: We modified employee information and received the updated record back.
> 
> ✅ **Delete (DELETE)**: We deleted employees and verified they were removed (404 Not Found).
> 
> This API demonstrates:
> - Proper HTTP status codes (200, 201, 204, 400, 404)
> - RESTful design principles
> - JWT authentication and authorization
> - Input validation and error handling
> - Query parameter filtering
> - Resource timestamps
> 
> Thank you!"

---

## **QUICK REFERENCE: Copy-Paste Commands**

### Terminal Setup:
```powershell
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

### Get Token (Always do this first):
```powershell
$headers = @{'Content-Type' = 'application/json'}
$body = @{username='hdube'; password='Hdubey156@'} | ConvertTo-Json
$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/token/" -Method POST -Headers $headers -Body $body
$token = ($response.Content | ConvertFrom-Json).access
Write-Host "Token: $token"
```

### Use $token in all subsequent requests:
```powershell
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}
```

---

## **TIMING GUIDE**

| Section | Time |
|---------|------|
| Introduction | 0:30 |
| Authentication | 1:00 |
| Create (Success + Error) | 2:00 |
| List & Filter | 2:00 |
| Retrieve (Success + 404) | 2:00 |
| Update | 2:00 |
| Delete | 1:30 |
| Summary | 1:00 |
| **Total** | **~12 minutes** |

---

## **PRO TIPS FOR DEMO DAY**

1. **Test everything beforehand** - Run all commands before the presentation
2. **Have backup token ready** - Copy token to notepad before demo
3. **Speak clearly** - Explain what you're doing as you type
4. **Point to the screen** - Show StatusCode, Content, and error messages
5. **Pause for questions** - After each section
6. **Handle errors gracefully** - If something fails, explain why
7. **Use formatting** - Write-Host with emojis makes it professional

---
