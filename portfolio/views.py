from django.shortcuts import render, redirect, HttpResponse
from portfolio.models import Portfolio
from Profiles.models import Profile
from django.conf import settings

from django.core.mail import send_mail,EmailMessage
# Create your views here.


def index(request):
    qs = Profile.objects.all()
    qs1 = Portfolio.objects.all()
    return render(request, 'index.html', {'qs':qs, 'qs1':qs1})


def about(request):
    return render(request, 'about.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blog_single(request):
    return render(request, 'blog-single.html', {})


def contact(request):
    qs = Profile.objects.all()
    return render(request, 'contact.html', {'qs': qs})


def portfolio(request):
    qs = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'qs': qs})


def services(request):
    return render(request, 'services.html', {})


def submit_queries(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    message += "\n Sender's Info: " + name + "  " + email
    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    email.send()
    print('Email sent.')
    # email = send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    return redirect('index')
