from django.urls import path
from accounts.views import *
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path("login" , login_view, name="login"),
    path("logout" , logout_view ,name= "logout"),
    path("signup" , signup_view ,name= "signup"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',
                                                                  success_url=reverse_lazy('accounts:password_reset_done'),
                                                                  email_template_name = "accounts/password_reset_email.html"),
                                                                    name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html' , success_url=reverse_lazy("accounts:password_reset_complete")),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
]
