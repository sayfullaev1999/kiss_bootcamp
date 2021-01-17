from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic.list import ListView

from account.forms import UserForm
from account.models import User, Mentor


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


class MentorList(View):
    def get(self, request):
        mentors = Mentor.objects.all()
        return render(request, 'account/mentor_list.html', context={'mentors': mentors})
    # model = Mentor
    # queryset = Mentor.objects.all()
    # template_name = 'account/mentor_list.html'
    # context_object_name = 'mentors'


class MentorDetail(View):
    def get(self, request, slug):
        mentor = get_object_or_404(Mentor, slug__iexact=slug)
        return render(request, 'account/mentor_detail.html', context={'mentor': mentor})
