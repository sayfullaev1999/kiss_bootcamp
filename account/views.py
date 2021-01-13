from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View

from account.forms import UserForm


class Register(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'registration/register.html', context={'form': form})

    def post(self, request):
        bound_form = UserForm(request.POST)
        if bound_form.is_valid():
            new_user = bound_form.save()
            login(request, user=new_user)
            return redirect(reverse('home_url'))
        return render(request, 'registration/register.html', context={'form': bound_form})