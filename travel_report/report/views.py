from ast import Delete
from calendar import c
from dataclasses import field
from re import template
from django.forms import SlugField
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import ReportCreateForm
from .models import TravelReport
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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



class TravelReportDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = "travelreportdetail.html"
    model = TravelReport

class TravelReportCreateView(LoginRequiredMixin,generic.CreateView):
    model = TravelReport
    template_name = "travelreportcreate.html"
    forms_class = ReportCreateForm
    fields = ('user','title',
        'transportation','cost','member','thoughts')
    success_url = reverse_lazy('report:home')

class TravelReportUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = TravelReport
    template_name = "travelreportupdate.html"
    form_class = ReportCreateForm

    def get_success_url(self):
        return reverse_lazy('report:report_detail',kwargs={'pk':self.kwargs['pk']})
    
    def form_valid(self,form):
        return super().form_valid(form)
    
    def form_invalid(self,form):
        return super().form_invalid(form)



class TravelReportDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = TravelReport
    template_name = "travelreportdelete.html"
    success_url = reverse_lazy('report:home')


