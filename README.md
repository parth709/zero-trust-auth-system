

# 🔐 Zero Trust Authentication System (Flask + JWT)

A **Zero Trust–based authentication system** built using **Flask** and **JWT**, demonstrating secure login, **role-based access control (RBAC)**, token expiration, and protected APIs with a simple frontend UI.

This project follows **real-world security principles** used in enterprise applications.

---

## 🚀 Features

- 🔑 JWT Authentication  
- ⏳ Token Expiration (Zero Trust principle)  
- 👥 Role-Based Access Control (Admin / User)  
- 🔒 Protected Routes  
- 🚫 Admin-Only Endpoint  
- 🎯 Custom JWT Error Messages  
- 🖥️ Frontend Login UI (HTML + JS)  
- 🛡️ Zero Trust Architecture Concept  

---

## 🧠 Zero Trust Concept Used

- **Never trust, always verify**
- Every request must carry a valid JWT
- No session-based trust
- Token is verified on **every API call**
- Role is validated before granting access

---

## 🏗️ Project Structure

```

zero-trust-auth-system/
│
├── app.py
├── templates/
│   └── login.html
├── requirements.txt
└── README.md

````

---

## ⚙️ Tech Stack

**Backend:** Flask (Python)  
**Authentication:** Flask-JWT-Extended  
**Frontend:** HTML, CSS, JavaScript  
**Security Model:** Zero Trust Architecture  

---

## 🔑 API Endpoints

### 1️⃣ Login
**POST** `/login`

**Request Body**
```json
{
  "username": "admin",
  "password": "admin123"
}
````

**Response:**
Returns a JWT access token.

---

### 2️⃣ Profile (Protected)

**GET** `/profile`

**Header**

```
Authorization: Bearer <token>
```

Accessible by any authenticated user.

---

### 3️⃣ Admin Panel (Admin Only)

**GET** `/admin`

**Header**

```
Authorization: Bearer <token>
```

Accessible only if `role = admin`.

---

## 🖥️ Frontend UI

* Login using username & password
* Token stored in browser storage
* Buttons to access:

  * Profile API
  * Admin API
* Real-time API response display

---

## ⏱️ Token Expiration

* Access tokens expire in **1 minute**
* Expired tokens are rejected automatically
* User must re-login after expiration

---

## 🚨 Custom Error Handling

* Missing Token
* Invalid Token
* Expired Token
* Unauthorized Role Access

All errors return **clean JSON responses**.

---

## 🧪 How to Run Locally

### 1️⃣ Install Dependencies

```bash
pip install flask flask-jwt-extended
```

### 2️⃣ Run Server

```bash
python app.py
```

### 3️⃣ Open Browser

```
http://127.0.0.1:5000/login-ui
```

---

## 🎯 Use Cases

* Internship / College Project
* Cybersecurity Portfolio
* Zero Trust Demonstration
* JWT Authentication Practice
* Backend Security Learning

---

## 📌 Future Improvements

* Refresh tokens
* Database integration
* Password hashing
* Logout & token revocation
* Deployment (Docker / Cloud)

---

## 👨‍💻 Author

**Parth Patil**
Aspiring Cybersecurity & Backend Developer

---

⭐ If you like this project, give it a **star** and feel free to **fork** 🍴

```

---


