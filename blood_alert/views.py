from django.shortcuts import render, redirect

from .models import Alert
from .forms import AddAlertForm, ResolvedAlertForm

from datetime import datetime

# Create your views here.

def alerts(request):
    alert = Alert.objects.all().order_by('date_time_posted').reverse()
    return render(
        request,
        'blood_alert/alerts.html',
        {'alerts': alert},
    )

def add_alert(request, template='blood_alert/add_alert.html'):
    form = AddAlertForm(request.POST or None)
    if form.is_valid():
        new_alert = Alert()
        new_alert.name = form.cleaned_data['name']
        new_alert.blood_type = form.cleaned_data['blood_type']
        new_alert.phone = form.cleaned_data['phone']
        new_alert.location = form.cleaned_data['location']
        new_alert.message = form.cleaned_data['message']
        new_alert.save()
        return redirect('alerts')
    context = {
        'form': form
    }
    return render(request, template, context)
