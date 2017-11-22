from django import forms
from captcha.fields import ReCaptchaField
from .models import post, Comment


class postForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = post
        fields = [
            'title',
            'content',
            'image',
        ]

class commentForm(forms.ModelForm):
    #captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
        ]