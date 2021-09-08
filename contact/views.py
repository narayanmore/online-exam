from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm
from contact.models import contact
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            res=contact(from_email=from_email,subject=subject,message=message)  #for database save
            res.save()
            try:
                send_mail(subject, message, from_email, ['narayanmore2525@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('http://localhost:8000/startexam/startexam/')

    res= render(request, 'contact/contact.html', {'form': form})
    return res

