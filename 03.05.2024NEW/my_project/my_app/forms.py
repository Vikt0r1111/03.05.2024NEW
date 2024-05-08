from django import forms
from captcha.fields import CaptchaField
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ContactMessage
        fields = ['email', 'name', 'content']