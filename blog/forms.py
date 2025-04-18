from django import forms
from blog.models import Comments
from captcha.fields import CaptchaField

class Commentform(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["post","name","subject","email","message"]