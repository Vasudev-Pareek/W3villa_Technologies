
# Task Manager Application

🎥 **Video Tutorial Available** 🎥  
A step-by-step video tutorial is available in this repository. [Download Video](TO%20DO%20list%20-%20Tutorial.mp4) or check out the tutorial in the **videos** folder.

---

A web application to manage daily tasks with features like adding, updating, and deleting tasks. Built with Django and MySQL.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setting Up Virtual Environment](#setting-up-virtual-environment)



1. **Clone the Repository**  
   Clone the project repository from GitHub:
   ```bash
   git clone https://github.com/yourusername/project-name.git
    ```
2. **Navigate to Project Directory**
  ```bash
  cd project-name 
  ```

3. **Install Dependencies**
Install the necessary packages listed in the requirements.txt file:
  ```bash
  pip install -r requirements.txt
  ``` 

3. **Run Migrations**
Set up the database by creating necessary tables:
  ```bash
 python manage.py makemigrations
 python manage.py migrate
  ``` 

## Usage
1. **Start the Django Server**
Run the server to use the application:
```bash
python manage.py runserver
```

2. **Access the Application**
Open your web browser and go to:
```bash
http://localhost:8000
```

## Features
- Task Management
    - Add, edit, update, and delete tasks.
- User Authentication
    - Secure user registration and login system.
- Task Search
    - Search for specific tasks to quickly locate them.


## Technologies Used
- Django – Backend framework
- MySQL – Database for storing user and task data
- HTML, CSS, JavaScript – Frontend technologies for user interface


# Alternative Project
There is also an alternative **HTML**, **CSS**, and **JavaScript** project version of this Task Manager with login-signup functionality. You can check it here: -

**Live Link to HTML/CSS/JS Task Manager Project:**
[Link Text](https://vasudevpareek.netlify.app/login%20to-do/)

# Setting Up Virtual Environment
To ensure package isolation, set up a virtual environment, if upper step is not work: -

1. **Install Virtualenv**
```bash
pip install virtualenv
```

2. **Create a Virtual Environment**
```bash
py -m virtualenv erp
```

3. **Activate the Virtual Environment**
```bash
.\erp\Scripts\Activate
```

4. **Install Django**
```bash
pip install Django
```

5. **Verify Django Installation**
```bash
django-admin --version
```

6. **Start a New Django App (if needed)**
```bash
python manage.py startapp erp_App
```

7. **Run Server in Virtual Environment**
```bash
python manage.py runserver
```


# Setting Up in VS Code
Select the Virtual Environment

1. **Open VS Code**.
2. **Go to View > Command Palette.**
3. **Select Python: Select Interpreter.**
4. **Choose Python 3.12.4 ('erp').**
5. **Open Terminal in VS Code**
6. **Go to Terminal > New Terminal or press `Ctrl + ``.**
7. **Run Multiple Servers (optional)**
If you want to run multiple apps simultaneously:
```bash
python manage.py runserver 8002
```


