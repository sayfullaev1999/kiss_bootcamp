from django.views.generic import ListView, DetailView

from project.models import Project


class ProjectList(ListView):
    model = Project


class ProjectDetail(DetailView):
    model = Project
