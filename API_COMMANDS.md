# Copy-Paste Ready Commands - Testing Your API

All commands below are ready to copy and paste into PowerShell Terminal 2 (while server runs in Terminal 1).

---

## **Setup (One Time)**

### **Create Test User**
```powershell
python manage.py createsuperuser
```

When prompted:
```
Username: tester
Email: tester@example.com
Password: testpass123
Password (again): testpass123
```

Or use quick method:
```powershell
python manage.py shell
```

Then paste:
```python
from django.contrib.auth.models import User
User.objects.create_user(username='tester', password='testpass123')
exit()
```

---

## **Terminal 1: Start Server (Keep Running)**

```powershell
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

**Output should be:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

## **Terminal 2: Test Commands**

Open a NEW PowerShell terminal and run:

```powershell
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1
```

---

## **1️⃣ GET JWT TOKEN**

Copy and paste:

```powershell
curl -s -X POST http://127.0.0.1:8000/api/token/ `
  -H "Content-Type: application/json" `
  -d '{"username":"tester","password":"testpass123"}'
```

**Output:**
```json
{
  "refresh": "...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

📌 **Copy the `access` value** - you'll need it for next commands!

---

## **2️⃣ CREATE EMPLOYEE (201 Created)**

Copy and paste (replace TOKEN with your access token):

```powershell
curl -X POST http://127.0.0.1:8000/api/employees/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3MjE4NjIwLCJpYXQiOjE3MzcyMTg1MjAsImp0aSI6IjdiZDI2ZmNmMTMwYzQwMzhiZTQyYThjMDZkZTkzZGJjIiwidXNlcl9pZCI6MX0.xyz..." `
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "Engineering",
    "role": "Developer"
  }'
```

**Expected:**
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

✅ Status: 201 Created

---

## **3️⃣ CREATE DUPLICATE EMPLOYEE (400 Bad Request)**

Try creating the same email again:

```powershell
curl -X POST http://127.0.0.1:8000/api/employees/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer YOUR_TOKEN" `
  -d '{
    "name": "Jane Doe",
    "email": "john.doe@example.com",
    "department": "Sales",
    "role": "Manager"
  }'
```

**Expected Error:**
```json
{
  "email": [
    "employee with this email already exists."
  ]
}
```

❌ Status: 400 Bad Request

---

## **4️⃣ CREATE EMPLOYEE WITH EMPTY NAME (400 Bad Request)**

```powershell
curl -X POST http://127.0.0.1:8000/api/employees/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer YOUR_TOKEN" `
  -d '{
    "name": "",
    "email": "test@example.com",
    "department": "HR"
  }'
```

**Expected Error:**
```json
{
  "name": [
    "Name must not be empty."
  ]
}
```

❌ Status: 400 Bad Request

---

## **5️⃣ LIST ALL EMPLOYEES (200 OK)**

```powershell
curl -X GET http://127.0.0.1:8000/api/employees/ `
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Expected:**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "department": "Engineering",
      "role": "Developer",
      "date_joined": "2026-01-16"
    }
  ]
}
```

✅ Status: 200 OK

---

## **6️⃣ LIST WITH PAGINATION (page 2)**

```powershell
curl -X GET "http://127.0.0.1:8000/api/employees/?page=2" `
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## **7️⃣ FILTER BY DEPARTMENT**

```powershell
curl -X GET "http://127.0.0.1:8000/api/employees/?department=Engineering" `
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## **8️⃣ FILTER BY ROLE**

```powershell
curl -X GET "http://127.0.0.1:8000/api/employees/?role=Developer" `
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## **9️⃣ FILTER BY BOTH**

```powershell
curl -X GET "http://127.0.0.1:8000/api/employees/?department=Engineering&role=Developer" `
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## **🔟 GET SINGLE EMPLOYEE (200 OK)**

```powershell
curl -X GET http://127.0.0.1:8000/api/employees/1/ `
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Expected:**
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

✅ Status: 200 OK

---

## **1️⃣1️⃣ GET NON-EXISTENT EMPLOYEE (404 Not Found)**

```powershell
curl -X GET http://127.0.0.1:8000/api/employees/9999/ `
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Expected Error:**
```json
{
  "detail": "Not found."
}
```

❌ Status: 404 Not Found

---

## **1️⃣2️⃣ UPDATE EMPLOYEE (200 OK)**

```powershell
curl -X PUT http://127.0.0.1:8000/api/employees/1/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer YOUR_TOKEN" `
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "Sales",
    "role": "Senior Developer"
  }'
```

**Expected:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Sales",
  "role": "Senior Developer",
  "date_joined": "2026-01-16"
}
```

✅ Status: 200 OK

---

## **1️⃣3️⃣ DELETE EMPLOYEE (204 No Content)**

```powershell
curl -X DELETE http://127.0.0.1:8000/api/employees/1/ `
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Expected:**
- No response body
- Just empty output

✅ Status: 204 No Content

---

## **1️⃣4️⃣ DELETE NON-EXISTENT EMPLOYEE (404 Not Found)**

```powershell
curl -X DELETE http://127.0.0.1:8000/api/employees/9999/ `
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Expected Error:**
```json
{
  "detail": "Not found."
}
```

❌ Status: 404 Not Found

---

## **1️⃣5️⃣ REQUEST WITHOUT TOKEN (401 Unauthorized)**

```powershell
curl -X GET http://127.0.0.1:8000/api/employees/
```

**Expected Error:**
```json
{
  "detail": "Authentication credentials were not provided."
}
```

❌ Status: 401 Unauthorized

---

## **Quick Token Storage (Optional)**

To avoid copying token each time, save it to a variable:

```powershell
# Get token and save to variable
$response = curl -s -X POST http://127.0.0.1:8000/api/token/ `
  -H "Content-Type: application/json" `
  -d '{"username":"tester","password":"testpass123"}'

# Convert to object
$json = $response | ConvertFrom-Json

# Get access token
$token = $json.access

# Now use $token in commands
curl -X GET http://127.0.0.1:8000/api/employees/ `
  -H "Authorization: Bearer $token"
```

---

## **Swagger UI (No Token Needed)**

Visit in browser:
```
http://127.0.0.1:8000/swagger/
```

You can test all endpoints visually with a nice UI!

---

## **Postman Collection (Alternative)**

Instead of curl, use **Postman**:

1. Open Postman
2. Create new folder "Employee API"
3. Create requests:
   - POST /api/token/
   - POST /api/employees/
   - GET /api/employees/
   - GET /api/employees/{id}/
   - PUT /api/employees/{id}/
   - DELETE /api/employees/{id}/
4. Set Authorization → Bearer Token for each request
5. Paste token from step 1

---

## **Summary Table**

| # | Method | Endpoint | Token? | Status | Response |
|---|--------|----------|--------|--------|----------|
| 1 | POST | /api/token/ | ❌ | 200 | access + refresh |
| 2 | POST | /api/employees/ | ✅ | 201 | created employee |
| 3 | POST | /api/employees/ | ✅ | 400 | duplicate error |
| 4 | GET | /api/employees/ | ✅ | 200 | employee list |
| 5 | GET | /api/employees/1/ | ✅ | 200 | single employee |
| 6 | GET | /api/employees/9999/ | ✅ | 404 | not found |
| 7 | PUT | /api/employees/1/ | ✅ | 200 | updated employee |
| 8 | DELETE | /api/employees/1/ | ✅ | 204 | no content |
| 9 | DELETE | /api/employees/9999/ | ✅ | 404 | not found |
| 10 | ANY | /api/employees/ | ❌ | 401 | unauthorized |

---

**Ready to test! 🚀**
