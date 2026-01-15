# README — Employee Management API

## 1. Project summary & purpose
Build a RESTful CRUD API for employees with authentication, filtering, pagination, and tests.

## 2. Architecture diagram
(Include ASCII or image in /proof/ directory)

## 3. Setup steps (Windows + VSCode)
1. Clone repo
2. python -m venv venv
3. .\venv\Scripts\Activate.ps1
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

## 4. Authentication
- POST /api/token/ to obtain JWT access token.
- Add header `Authorization: Bearer <access>` for all requests.

## 5. API endpoints
- POST /api/employees/  (201)
- GET /api/employees/?page=<n>&department=<>&role=<> (200)
- GET /api/employees/{id}/ (200 / 404)
- PUT /api/employees/{id}/ (200)
- DELETE /api/employees/{id}/ (204)

## 6. Validation & Error handling
- Duplicate email => 400 Bad Request
- Missing/empty name => 400 Bad Request
- Non-existent ID => 404 Not Found

## 7. Tests
- Run: `python manage.py test` (tests cover create, duplicate email, 404 case)

## 8. Proof & Presentation
- Include screenshots: token request, create employee, duplicate email error, filtered list, delete 204
- Include a short demo video (screen recording) showing the 6 required demos.

## 9. Known issues & improvements
- (Explain tradeoffs, e.g., using SQLite for local demo; for production migrate to Postgres)
