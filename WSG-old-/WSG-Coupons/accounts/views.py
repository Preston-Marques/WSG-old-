from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
 
def register(request):
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            person = Person.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form_errors=form.errors
    return render_to_response(
        'registration/register.html',{'person':a,'form':form,'form_errors':form_errors},
        variables,
    )

def register_success(request):
    return render_to_response(
        'registration/success.html',
    )
