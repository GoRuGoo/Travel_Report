from calendar import c
from re import template
from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import TravelReport
from django.contrib.auth.mixins import LoginRequiredMixin
class HomeView(generic.TemplateView):
    template_name = "homepage.html"


class TravelReportListView(LoginRequiredMixin,generic.ListView):
    model = TravelReport
    template_name = 'travelreport.html'
    '''
    def get_queryset(self,**kwargs):
        reports = TravelReport.objects
        return reports
    '''
class NotView(generic.TemplateView):
    template_name = "404.html"