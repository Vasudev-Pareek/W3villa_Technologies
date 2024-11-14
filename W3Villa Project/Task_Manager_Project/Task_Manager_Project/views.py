from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from task__App.models import User

# def HomePage(request):
#     return HttpResponse("Hey Iam At Home")

# def SignUp(request):
#     return render(request ,"SignUp.html")

# def Login(request):
#     return render(request, "Login.html")

# def UserData(request):
#     # UserFirstName = request.POST.get("FirstName", "GUST")
#     # UserSecondName = request.POST.get("LastName", "GUST")
#     # Useremail = request.POST.get("email", "GUST@gmail.com")
#     # UserPassword = request.POST.get("Password", "123456")

#     # UserFirstName = request.POST["FirstName"]
#     # UserSecondName = request.POST["LastName"]
#     # Useremail = request.POST["email"]
#     # UserPassword = request.POST["Password"]
#     # data = {
#     #     "FirstName":UserFirstName,
#     #     "LastName":UserSecondName,
#     #     "email":Useremail,
#     #     "Password":UserPassword,
#     # }
#     # users = User.objects.all()
#     return render(request ,"UserData.html")
#     # return render(request ,"UserData.html", data)
#     # return render(request, "UserData.html")


# def saveEnquery(request):
#     # if request.method == "POST":
#     if request.method == 'POST':
#         UserFirstName = request.POST.get("FirstName", "GUST")
#         UserSecondName = request.POST.get("LastName", "GUST")
#         Useremail = request.POST.get("email", "GUST@gmail.com")
#         UserPassword = request.POST.get("Password", "123456")
#         data = User(first_name=UserFirstName, last_name=UserSecondName, email=Useremail, password=UserPassword)

#         data.save()
#     return render(request ,"SignUp.html")


# def viewusers(request):
#     user = User.objects.all()
#     return render(request, "viewusers.html", {"userData":user})


# def deleteProfile(request, id):
#     user = User.objects.get(email=id)
#     user.delete()
#     return redirect("/viewusers")


# def register(request):
#     pass

# def login(request):
#     pass

# def dashboard(request):
#     pass

# def logout(request):
#     pass