# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render


# Create your views here.
from django.views.generic.base import TemplateView
from .models import Student
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import LoginForm


class HomeView(TemplateView):
    template_name = 'index.html'


def index(request):
    return render(request, 'index.html')


def department(request):
    return render(request, 'department.html')


def login(request):
    return render(request, 'login.html')


def student_list(request):
    students = Student.objects.all()
    context = 'students : students'
    return render(request, 'student_list.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            if User.objects.filter(username=username).exists():
                # User.objects.create_user(username, password)
                user = authenticate(username=username, password=password)

            else:
                raise forms.ValidationError('Looks like a username with that email or password does not exists')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

