from importlib.resources import path
from django.urls import URLPattern, path
from . import views

app_name = 'report'
urlpatterns = [
    path('',views.IndexView.as_view(),name="test"),
]