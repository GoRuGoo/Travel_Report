from importlib.resources import path
from django.urls import URLPattern, path
from . import views

app_name = 'report'
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('travelreportlistview/',views.TravelReportListView.as_view(),name="travelreportlistview"),
    path('not-exist/',views.NotView.as_view(),name="none")
]
#urlのルーティングをするときは~~~~/とする。