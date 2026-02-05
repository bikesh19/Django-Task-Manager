# CRUD To-Do Task Application Using Django with Authentication

## 1. Title

**Design and Implementation of a CRUD To-Do Task Management System Using Django with User Authentication**

---

## 2. Objective

The objective of this lab is to design and implement a web-based To-Do Task Management System using Django that supports:

- User authentication (login & registration)
- CRUD operations (Create, Read, Update, Delete) on tasks
- Secure access so users can manage only their own tasks

---

## 3. Theory

### 3.1 CRUD Operations

CRUD stands for:

- **Create** – Add new tasks  
- **Read** – View existing tasks  
- **Update** – Modify task details  
- **Delete** – Remove tasks  

CRUD is the foundation of most database-driven applications and ensures efficient data management.

---

### 3.2 Django Framework

Django is a high-level Python web framework that follows the **MTV (Model–Template–View)** architecture:

- **Model** – Handles database structure  
- **Template** – Handles user interface  
- **View** – Handles application logic and request/response  

Django provides the following features:

- Built-in authentication system  
- ORM (Object Relational Mapping) for database operations  
- Security features such as CSRF protection and password hashing  

---

### 3.3 Authentication

Authentication verifies the identity of users.

In this application:

- Users must register and log in to access the system  
- Only authenticated users can create, update, or delete tasks  
- Each task is linked to a specific user, ensuring data privacy  

---

## Features

- User registration and login
- Create, view, update, and delete tasks
- Tasks are user-specific
- Clean and beginner-friendly project structure

---

## Setup Instructions


# 1. Clone the repository
git clone https://github.com/bikesh19/Django-Task-Manager.git
cd Django-Task-Manager

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver

# 6. Open the application in your browser
# http://127.0.0.1:8000/


---
## 7. Discussion

The To-Do Task application successfully demonstrates CRUD operations integrated with user authentication. Django’s ORM simplifies database interaction, while the built-in authentication system ensures secure access control. The clear separation of models, views, and templates improves maintainability and scalability of the application.

---

## 8. Conclusion

In this lab, a CRUD-based To-Do Task Management System was developed using Django. The application provides secure authentication and efficient task management functionality. This lab enhanced understanding of Django architecture, database modeling, and secure web application development.

---

## Author

**Bikesh Sah**

