from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html',{"email":"contactus@gmail.com","phone":"0653783834"})

def profile(request):
    return render(request, 'profile.html',{"name":"sravya","email":"sravya@gmail.com",
                                           "user_data":
                                               [
                                                   {"name":"sravya", "email": "sravya@gmail.com"},
                                                   {"name":"kavya","email":"kavya@gmail.com"},
                                                   {"name":"raj","email":"raj@gmail.com"}
                                               ]
                                           })

def grade(request,marks):
    return render(request, 'grade.html',{"marks": marks})
def users(request,name,email):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
    return render(request, 'users.html',{"name":name,"email":email})