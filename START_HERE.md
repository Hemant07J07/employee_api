# 🚀 START HERE - Complete Server & API Testing Guide

## **What You Need to Know**

Your API is **working correctly**. This guide shows you exactly how to:
1. Start the server
2. Get an authentication token
3. Test all API endpoints

---

## **📋 QUICK START (5 minutes)**

### **Terminal 1: Start Server**

```powershell
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

**Keep this running! Don't close it!** ✅

### **Terminal 2: Test API (Open NEW window)**

```powershell
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1

# Step 1: Get Token
curl -s -X POST http://127.0.0.1:8000/api/token/ `
  -H "Content-Type: application/json" `
  -d '{"username":"tester","password":"testpass123"}'

# Copy the "access" value from response

# Step 2: Create Employee (replace TOKEN with your access value)
curl -X POST http://127.0.0.1:8000/api/employees/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer TOKEN" `
  -d '{"name":"John Doe","email":"john@example.com","department":"Engineering","role":"Developer"}'
```

**That's it!** You're now testing your API! 🎉

---

## **📚 Full Documentation Files**

Your project now has 4 helpful guides:

| File | Purpose | Read When |
|------|---------|-----------|
| **QUICK_START_GUIDE.md** | Step-by-step setup | You're just starting |
| **JWT_AUTHENTICATION_GUIDE.md** | Understand how tokens work | You want to learn concepts |
| **API_COMMANDS.md** | Copy-paste all test commands | You're ready to test |
| **VISUAL_GUIDE.md** | Diagrams and flow charts | You're visual learner |

---

## **⚠️ Important Rules**

1. **Terminal 1 MUST stay running** with `python manage.py runserver`
2. **Use Terminal 2** for all curl commands
3. **Token goes in Authorization header** like: `Authorization: Bearer YOUR_TOKEN`
4. **Tokens expire** after ~5 minutes, get a new one if needed
5. **Use backtick** `` ` `` for line breaks in PowerShell, not backslash `\`

---

## **🔑 Key Concepts**

### **What is a JWT Token?**
- Short: **Authentication Pass**
- Your username/password → Token → Use token for all requests
- Like showing ID card once, getting a badge to wear

### **What is curl?**
- **Command Line Tool** to send HTTP requests
- Like Postman, but text-based
- `-X POST` = method, `-H` = header, `-d` = data

### **What is http://127.0.0.1:8000?**
- `127.0.0.1` = Your computer
- `:8000` = Port (server listening here)
- Local server only (not on internet)

---

## **🎯 The Process**

```
1. Start Server (Terminal 1)
         ↓
2. Get Token (Terminal 2 - POST /api/token/)
         ↓
3. Copy Access Token
         ↓
4. Use Token in Authorization Header
         ↓
5. Test Endpoints (POST/GET/PUT/DELETE)
         ↓
6. See Results (201/200/204/400/404)
```

---

## **⚡ Common Commands Quick Copy**

### **Get Token:**
```powershell
curl -s -X POST http://127.0.0.1:8000/api/token/ `
  -H "Content-Type: application/json" `
  -d '{"username":"tester","password":"testpass123"}'
```

### **Create Employee:**
```powershell
curl -X POST http://127.0.0.1:8000/api/employees/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer YOUR_TOKEN" `
  -d '{"name":"John Doe","email":"john@example.com","department":"Engineering","role":"Developer"}'
```

### **List Employees:**
```powershell
curl -X GET http://127.0.0.1:8000/api/employees/ `
  -H "Authorization: Bearer YOUR_TOKEN"
```

### **Get One Employee:**
```powershell
curl -X GET http://127.0.0.1:8000/api/employees/1/ `
  -H "Authorization: Bearer YOUR_TOKEN"
```

### **Update Employee:**
```powershell
curl -X PUT http://127.0.0.1:8000/api/employees/1/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer YOUR_TOKEN" `
  -d '{"name":"John Doe","email":"john@example.com","department":"Sales","role":"Manager"}'
```

### **Delete Employee:**
```powershell
curl -X DELETE http://127.0.0.1:8000/api/employees/1/ `
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## **✅ Success Indicators**

### **Good Sign (Server Running):**
Terminal 1 shows:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### **Good Sign (Token Received):**
Terminal 2 shows:
```json
{
  "refresh": "...",
  "access": "eyJhbGc..."
}
```

### **Good Sign (Employee Created):**
Terminal 2 shows:
```json
{
  "id": 1,
  "name": "John Doe",
  ...
}
```
With status `201 Created`

---

## **❌ Common Issues & Fixes**

| Problem | Solution |
|---------|----------|
| "Connection refused" | Start server in Terminal 1 |
| "Cannot connect to 127.0.0.1:8000" | Check Terminal 1 is running |
| "401 Unauthorized" | Add Authorization header with token |
| "400 Bad Request" | Check JSON syntax (quotes, commas) |
| "404 Not Found" | Employee ID doesn't exist |
| "Port 8000 in use" | Run on different port: `runserver 8001` |
| Command not working | Use backtick `` ` `` not backslash `\` |

---

## **🌐 Browser Alternatives**

Don't want to use curl? Try these:

### **Option 1: Swagger UI (No token needed!)**
Open browser: `http://127.0.0.1:8000/swagger/`
- Visual interface
- Click buttons instead of typing
- Very easy for demos

### **Option 2: Postman (Download free)**
- Create requests visually
- Save token in Bearer authentication
- Better for presentations

### **Option 3: Thunder Client (VS Code extension)**
- Built into VS Code
- Similar to Postman
- No separate download needed

---

## **📊 All Endpoints**

| Method | URL | Needs Token | Purpose | Status |
|--------|-----|-------------|---------|--------|
| POST | `/api/token/` | ❌ | Get JWT token | 200 |
| POST | `/api/employees/` | ✅ | Create employee | 201 |
| GET | `/api/employees/` | ✅ | List all | 200 |
| GET | `/api/employees/{id}/` | ✅ | Get one | 200/404 |
| PUT | `/api/employees/{id}/` | ✅ | Update | 200 |
| DELETE | `/api/employees/{id}/` | ✅ | Delete | 204 |
| GET | `/swagger/` | ❌ | API docs | 200 |

---

## **🎓 Learning Path**

1. **Beginner:** Read QUICK_START_GUIDE.md
2. **Intermediate:** Follow API_COMMANDS.md and copy-paste
3. **Advanced:** Read JWT_AUTHENTICATION_GUIDE.md to understand concepts
4. **Presentation:** Use VISUAL_GUIDE.md to explain to others

---

## **💡 Pro Tips**

1. **Save token to variable** (PowerShell):
   ```powershell
   $token = "eyJhbGc..."
   curl -X GET http://127.0.0.1:8000/api/employees/ `
     -H "Authorization: Bearer $token"
   ```

2. **Test filtering:**
   ```powershell
   curl -X GET "http://127.0.0.1:8000/api/employees/?department=Engineering" `
     -H "Authorization: Bearer YOUR_TOKEN"
   ```

3. **Pretty print JSON** (PowerShell):
   ```powershell
   curl ... | ConvertFrom-Json | ConvertTo-Json
   ```

4. **Use Postman for interviews** - looks more professional than curl

---

## **🚨 Setup Checklist**

Before you test:

- [ ] Virtual environment created (`venv` folder exists)
- [ ] Python packages installed (`pip install -r requirements.txt`)
- [ ] Database migrated (`python manage.py migrate`)
- [ ] Test user created (`python manage.py createsuperuser` or shell)
- [ ] Server running (`python manage.py runserver` in Terminal 1)
- [ ] .env file created (for security config)

All checked? You're ready to test! 🎉

---

## **📞 File Structure**

```
C:\Users\hdube\employee_api\
├── README.md                      ← Main project doc
├── QUICK_START_GUIDE.md          ← THIS ONE FIRST
├── JWT_AUTHENTICATION_GUIDE.md    ← Learn concepts
├── API_COMMANDS.md               ← Copy-paste commands
├── VISUAL_GUIDE.md               ← Diagrams & flow
├── SECURITY_FIXES.md             ← Security improvements
├── manage.py                      ← Django manager
├── config/                        ← Django config
│   ├── settings.py               ← App settings
│   ├── urls.py                   ← URL routing
│   └── wsgi.py                   ← Server config
├── employees/                     ← Your API app
│   ├── models.py                 ← Employee model
│   ├── views.py                  ← API endpoints
│   ├── serializers.py            ← Data validation
│   ├── urls.py                   ← App URLs
│   ├── tests.py                  ← Unit tests
│   └── migrations/               ← Database versions
├── db.sqlite3                    ← Database
├── requirements.txt              ← Python packages
├── .env                          ← Environment vars
├── .env.example                  ← Example .env
└── .gitignore                    ← Git ignore rules
```

---

## **🎯 Your Next Steps**

1. **Read:** QUICK_START_GUIDE.md
2. **Do:** Follow the setup steps
3. **Test:** Copy commands from API_COMMANDS.md
4. **Demo:** Record screen showing all endpoints
5. **Present:** Explain your work to interviewer

---

**You've got this! Your API is production-ready. Now test it! 🚀**

For questions, refer to the detailed guides in the root folder.
