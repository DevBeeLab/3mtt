from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from app.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def homepage(request):
    return render(request, 'home.html')

@login_required
def aboutpage(request):
    return render(request, 'about.html')

# def contactpage(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         if not name or not email or not message:
#             messages.error(request, 'all filed are required')
#             return render(request, 'contact.html')
#         if len(name) < 3:
#             messages.error(request, 'name too short')
#             return render(request, 'contact.html')

#         else:
#             messages.success(request, 'your form has been submitted')
#             return redirect('home')

#     else:
#         return render(request, 'contact.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            messages.error(request, 'all filed are required')
            return render(request, 'contact.html')
        if len(name) < 3:
            messages.error(request, 'name too short')
            return render(request, 'contact.html')

        else:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'your form has been submitted')
            return redirect('home')


