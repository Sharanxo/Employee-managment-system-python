# **Employee Management System**

A simple **Employee Management System** built using **Python** and **MySQL**. This program allows you to **add, remove, promote, and display employees** stored in a MySQL database.

---

## **📌 Features**
- ✅ Add new employees  
- ✅ Remove existing employees  
- ✅ Promote employees by increasing salary  
- ✅ Display all employee details  
- ✅ Prevent duplicate employee entries  

---

## **📂 Table Structure**
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    post VARCHAR(50),
    salary INT
);
```

---

## **⚙️ Installation & Setup**

### **1️⃣ Install MySQL**
Ensure you have **MySQL** installed and running on your system. If not, download it from:  
🔗 [MySQL Download](https://dev.mysql.com/downloads/)

### **2️⃣ Install Required Python Package**
Install `mysql-connector-python` if not already installed:
```sh
pip install mysql-connector-python
```

### **3️⃣ Configure MySQL Connection**
Edit the database connection in `EMS.py`:
```python
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  # Change this to your MySQL password
    database="emp"    # Make sure the database exists
)
```

### **4️⃣ Create the Database & Table**
Run the following SQL commands in **MySQL Workbench** or **Command Line**:
```sql
CREATE DATABASE emp;
USE emp;
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    post VARCHAR(50),
    salary INT
);
```

---

## **▶️ Running the Program**
Run the script using Python:
```sh
python EMS.py
```

---

## **🖥️ Usage**
### **Main Menu**
```
Welcome to Employee Management Record
Press:
1 to Add Employee
2 to Remove Employee
3 to Promote Employee
4 to Display Employees
5 to Exit
```

### **Example Commands**
#### ➕ **Add Employee**
```
Enter Employee Id: 1
Enter Employee Name: John
Enter Employee Post: Manager
Enter Employee Salary: 70000
Employee Added Successfully
```
#### ❌ **Remove Employee**
```
Enter Employee Id: 1
Employee Removed Successfully
```
#### ⬆️ **Promote Employee**
```
Enter Employee's Id: 2
Enter increase in Salary: 5000
Employee Promoted Successfully
```
#### 📜 **Display Employees**
```
Employee Id: 2
Employee Name: Sarah
Employee Post: Assistant Manager
Employee Salary: 45000
------------------------------------
```

---

## **🛠️ Troubleshooting**
### 🔴 *Error: Authentication plugin 'caching_sha2_password' is not supported*
**Fix**: Run the following MySQL command:
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
FLUSH PRIVILEGES;
```

### 🔴 *Error: Database does not exist*
**Fix**: Ensure you created the **emp** database before running the script.

---

 
