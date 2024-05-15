from django.shortcuts import render, get_object_or_404
from .models import Outcome
from django import forms
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .module import ope_db

class NewScheduleForm(forms.Form):
    title = forms.CharField(label='用途', max_length=25, required=True)
    date = forms.DateField(label='日時', widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d'], required=True)
    price = forms.IntegerField(label='金額', required=True)
    note = forms.CharField(widget=forms.Textarea, max_length=200, required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
    

# Create your views here.
def index(request):
    outcomes = {'outcomes': ope_db.get()} 
    return render(request, 'dashboard/index.html', outcomes)

def form(request):
    my_dict = {'form': NewScheduleForm()}
    return render(request, 'dashboard/form.html', my_dict)

def update(request, outcome_id):
    outcome = get_object_or_404(Outcome, pk=outcome_id)
    form = NewScheduleForm()
    form.fields["title"].initial = outcome.title
    form.fields["date"].initial = outcome.date
    form.fields["price"].initial = outcome.price
    form.fields["note"].initial = outcome.note
    
    my_dict = {'form': form, 'outcome_id': int(outcome_id)}
    return render(request, 'dashboard/form.html', my_dict)

def outcome_save(request):
    # Test print 
    print(ope_db.get())
    print(request.POST)
    print(request.POST["title"])
    # Test print end
    ope_db.write(title=request.POST["title"],
                 date =request.POST["date"],
                 price=request.POST["price"],
                 note =request.POST["note"])
    
    return HttpResponseRedirect(reverse("dashboard:index"))

def outcome_update(request, outcome_id):
    ope_db.update(outcome_id,
                title=request.POST["title"],
                date =request.POST["date"],
                price=request.POST["price"],
                note =request.POST["note"])
    
    return HttpResponseRedirect(reverse("dashboard:index"))

def outcome_delete(request, outcome_id):
    ope_db.delete(outcome_id)
    return HttpResponseRedirect(reverse("dashboard:index"))
    