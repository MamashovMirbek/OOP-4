# User Management System

## Overview
This Python project implements a User Management System using Object-Oriented Programming principles. The system allows users to be added, stored, and managed efficiently.

## Features
- **User Class**: Represents a user with details like ID, name, surname, email, password, and birthday.
- **UserService Class**: Manages user records, allowing adding, deleting, and updating users.
- **UserUtil Class**: Provides utility functions like generating user IDs, strong passwords, and validating emails.
- **Interactive CLI**: Allows users to enter their details and be stored in the system.

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/MamashovMirbek/OOP-4/
   ```
2. Navigate to the project folder:
   ```bash
   cd user-management-system
   ```
3. Run the script:
   ```bash
   python user_management_system.py
   ```

## UML Diagram
A UML class diagram representing the system is included in the `uml_diagram.png` file.

## Sample Input/Output
**Example Interaction:**
```
Welcome to the User Management System!

Choose an option:
1. Add a new user
2. Finish
Enter your choice (1 or 2): 1
Enter your first name: Mirbek
Enter your last name: Mamashov
Enter your birthday (YYYY-MM-DD): 2002-01-03

User successfully created!
User ID: 190401007, Name: Mirbek Mamasho, Email: mirbek.mamashov@alatoo.edu.kg
Generated Password: P@s5w0rD (Keep it safe!)
Age: 23
Total Users in System: 1
```

## Author
- **Mirbek Mamashov** (MamashovMirbek)

