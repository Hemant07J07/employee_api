# Quick Start Guide - Running the Server & Getting JWT Token

## **STEP 1: Activate Virtual Environment**

Open PowerShell and navigate to your project folder:

```powershell
cd C:\Users\hdube\employee_api
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` prefix in your terminal:
```
(venv) PS C:\Users\hdube\employee_api>
```

---

## **STEP 2: Run Database Migrations** (One time only)

If you haven't done this yet:

```powershell
python manage.py migrate
```

Expected output:
```
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, employees, sessions
Running migrations:
  No migrations to apply.
```

---

## **STEP 3: Create a Test User** (One time only)

Create a superuser/test user for authentication:

```powershell
python manage.py createsuperuser
```

Follow the prompts:
```
Username: tester
Email: tester@example.com
Password: testpass123
Password (again): testpass123
Superuser created successfully.
```

Or if you prefer quick test user:

```powershell
python manage.py shell
```

Then in the Python shell:

```python
from django.contrib.auth.models import User
User.objects.create_user(username='tester', password='testpass123')
exit()
```

---

## **STEP 4: Start the Development Server**

```powershell
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**Keep this terminal open!** The server must keep running.

---

## **STEP 5: Open Another PowerShell Terminal**

Open a **NEW PowerShell window** (keep the first one running the server).

Navigate to your project:

```powershell
cd C:\Users\hdube\employee_api
```

Activate virtual environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## **STEP 6: Get JWT Token (Request Authentication)**

Run this command to get your authentication token:

```powershell
curl -s -X POST http://127.0.0.1:8000/api/token/ `
  -H "Content-Type: application/json" `
  -d '{"username":"tester","password":"testpass123"}'
```

**Note:** In PowerShell, use backtick `` ` `` for line continuation instead of backslash `\`

---

## **STEP 7: Copy Your Access Token**

You'll get a response like this:

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNzMwNDkyMCwiaWF0IjoxNzM3MjE4NTIwLCJqdGkiOiIyNmEwODdlZjc4MjE0YThhYTkyZDk4YzZmY2UyNDk5OCIsInVzZXJfaWQiOjF9.abc123...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3MjE4NjIwLCJpYXQiOjE3MzcyMTg1MjAsImp0aSI6IjdiZDI2ZmNmMTMwYzQwMzhiZTQyYThjMDZkZTkzZGJjIiwidXNlcl9pZCI6MX0.xyz789..."
}
```

**Copy the `access` token value** (the long string after `"access": "`).

---

## **STEP 8: Use the Token to Create an Employee**

Now use the token you copied. Replace `YOUR_ACCESS_TOKEN` with your actual token:

```powershell
curl -X POST http://127.0.0.1:8000/api/employees/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" `
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "Engineering",
    "role": "Developer"
  }'
```

**Expected Response (201 Created):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Engineering",
  "role": "Developer",
  "date_joined": "2026-01-16"
}
```

---

## **STEP 9: Get All Employees**

```powershell
curl -X GET "http://127.0.0.1:8000/api/employees/?page=1&department=Engineering" `
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## **STEP 10: Get Single Employee by ID**

```powershell
curl -X GET http://127.0.0.1:8000/api/employees/1/ `
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## **Terminal Setup Overview**

You should have **2 PowerShell windows open:**

### **Terminal 1 (Server Running):**
```
(venv) PS C:\Users\hdube\employee_api> python manage.py runserver
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
✅ **Keep this running** - Don't close it!

### **Terminal 2 (Testing API):**
```
(venv) PS C:\Users\hdube\employee_api> curl -s -X POST http://127.0.0.1:8000/api/token/ ...
```
✅ **Use this to run API commands**

---

## **Complete Workflow Example**

```powershell
# Terminal 1: Start server
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1
python manage.py runserver

# Terminal 2: Get token
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1

# Get token
$response = curl -s -X POST http://127.0.0.1:8000/api/token/ `
  -H "Content-Type: application/json" `
  -d '{"username":"tester","password":"testpass123"}'

# The response contains your token
# Copy the "access" value and use it in next requests

# Create employee
curl -X POST http://127.0.0.1:8000/api/employees/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer <PASTE_YOUR_ACCESS_TOKEN_HERE>" `
  -d '{"name":"John Doe","email":"john@example.com","department":"HR","role":"Manager"}'

# List all employees
curl -X GET "http://127.0.0.1:8000/api/employees/" `
  -H "Authorization: Bearer <PASTE_YOUR_ACCESS_TOKEN_HERE>"
```

---

## **Troubleshooting**

### **Error: "Connection refused" or "Cannot connect to 127.0.0.1:8000"**
- Check that your **first terminal still has the server running**
- Make sure you didn't close Terminal 1

### **Error: "401 Unauthorized"**
- You didn't include the `Authorization` header
- Your token might be incorrect or expired
- Get a new token from `/api/token/`

### **Error: "Invalid username/password"**
- Make sure the credentials match what you created with `createsuperuser`
- Default in docs is `username: tester`, `password: testpass123`

### **Port 8000 already in use**
```powershell
python manage.py runserver 8001
```
Then use `http://127.0.0.1:8001/` instead

---

## **Using Postman Instead of curl**

If you prefer a GUI:

1. **Open Postman**
2. **Create POST request** to `http://127.0.0.1:8000/api/token/`
3. **Set Body** (raw JSON):
   ```json
   {
     "username": "tester",
     "password": "testpass123"
   }
   ```
4. **Click Send** → Copy the `access` token
5. **Create new request** to `http://127.0.0.1:8000/api/employees/`
6. **Go to Authorization tab** → Type: Bearer Token → Paste token
7. **Click Send**

---

## **API Endpoints Summary**

| Method | Endpoint | Auth | Purpose |
|--------|----------|------|---------|
| POST | `/api/token/` | ❌ No | Get access token |
| POST | `/api/employees/` | ✅ Yes | Create employee |
| GET | `/api/employees/` | ✅ Yes | List all employees |
| GET | `/api/employees/{id}/` | ✅ Yes | Get single employee |
| PUT | `/api/employees/{id}/` | ✅ Yes | Update employee |
| DELETE | `/api/employees/{id}/` | ✅ Yes | Delete employee |
| GET | `/swagger/` | ❌ No | API documentation |

---

## **Quick Reference**

```powershell
# 1. Activate venv
.\venv\Scripts\Activate.ps1

# 2. Run server (Terminal 1)
python manage.py runserver

# 3. Get token (Terminal 2)
curl -s -X POST http://127.0.0.1:8000/api/token/ `
  -H "Content-Type: application/json" `
  -d '{"username":"tester","password":"testpass123"}'

# 4. Use token in requests
curl -X GET http://127.0.0.1:8000/api/employees/ `
  -H "Authorization: Bearer <YOUR_TOKEN>"
```

---

**That's it! You're ready to test your API!** 🚀
