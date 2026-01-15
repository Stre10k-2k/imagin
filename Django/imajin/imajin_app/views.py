from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Contact

def sign_up(request):
    if request.method == "POST":
        name = request.POST.get("first_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "").strip()
        confirm_password = request.POST.get("confirm_password", "").strip()

        if name == "" or email == "" or password == "":
            messages.error(request, 'You must fill all gaps')
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
            return redirect("signup")
        
        if password != confirm_password:
            messages.error(request, "Password must be equil to confirm password")
            return redirect("signup")
        
        username = email.split("@")[0]
        
        user = User.objects.create_user(
            first_name = name,
            last_name = name,
            email = email,
            password = password,
            username = username,
        )

        messages.success(request, "Success, you are registered")

        return redirect("login")

    return render(request, "sign_up.html")

def log_in(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "").strip()

        try:
            useremail = User.objects.get(email=email)
            username = str(useremail).strip("@")[0]

        except Exception as e:

            messages.error(request, "User email not found")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user == True:
            login(request, user)
            return redirect("coming")
        
        messages.error(request, "Incorrect password")

        return redirect("login")

    return render(request, "login.html")
def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name", "") or ""
        email = request.POST.get("email", "") or ""
        phone = request.POST.get("phone", "") or ""
        company = request.POST.get("company", "") or ""
        msg = request.POST.get("text", "")

        if msg == "":
            messages.error(request, "Please write your message")
            return redirect("contact")
        
        Contact.objects.create(name=name, email=email, phone=phone, company=company, msg=msg)

        messages.success(request, "Your message is taken")
    return render(request, "contact.html")
def coming_soon(request):
    return render(request, "coming.html")
def not_found(request):
    pass