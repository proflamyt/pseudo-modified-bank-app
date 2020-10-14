
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect 
from django import template
from .models import Transaction
from .form import *


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    transfer = Transaction.objects.all()
    context = {
        'transaction':transfer
        
    }

        


    
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        if html_template.template.name == 'icons.html' and request.POST:
            form = TransactionForm(request.POST)
            if form.is_valid():
                form.save()
                amount = int(request.POST['last_transaction'])

                balance = request.user.amount 

                balance = balance-amount

                request.user.amount = balance

                request.user.save()
                return render(request, 'tables.html')
            error = form.errors
            return render(request, 'icons.html',{'error':error})

            
            
        
        
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))
'''
    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
'''

def home(request):
    return render(request, "new/index.html")

def mail(request):
    error = None
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
 
        if f.is_valid():
            name = f.cleaned_data['Name']
            sender = f.cleaned_data['Email']
            subject  = f.cleaned_data['Telephone']
            message = f.cleaned_data['Message']
            subject = f"You have a new Feedback from {name}:{sender}"
            message = f"Subject: {subject}\n\nMessage: {message}"
           
 
            f.save()
            
  
            context = {
                    
                     'message': 'Feedback Sent'
                }
        
            return HttpResponseRedirect(reverse('home'))            
           
        error = f.errors
    context = {
        'error':error
    }
        
    return render(request, 'new/index.html' ,context)