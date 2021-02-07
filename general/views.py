from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from news.models import News
from course.models import Course
from project.models import Project
from account.models import Mentor, User, Sponsor
from course.forms import ContactUsForm
from news.forms import SubscriberForm


def home(request):
    news = News.objects.all()[:3]
    courses = Course.objects.all()[:4]
    mentors = Mentor.objects.all()[:3]
    projects = Project.objects.all()[:3]
    form = ContactUsForm()
    subscriber_form = SubscriberForm()
    context = {
        'news': news,
        'courses': courses,
        'mentors': mentors,
        'projects': projects,
        'form': form,
        'subscriber_form': subscriber_form
    }
    return render(request, 'home.html', context=context)


def about(request):
    users = User.objects.all()
    projects = Project.objects.all()
    sponsors = Sponsor.objects.all()
    context = {
        'users': users,
        'projects': projects,
        'sponsors': sponsors,
    }
    return render(request, 'about.html', context=context)


def contact_us(request):
    if request.method == 'POST':
        bound_form = ContactUsForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect(reverse('home_url'))
        news = News.objects.all()[:3]
        courses = Course.objects.all()[:4]
        mentors = Mentor.objects.all()[:3]
        projects = Project.objects.all()[:3]
        context = {
            'news': news,
            'courses': courses,
            'mentors': mentors,
            'projects': projects,
            'form': bound_form
        }
        return render(request, 'home.html', context=context)
