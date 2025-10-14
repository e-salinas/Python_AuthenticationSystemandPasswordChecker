# 🔐 Python Authentication System & Password Checker

A Python-based authentication system designed to handle secure user sign-up, login, and password strength verification.

This project was built as part of my cybersecurity learning journey to better understand how authentication works at a foundational level while gaining skills using Python.

---

## 🧰 Project Overview

This tool allows users to:
- **Register** with a username and password.
- **Authenticate** existing users through a login process.
- **Validate password strength** against basic security standards such as:
  - Minimum length
  - Complexity (uppercase, lowercase, digits, symbols)

User credentials are hashed using SHA-256 using the hashlib module and stored in a text file (`users.txt`) and validated at runtime.  
The system is designed to be modular so it can be expanded with more security features (e.g., hashing algorithms, encryption, or database storage).

---

## 🧠 What I Learned

Working on this project helped me:
- Understand **how authentication systems work** at a basic level.
- Implement **input validation** and **password strength checks**.
- Use hashlib to add **password hashing**.
- Setup an audit feature to **log events**.
- Work with **file I/O** for storing and retrieving user data.
- Explore **basic security principles** like password handling and why plaintext passwords should be avoided.
- Gain experience in **structuring, editing, and testing code** to implement changes safely.
- Structure Python code in a modular way to support future improvements.

---

## ⚡ Future Improvements

- Integrate a lockout mechanism after failed login attempts.
- Store credentials in a secure database instead of a flat file.

---

## 🧑‍💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/e-salinas/Python_AuthenticationSystemandPasswordChecker.git
   cd Python_AuthenticationSystemandPasswordChecker
