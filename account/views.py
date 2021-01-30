from django.contrib.auth import login
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic import ListView
from django.views.generic import DetailView

from .forms import UserForm
from .models import Mentor, Sponsor


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


class MentorList(ListView):
    model = Mentor
    template_name = 'account/mentor_list.html'


class MentorDetail(DetailView):
    model = Mentor
    template_name = 'account/mentor_detail.html'


class SponsorList(ListView):
    model = Sponsor
    template_name = 'account/sponsor_list.html'


class SponsorDetail(DetailView):
    model = Sponsor
    template_name = 'account/sponsor_detail.html'
