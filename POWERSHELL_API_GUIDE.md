# PowerShell API Testing Guide

## Problem
Regular `curl` syntax doesn't work in PowerShell. You need to use PowerShell's `Invoke-WebRequest` cmdlet instead.

---

## ✅ **CORRECT METHOD FOR POWERSHELL**

### **Step 1: Start the Server (Terminal 1)**
```powershell
cd C:\Users\hdube\employee_api
python manage.py runserver
```
**Expected Output:**
```
Starting development server at http://127.0.0.1:8000/
```
**Keep this terminal running!**

---

### **Step 2: Open NEW Terminal (Terminal 2)**
Do NOT use the server terminal. Open a new PowerShell window.

---

### **Step 3: Get JWT Token**

Copy and paste this **EXACT** command:

```powershell
$headers = @{'Content-Type' = 'application/json'}; $body = @{username='hdube'; password='Hdubey156@'} | ConvertTo-Json; Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/token/" -Method POST -Headers $headers -Body $body
```

**Expected Output:**
```json
StatusCode        : 200
StatusDescription : OK
Content           : {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."}
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 456
                    Content-Type: application/json
```

---

## 📌 **BREAKING DOWN THE COMMAND**

```powershell
# Step 1: Define headers as a hashtable
$headers = @{'Content-Type' = 'application/json'}

# Step 2: Define body with your credentials
$body = @{username='hdube'; password='Hdubey156@'} | ConvertTo-Json

# Step 3: Send the POST request
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/token/" `
    -Method POST `
    -Headers $headers `
    -Body $body
```

---

## 🔑 **EXTRACT YOUR ACCESS TOKEN**

The response contains both `refresh` and `access` tokens. You need the `access` token.

Run this to extract it:

```powershell
# Get the token response
$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/token/" `
    -Method POST `
    -Headers @{'Content-Type' = 'application/json'} `
    -Body (@{username='hdube'; password='Hdubey156@'} | ConvertTo-Json)

# Convert to JSON and extract access token
$tokenData = $response.Content | ConvertFrom-Json
$accessToken = $tokenData.access


# Display the token
Write-Host "Access Token: $accessToken"
```

**Save this token!** You'll need it for all other API calls.

---

## 📋 **ALL API COMMANDS FOR POWERSHELL**

### **1️⃣ GET TOKEN**
```powershell
$headers = @{'Content-Type' = 'application/json'}
$body = @{username='hdube'; password='Hdubey156@'} | ConvertTo-Json
$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/token/" -Method POST -Headers $headers -Body $body
$accessToken = ($response.Content | ConvertFrom-Json).access
Write-Host "Token: $accessToken"
```

---

### **2️⃣ CREATE EMPLOYEE (POST)**
```powershell
# Replace TOKEN with your actual access token
$token = "YOUR_ACCESS_TOKEN_HERE"
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}
$body = @{
    name = 'John Doe'
    email = 'john@example.com'
    department = 'Engineering'
    role = 'Developer'
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/" -Method POST -Headers $headers -Body $body
```

**Expected:** `StatusCode 201`

---

### **3️⃣ LIST ALL EMPLOYEES (GET)**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/" -Method GET -Headers $headers
```

**Expected:** `StatusCode 200` with list of employees

---

### **4️⃣ FILTER BY DEPARTMENT**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

# Filter by Engineering department
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/?department=Engineering" -Method GET -Headers $headers
```

---

### **5️⃣ GET SINGLE EMPLOYEE**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

# Replace 1 with actual employee ID
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/1/" -Method GET -Headers $headers
```

**Expected:** `StatusCode 200` with employee details

---

### **6️⃣ UPDATE EMPLOYEE (PUT)**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}
$body = @{
    name = 'John Updated'
    email = 'john.updated@example.com'
    department = 'Sales'
    role = 'Manager'
} | ConvertTo-Json

# Replace 1 with actual employee ID
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/1/" -Method PUT -Headers $headers -Body $body
```

**Expected:** `StatusCode 200`

---

### **7️⃣ DELETE EMPLOYEE (DELETE)**
```powershell
$token = "YOUR_ACCESS_TOKEN_HERE"
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $token"
}

# Replace 1 with actual employee ID
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/1/" -Method DELETE -Headers $headers
```

**Expected:** `StatusCode 204` (No Content)

---

## ⚠️ **COMMON ERRORS & SOLUTIONS**

### **Error 1: Authentication Header Wrong**
```
"detail": "Authentication credentials were not provided."
```
**Solution:** Make sure your `Authorization` header is exactly:
```powershell
'Authorization' = "Bearer $token"
```

### **Error 2: Invalid JSON in Body**
```
"detail": "JSON parse error - Expecting value"
```
**Solution:** Use `| ConvertTo-Json` to convert PowerShell hashtables to JSON

### **Error 3: Server Not Running**
```
Invoke-WebRequest : Unable to connect to the remote server
```
**Solution:** Run `python manage.py runserver` in the first terminal first

---

## 💡 **QUICK REFERENCE TABLE**

| Method | URL | Purpose | Status |
|--------|-----|---------|--------|
| POST | `/api/token/` | Get JWT token | 200 |
| POST | `/api/employees/` | Create employee | 201 |
| GET | `/api/employees/` | List employees | 200 |
| GET | `/api/employees/?department=X` | Filter by department | 200 |
| GET | `/api/employees/1/` | Get single employee | 200/404 |
| PUT | `/api/employees/1/` | Update employee | 200 |
| DELETE | `/api/employees/1/` | Delete employee | 204 |

---

## 🎯 **COMPLETE WORKFLOW EXAMPLE**

Run these commands in order:

```powershell
# 1. Get token
$headers = @{'Content-Type' = 'application/json'}
$body = @{username='hdube'; password='Hdubey156@'} | ConvertTo-Json
$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/token/" -Method POST -Headers $headers -Body $body
$token = ($response.Content | ConvertFrom-Json).access
Write-Host "✅ Token obtained: $token"

# 2. Create employee
$headers = @{'Content-Type' = 'application/json'; 'Authorization' = "Bearer $token"}
$body = @{name='Jane Smith'; email='jane@example.com'; department='HR'; role='Manager'} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/" -Method POST -Headers $headers -Body $body
Write-Host "✅ Employee created"

# 3. List employees
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/" -Method GET -Headers $headers
Write-Host "✅ Employees listed"

# 4. Filter by department
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/employees/?department=HR" -Method GET -Headers $headers
Write-Host "✅ Filtered by HR department"
```

---

## 📖 **ADDITIONAL TIPS**

1. **Save your token in a variable** - easier to reuse
2. **Always use `-Method POST/GET/PUT/DELETE`** - be explicit
3. **Authorization header format** - `"Bearer $token"` (with space!)
4. **Test in Postman first** - more user-friendly for learning
5. **Use `Write-Host` for readability** - helps track your progress
