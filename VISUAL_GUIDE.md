# Visual Guide - How to Run the Server & Test API

---

## **🎯 YOUR GOAL**

```
1. Start Server (Terminal 1)
           ↓
2. Get Authentication Token (Terminal 2)
           ↓
3. Use Token to Test API Endpoints (Terminal 2)
```

---

## **PHASE 1: SETUP (One Time)**

```
┌─────────────────────────────────────────────┐
│ PowerShell Terminal 1                       │
│                                             │
│ $ cd C:\Users\hdube\employee_api           │
│ $ .\venv\Scripts\Activate.ps1              │
│ (venv) $ python manage.py createsuperuser  │
│                                             │
│ When asked:                                 │
│ Username: tester                           │
│ Email: tester@example.com                  │
│ Password: testpass123                       │
│                                             │
│ ✅ User created!                           │
└─────────────────────────────────────────────┘
```

---

## **PHASE 2: RUN SERVER**

```
┌──────────────────────────────────────────────────┐
│ PowerShell Terminal 1 - KEEP THIS RUNNING!       │
│                                                  │
│ $ cd C:\Users\hdube\employee_api               │
│ $ .\venv\Scripts\Activate.ps1                  │
│ (venv) $ python manage.py runserver            │
│                                                  │
│ Starting development server at                 │
│ http://127.0.0.1:8000/                         │
│ Quit the server with CTRL-BREAK.               │
│                                                  │
│ ✅ SERVER RUNNING! (Don't close this!)         │
└──────────────────────────────────────────────────┘
```

**⚠️ Important:** Keep Terminal 1 open while you test!

---

## **PHASE 3: OPEN NEW TERMINAL FOR TESTING**

```
┌──────────────────────────────────────────────────┐
│ Open PowerShell Terminal 2 (NEW WINDOW)          │
│                                                  │
│ $ cd C:\Users\hdube\employee_api               │
│ $ .\venv\Scripts\Activate.ps1                  │
│ (venv) $ _  ← Ready for commands!              │
└──────────────────────────────────────────────────┘
```

---

## **PHASE 4: GET TOKEN**

```
Terminal 2 Input:
┌────────────────────────────────────────────────────────┐
│ curl -s -X POST http://127.0.0.1:8000/api/token/ `   │
│   -H "Content-Type: application/json" `              │
│   -d '{"username":"tester","password":"testpass123"}' │
└────────────────────────────────────────────────────────┘
                         ↓
Terminal 2 Output:
┌────────────────────────────────────────────────────────┐
│ {                                                      │
│   "refresh": "eyJhbGc...",                            │
│   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... │
│ }                                                      │
└────────────────────────────────────────────────────────┘
                         ↓
Copy the "access" value → Use in all other requests!
```

---

## **PHASE 5: TEST ENDPOINTS**

### **Step 5.1: Create Employee**

```
Input:
┌────────────────────────────────────────────┐
│ curl -X POST                               │
│   http://127.0.0.1:8000/api/employees/ ` │
│   -H "Content-Type: application/json" ` │
│   -H "Authorization: Bearer YOUR_TOKEN" `│
│   -d '{                                   │
│     "name": "John Doe",                  │
│     "email": "john@example.com",         │
│     "department": "Engineering",         │
│     "role": "Developer"                  │
│   }'                                      │
└────────────────────────────────────────────┘
         ↓ (Server processes)
Output:
┌────────────────────────────────────────────┐
│ HTTP 201 Created                           │
│ {                                          │
│   "id": 1,                                │
│   "name": "John Doe",                    │
│   "email": "john@example.com",           │
│   "department": "Engineering",           │
│   "role": "Developer",                   │
│   "date_joined": "2026-01-16"            │
│ }                                          │
│                                            │
│ ✅ Employee created!                      │
└────────────────────────────────────────────┘
```

### **Step 5.2: Get All Employees**

```
Input:
┌──────────────────────────────┐
│ curl -X GET                  │
│   http://127.0.0.1:8000/api/employees/ `│
│   -H "Authorization: Bearer YOUR_TOKEN"  │
└──────────────────────────────┘
         ↓
Output:
┌──────────────────────────────┐
│ HTTP 200 OK                  │
│ {                            │
│   "count": 1,               │
│   "results": [              │
│     {id: 1, name: "John"... │
│   ]                         │
│ }                            │
│                              │
│ ✅ List retrieved!          │
└──────────────────────────────┘
```

### **Step 5.3: Get One Employee**

```
Input:
┌──────────────────────────────┐
│ curl -X GET                  │
│   http://127.0.0.1:8000/api/employees/1/ `│
│   -H "Authorization: Bearer YOUR_TOKEN"  │
└──────────────────────────────┘
         ↓
Output:
┌──────────────────────────────┐
│ HTTP 200 OK                  │
│ {                            │
│   "id": 1,                  │
│   "name": "John Doe",       │
│   "email": "john@example.com",│
│   ...                        │
│ }                            │
│                              │
│ ✅ Employee found!          │
└──────────────────────────────┘
```

### **Step 5.4: Update Employee**

```
Input:
┌──────────────────────────────┐
│ curl -X PUT                  │
│   http://127.0.0.1:8000/api/employees/1/ `│
│   -H "Authorization: Bearer YOUR_TOKEN" ` │
│   -d '{                      │
│     "name": "John Doe",     │
│     "email": "john@example.com",          │
│     "department": "Sales",  │
│     "role": "Manager"       │
│   }'                         │
└──────────────────────────────┘
         ↓
Output:
┌──────────────────────────────┐
│ HTTP 200 OK                  │
│ {                            │
│   "department": "Sales",    │
│   "role": "Manager",        │
│   ...                        │
│ }                            │
│                              │
│ ✅ Employee updated!        │
└──────────────────────────────┘
```

### **Step 5.5: Delete Employee**

```
Input:
┌──────────────────────────────┐
│ curl -X DELETE               │
│   http://127.0.0.1:8000/api/employees/1/ `│
│   -H "Authorization: Bearer YOUR_TOKEN"  │
└──────────────────────────────┘
         ↓
Output:
┌──────────────────────────────┐
│ HTTP 204 No Content          │
│ (no response body)           │
│                              │
│ ✅ Employee deleted!        │
└──────────────────────────────┘
```

---

## **COMPLETE WORKFLOW DIAGRAM**

```
┌──────────────────────────────────────────────────────────────────┐
│                      YOUR COMPUTER                               │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Terminal 1 (SERVER)           Terminal 2 (TESTING)             │
│  ┌─────────────────────┐       ┌─────────────────────┐          │
│  │ python manage.py    │       │ $ curl -X POST ...  │          │
│  │ runserver           │◄──────│   /api/token/ ...   │          │
│  │                     │       │                     │          │
│  │ http://127.0.0.1    │       │ Gets: access token  │          │
│  │ :8000 ✅ RUNNING    │       │                     │          │
│  │                     │       │ $ curl -X POST ...  │          │
│  │ Listens for HTTP    │◄──────│   /api/employees/ ..│          │
│  │ Requests            │       │                     │          │
│  │                     │       │ Create ✅           │          │
│  │ Returns Responses:  │       │                     │          │
│  │ 201, 200, 204, 400,│       │ $ curl -X GET ...   │          │
│  │ 404, etc.          │◄──────│   /api/employees/ ..│          │
│  │                     │       │                     │          │
│  │                     │       │ List ✅             │          │
│  │ Database (SQLite):  │       │                     │          │
│  │ Stores employees    │       │ $ curl -X DELETE ..│          │
│  │                     │       │   /api/employees/1/│          │
│  │ ✅ Always Running   │       │                     │          │
│  │                     │       │ Delete ✅           │          │
│  └─────────────────────┘       └─────────────────────┘          │
│                                                                  │
│  Data Flow:                                                     │
│  Terminal 2 HTTP Request → Terminal 1 → Database → Response    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## **QUICK CHECKLIST**

```
Before you start:
☐ Virtual environment activated (see (venv) in terminal)
☐ Server running in Terminal 1 (port 8000 listening)
☐ New Terminal 2 opened for testing
☐ Test user created (username: tester, password: testpass123)

Testing:
☐ Get token (POST /api/token/)
☐ Copy access token value
☐ Create employee (POST /api/employees/)
☐ List employees (GET /api/employees/)
☐ Get single employee (GET /api/employees/1/)
☐ Update employee (PUT /api/employees/1/)
☐ Delete employee (DELETE /api/employees/1/)
☐ Try duplicate email → 400 error
☐ Try invalid ID → 404 error
☐ Try without token → 401 error

✅ All tests passing? Great! You're ready for the interview!
```

---

## **PORT ALREADY IN USE?**

If you get "Port 8000 is already in use":

```powershell
# Use different port
python manage.py runserver 8001

# Then all URLs change from :8000 to :8001
curl -X GET http://127.0.0.1:8001/api/employees/ ...
```

---

## **QUICK REFERENCE**

| Task | Command |
|------|---------|
| Activate venv | `.\venv\Scripts\Activate.ps1` |
| Create user | `python manage.py createsuperuser` |
| Start server | `python manage.py runserver` |
| Run tests | `python manage.py test` |
| Get token | `curl -X POST http://127.0.0.1:8000/api/token/ ...` |
| View Swagger | Open browser: `http://127.0.0.1:8000/swagger/` |

---

**You're all set! Start with the checklists above.** ✅
