__author__ = 'yinmingke'
from django import forms

from django.forms import PasswordInput, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserProfileForm(forms.Form):
    qq = forms.CharField(label='QQ号码', max_length=30, required=True,
                         widget=forms.TextInput(attrs={'class': 'form-control', }))
    mobile = forms.CharField(label='手机号码', max_length=30, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', }))
    wang = forms.CharField(label='阿里旺旺', max_length=30, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control', }))


class ForgetPasswordForm(forms.Form):
    user_name = forms.CharField(label='手机号码', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '手机号码', 'class': 'form-control'}))
    sms_code = forms.CharField(label='验证码', required=True)


class ChangePasswordForm(forms.Form):
    password_old = forms.CharField(label='旧密码',
                                   widget=PasswordInput(attrs={'placeholder': '旧密码', 'class': 'form-control'}),
                                   required=True)
    password_1 = forms.CharField(label='新密码',
                                 widget=PasswordInput(attrs={'placeholder': '新密码', 'class': 'form-control'}),
                                 required=True)
    password_2 = forms.CharField(label='密码确认',
                                 widget=PasswordInput(attrs={'placeholder': '密码确认', 'class': 'form-control'}),
                                 required=True)


class SignUpForm(forms.Form):
    user_name = forms.CharField(label='手机号码', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '手机号码', 'class': 'form-control'}))
    password_1 = forms.CharField(label='密码', widget=PasswordInput(attrs={'placeholder': '密码', 'class': 'form-control'}),
                                 required=True)
    password_2 = forms.CharField(label='密码确认',
                                 widget=PasswordInput(attrs={'placeholder': '密码确认', 'class': 'form-control'}),
                                 required=True)
    sms_code = forms.CharField(label='验证码', required=True)


class CreateNewUserForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '用户名', 'class': 'form-control'}))
    email = forms.EmailField(label='电子邮件', required=True,
                             widget=forms.EmailInput(attrs={'placeholder': '电子邮件', 'class': 'form-control'}))
    password_1 = forms.CharField(label='密码', widget=PasswordInput(attrs={'placeholder': '密码', 'class': 'form-control'}),
                                 required=True)
    password_2 = forms.CharField(label='密码确认',
                                 widget=PasswordInput(attrs={'placeholder': '密码确认', 'class': 'form-control'}),
                                 required=True)

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        if User.objects.filter(username=user_name).count() > 0:
            raise ValidationError('该用户名已经被注册', code="userexists")
        return user_name

    def clean_email(self):
        user_email = self.cleaned_data.get("email")
        if User.objects.filter(email=user_email).count() > 0:
            raise ValidationError('该email已经被注册', code='emailexists')
        return user_email

    def clean_password_2(self):
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")
        if password_1 and password_2 and password_1 != password_2:
            raise ValidationError('两次输入的密码必须一致', code="pwd")
        return password_2


class LoginForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '用户名', 'class': 'form-control'}))
    password = forms.CharField(label='密码', widget=PasswordInput(attrs={'placeholder': '密码', 'class': 'form-control'}),
                               required=True)

    def clean_user_name(self):
        uname = self.cleaned_data.get("user_name")
        upwd = self.data.get("password")
        user = authenticate(username=uname, password=upwd)
        if user is None:
            raise ValidationError("输入的用户名和密码不匹配", code='login_error')
        return uname


'''
hello
'''
