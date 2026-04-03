# 💰 Finance Tracker System (Flask-Based)

## 📌 Project Overview

The **Finance Tracker System** is a simple web-based application developed using **Flask** and **SQLite**. It allows users to manage their financial transactions such as income and expenses, view summaries, and access features based on their role.

This project demonstrates backend development concepts including CRUD operations, role-based access control, and database handling in a structured and beginner-friendly way.

---

## 🎯 Objectives

* Build a backend system using Flask
* Implement Create, Read, Update, Delete (CRUD) operations
* Manage financial records efficiently
* Provide summary and analytics (income, expense, balance)
* Implement role-based access (Admin & Viewer)

---

## 🛠️ Technologies Used

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Template Engine:** Jinja2

---

## ✨ Features

### 🔐 Authentication System

* Login functionality with session management
* Two roles:

  * **Admin** → Full access (Add, Edit, Delete)
  * **Viewer** → Read-only access

### 💵 Financial Management

* Add transactions (income/expense)
* Edit existing records
* Delete transactions
* View all financial records

### 📊 Summary Dashboard

* Total Income
* Total Expenses
* Current Balance

### 🎨 User Interface

* Clean and simple UI using CSS
* Navigation bar with user info and logout button
* Role-based dashboard display

---

## 📁 Project Structure

```
finance_app/
│
├── app.py
├── database.db
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── static/
│   └── style.css
```

---

## ▶️ How to Run the Project

### Step 1: Install Flask

```
pip install flask
```

### Step 2: Run the Application

```
python app.py
```

### Step 3: Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔑 Login Credentials

| Role   | Username | Password  |
| ------ | -------- | --------- |
| Admin  | admin    | admin123  |
| Viewer | viewer   | viewer123 |

---

## 🔄 Application Flow

1. User logs in with credentials
2. System validates user role
3. Redirects to dashboard
4. Admin can manage transactions
5. Viewer can only view data
6. Logout ends the session

---

## ⚠️ Assumptions

* Authentication is simplified (no encryption)
* Data is stored locally using SQLite
* Designed for learning and demonstration purposes only

---

## 🚀 Future Enhancements

* Password encryption for security
* Advanced analytics (charts/graphs)
* Export data (CSV/Excel)
* Pagination and search functionality
* Deployment on cloud platform

---

## ✅ Conclusion

This project successfully demonstrates the core concepts of backend development using Flask. It includes database integration, role-based access control, and structured application design, making it a solid foundation for building real-world applications.

---

## 👨‍💻 Author

Sabeeha Irshad
