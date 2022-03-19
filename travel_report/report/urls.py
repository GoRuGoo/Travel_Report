from importlib.resources import path
from django.urls import URLPattern, path
from . import views

app_name = 'report'
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('./viewotherpeople',views.TravelReportListView.as_view(),name="viewotherpeople"),
]