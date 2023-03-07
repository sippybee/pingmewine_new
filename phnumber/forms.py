from django import forms
from django.conf import settings
from phonenumber_field.formfields import PhoneNumberField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.core.mail import send_mail
from django.urls import reverse


class ClientForm(forms.Form):
    phone = PhoneNumberField(region="US")
    # captcha = ReCaptchaField()
