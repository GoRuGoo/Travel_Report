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
    template_name = 'travel_report.html'
    
    def get_queryset(self):
        reports = TravelReport.objects.filter(user=self.request.user).order_by('-created_at')
        return reports