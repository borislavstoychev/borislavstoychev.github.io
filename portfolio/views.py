from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from djangoProject import settings
from portfolio.forms import ContactForm



def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['stoy4ew@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "index.html", {'form': form})


def successView(request):
    return render(request, 'demo.html')


def index(request):
    return render(request, 'index.html')


def demo(request):
    return render(request, 'demo.html')


def cont(request):
    return render(request, 'contact.html')
