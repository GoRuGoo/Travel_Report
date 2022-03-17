from importlib.resources import path
from django.urls import URLPattern, path
from . import views

app_name = 'report'
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('./login',views.LoginView.as_view(),name="login"),
    path('./signup',views.SignupView.as_view(),name="signup"),
    path('./viewotherpeople',views.OtherView.as_view(),name="viewotherpeople"),
]