from django.shortcuts import render

from news.models import News
from course.models import Course
from project.models import Project
from account.models import Mentor, User, Sponsor

def home(request):
    news = News.objects.all()[:3]
    courses = Course.objects.all()[:4]
    mentors = Mentor.objects.all()[:3]
    projects = Project.objects.all()[:3]
    context = {
        'news':news,
        'courses':courses,
        'mentors':mentors,
        'projects':projects,
    }
    return render(request, 'home.html', context=context)


def about(request):
    users = User.objects.all()
    projects = Project.objects.all()
    sponsors = Sponsor.objects.all()
    context = {
        'users':users,
        'projects':projects,
        'sponsors':sponsors,
    }
    return render(request, 'about.html', context=context)
