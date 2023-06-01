from django.shortcuts import render
from django.views import generic


# Create your views here.

class LoginPageView(generic.TemplateView):
    template_name = 'accounts/login.html'


# render register page.
class RegisterPageView(generic.TemplateView):
    template_name = 'accounts/register.html'
