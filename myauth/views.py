from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        username = username.lower()
        email = email.lower()
        if not username or not firstname or not lastname or not email or not password:
            messages.error(request, 'All fields are required')
            return render(request, 'signup.html')
        if len(username) < 3:
            messages.error(request, 'Username too short')
            return render(request, 'signup.html')
        if len(password) < 8:
            messages.error(request, 'Password too short')
            return render(request, 'signup.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'signup.html')
        else:
            user = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
            )
            user.set_password(password)
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect(resolve_url('home'))
    
# class LoginView(View):
#     def get(self, request):
#         return render(request, 'login.html')

#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Logged in successfully!')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid username or password')
#             return render(request, 'login.html')

def LoginView(request):
    next_page = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Both fields are required')
            return render(request, 'login.html')
        username = username.lower()
        user_exist = User.objects.filter(username=username).first()
        if not user_exist:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
        user = authenticate(request, username=username, password=password)  
        if not user:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
        login(request, user_exist)
        messages.success(request, 'Logged in successfully!')
        return redirect(next_page or resolve_url('home'))
    else:
        return render(request, 'login.html')
    
def LogoutView(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect(resolve_url('login'))