from django.shortcuts import render, redirect
from task__App.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import ToDo

def SignUp(request):
    return render(request ,"SignUp.html")

def Login(request):
    return render(request, "Login.html")

def TaskManager(request):
    return render(request, "Task_Manager.html")


def saveEnquery(request):
    if request.method == 'POST':
        UserFirstName = request.POST.get("FirstName", "GUST")
        UserSecondName = request.POST.get("LastName", "GUST")
        Useremail = request.POST.get("email", "GUST@gmail.com")
        UserPassword = request.POST.get("Password", "123456")

      # Check if the email already exists
        if User.objects.filter(email=Useremail).exists():
            # A better error message if the email already exists
            messages.error(request, "The email address '{}' is already associated with an existing account. Please use a different email or log in.".format(Useremail))
            return render(request, "Task_Manager.html")  # Redirect to the signup page with error message
        
        # Create a new user and hash their password
        user = User(first_name=UserFirstName, last_name=UserSecondName, email=Useremail)
        user.set_password(UserPassword)  # Hash the password before saving
        user.save()

        # Provide feedback and redirect to the login page
        messages.success(request, "SignUp successful. You can now login.")
        return render(request, "Task_Manager.html") # Redirect to Login page after successful signup
        # return redirect('TaskManager')  # Redirect to Login page after successful signup

    return render(request, "SignUp.html")


def LoginData(request):
    if request.method == 'POST':
        Useremail = request.POST.get("loginEmail", "")
        UserPassword = request.POST.get("loginPassword", "")

        # Check if the email exists in the database
        try:
            user = User.objects.get(email=Useremail)  # Find user by email
            # Check if the entered password matches the stored password
            if user.check_password(UserPassword):  # Verify hashed password
                messages.success(request, "Login successful!")
                return redirect('Task_Manager')  # Redirect to the task manager or dashboard page
            else:
                messages.error(request, "Incorrect password. Please try again.")
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist. Please sign up.")

    return render(request, "Login.html")
    

# we can also view how many users we have.
def viewusers(request):
    user = User.objects.all()
    return render(request, "viewusers.html", {"userData":user})


def add_to_do(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Save the to-do item in the database
        todo = ToDo(title=title, description=description)
        todo.save()

        messages.success(request, "To-Do item added successfully!")
        return redirect('to_do_list')  # Redirect to a to-do list or home page

    return render(request, "add_to_do.html")  # Render a form for adding to-do items

