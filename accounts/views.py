from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CustomUserForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('accounts:login')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            if "@gmail.com" in username:
                user_by_email = User.objects.filter(email=username).first()
                user = authenticate(request , username=user_by_email , password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.add_message(request , messages.ERROR , "The information has not been entered correctly !!" , extra_tags="error")
            else:
                user = authenticate(request , username=username , password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.add_message(request , messages.ERROR , "The information has not been entered correctly !!" , extra_tags="error")
    else:
        return redirect("/")
    return render(request,"accounts/login.html")

@login_required(login_url="/accounts/login")
def logout_view(request):
    logout(request)
    return redirect("/")

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request , messages.SUCCESS , "Registration was successful " , extra_tags="succ")
                return redirect("/")
            
        form = CustomUserForm()
        context = {"form":form }
        return render(request,"accounts/signup.html",context)
    else:
        return redirect("/")   