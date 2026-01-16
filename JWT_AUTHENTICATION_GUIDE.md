# Understanding JWT Token Authentication - Step by Step

## **What is Happening?**

The curl command is authenticating your user and getting a **JWT (JSON Web Token)** to use for API requests.

---

## **The Authentication Flow**

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR COMPUTER                             │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Terminal 1 (Server):          Terminal 2 (Client):          │
│  ┌──────────────────┐          ┌──────────────────┐          │
│  │ Django Server    │◄────────►│ curl Command     │          │
│  │ :8000            │  HTTP    │ (PowerShell)     │          │
│  │                  │          │                  │          │
│  │ Running...       │          │ Sends username   │          │
│  └──────────────────┘          │ + password       │          │
│                                └──────────────────┘          │
│                                          │                   │
│                                          ▼                   │
│                                   Server checks              │
│                                   credentials               │
│                                          │                   │
│                                          ▼                   │
│                                  Returns TOKEN              │
│                                   (access +                 │
│                                    refresh)                 │
└─────────────────────────────────────────────────────────────┘
```

---

## **PART 1: Starting the Server**

### **Step 1.1: Open PowerShell**
- Right-click on desktop → Select "Open PowerShell here" OR
- Press `Win + X` → Select "Windows PowerShell (Admin)"

### **Step 1.2: Navigate to Your Project**
```powershell
cd C:\Users\hdube\employee_api
```

### **Step 1.3: Activate Virtual Environment**
```powershell
.\venv\Scripts\Activate.ps1
```

**You should see:**
```
(venv) PS C:\Users\hdube\employee_api>
```

The `(venv)` prefix means your virtual environment is active ✅

### **Step 1.4: Run the Server**
```powershell
python manage.py runserver
```

**You should see:**
```
Watching for file changes with StatReloader
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**⚠️ IMPORTANT: Keep this terminal window open! Don't close it!**

---

## **PART 2: Getting the Token (New Terminal)**

### **Step 2.1: Open a NEW PowerShell Window**

**While Terminal 1 is still running**, open a second PowerShell window.

### **Step 2.2: Activate Virtual Environment (again)**
```powershell
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1
```

### **Step 2.3: Run the Authentication Command**

Copy and paste this exact command:

```powershell
curl -s -X POST http://127.0.0.1:8000/api/token/ `
  -H "Content-Type: application/json" `
  -d '{"username":"tester","password":"testpass123"}'
```

**Breaking it down:**

| Part | Meaning |
|------|---------|
| `curl` | Command to make HTTP requests |
| `-s` | Silent mode (no progress bar) |
| `-X POST` | HTTP method = POST request |
| `http://127.0.0.1:8000/api/token/` | Server address + endpoint |
| `-H "Content-Type: application/json"` | Header saying "I'm sending JSON" |
| `-d '{"username":"tester","password":"testpass123"}'` | The data (credentials) |
| `` ` `` | PowerShell line continuation character |

---

## **PART 3: Understanding the Response**

### **Step 3.1: You'll Get JSON Like This:**

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNzMwNDkyMCwiaWF0IjoxNzM3MjE4NTIwLCJqdGkiOiIyNmEwODdlZjc4MjE0YThhYTkyZDk4YzZmY2UyNDk5OCIsInVzZXJfaWQiOjF9.abc123xyz789...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3MjE4NjIwLCJpYXQiOjE3MzcyMTg1MjAsImp0aSI6IjdiZDI2ZmNmMTMwYzQwMzhiZTQyYThjMDZkZTkzZGJjIiwidXNlcl9pZCI6MX0.xyz789abc123..."
}
```

### **Step 3.2: What Each Part Means**

- **`refresh` token:** Used to get a new `access` token when it expires
- **`access` token:** Your pass to make API requests (THIS IS WHAT YOU NEED!)

### **Step 3.3: Copy the Access Token**

Find this line:
```
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0..."
```

Copy the long string starting with `eyJ...` (the whole thing until the next quote).

---

## **PART 4: Using the Token to Create an Employee**

### **Step 4.1: In Terminal 2, Run This Command:**

Replace `YOUR_ACCESS_TOKEN` with the token you copied:

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

### **Step 4.2: What This Does:**

| Part | Does What |
|------|-----------|
| `curl -X POST` | Send a POST request (create something) |
| `http://127.0.0.1:8000/api/employees/` | Create an employee at this address |
| `Authorization: Bearer YOUR_ACCESS_TOKEN` | "Here's my token, I'm allowed!" |
| `-d '{...}'` | The employee data to create |

### **Step 4.3: You Get This Response (201 Created):**

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

✅ **Success! Employee created!**

---

## **Complete Terminal Examples**

### **Example 1: Full Workflow (Copy & Paste)**

**Terminal 1:**
```powershell
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

Then open **Terminal 2:**

```powershell
cd C:\Users\hdube\employee_api
.\venv\Scripts\Activate.ps1

# Get token
curl -s -X POST http://127.0.0.1:8000/api/token/ `
  -H "Content-Type: application/json" `
  -d '{"username":"tester","password":"testpass123"}'
```

You'll see the token response. Copy the `access` value.

Then create an employee (replace TOKEN):

```powershell
curl -X POST http://127.0.0.1:8000/api/employees/ `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." `
  -d '{"name":"Alice Smith","email":"alice@example.com","department":"HR","role":"Manager"}'
```

---

## **Diagram: Where Everything Runs**

```
┌──────────────────────────────────────────────────────────┐
│             YOUR COMPUTER (Windows PC)                   │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  ┌─────────────────────┐      ┌──────────────────────┐   │
│  │   Terminal 1        │      │   Terminal 2         │   │
│  │  (SERVER RUNNING)   │      │  (CLIENT - TESTING)  │   │
│  │                     │      │                      │   │
│  │ Command:            │      │ Command:             │   │
│  │ python manage.py    │      │ curl -X POST ...     │   │
│  │ runserver           │      │                      │   │
│  │                     │      │ Sends:               │   │
│  │ Listens on:         │◄─────┤ Username + Password  │   │
│  │ http://127.0.0.1    │      │                      │   │
│  │ :8000               │      │ Receives:            │   │
│  │                     │      │ Access Token         │   │
│  │ Database:           │      │                      │   │
│  │ Stores/Reads Data   │      │ Uses Token:          │   │
│  │                     │      │ curl -X POST ...     │   │
│  │ Running ✅          │      │ -H "Authorization    │   │
│  │                     │      │ Bearer TOKEN"        │   │
│  └─────────────────────┘      └──────────────────────┘   │
│                                                           │
│  Data Flow: Terminal 2 → HTTP → Terminal 1 (Django)     │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

---

## **Common Questions**

### **Q: Why do I need 2 terminals?**
A: One runs the server (must keep running), one sends requests to it.

### **Q: What if I close Terminal 1?**
A: The server stops. Terminal 2 commands will fail. Reopen Terminal 1 and run the server again.

### **Q: How long is the token valid?**
A: By default, JWT access tokens expire in ~5 minutes. Get a new one when needed.

### **Q: What if the curl command doesn't work?**
A: 
- Make sure `http://127.0.0.1:8000` is accessible (server running in Terminal 1)
- Check username/password are correct
- In PowerShell, use `` ` `` (backtick) for line breaks, not `\` (backslash)

### **Q: Can I use Postman instead?**
A: Yes! It's easier. Import the collection and set Bearer token in the Authorization tab.

---

**You're now ready to test your API!** 🚀
