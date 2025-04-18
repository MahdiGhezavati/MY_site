from django import forms
from website.models import Contact , Newsletter
from captcha.fields import CaptchaField

class Contactform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        exclude = ["name"]

class newsletterform(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"