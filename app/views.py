from django.shortcuts import render

from app.forms import *
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
# Create your views here.

class DataInsertByTV(TemplateView):
    template_name='DataInsertByTV.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        #ECDO['name']='Kirti'
        #ECDO['age']=23
        ECDO['ECFO']=CollegeForm()
        return ECDO

    def post(self,request):
        CFDO=CollegeForm(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('DONE')
        else:
            return HttpResponse('FAIL')

class InsertDataByFV(FormView):
    template_name='InsertDataByFV.html'
    form_class=CollegeForm
    
    def form_valid(self,form):
        form.save()
        return HttpResponse('DONE')