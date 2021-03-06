from importlib.resources import path
from django.urls import URLPattern, path
from . import views

app_name = 'report'
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('travelreportlistview/',views.TravelReportListView.as_view(),name="travelreportlistview"),
    path('not-exist/',views.NotView.as_view(),name="none"),
    path('report_detail/<int:pk>/',views.TravelReportDetailView.as_view(),name='report_detail'),
    path('report_create/',views.TravelReportCreateView.as_view(),name="report_create"),
    path('report_update/<int:pk>',views.TravelReportUpdateView.as_view(),name="report_update"),
    path('report_delete/<int:pk>',views.TravelReportDeleteView.as_view(),name="report_delete"),
]
#urlのルーティングをするときは~~~~/とする。