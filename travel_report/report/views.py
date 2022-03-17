from re import template
from django.shortcuts import render

# Create your views here.
from django.views import generic
class HomeView(generic.TemplateView):
    template_name = "homepage.html"
class LoginView(generic.TemplateView):
    template_name = "login.html"
class SignupView(generic.TemplateView):
    template_name = "signup.html"
class OtherView(generic.TemplateView):
    template_name = "otherpeople.html"