# django
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
# Django-rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView

# Course app
from course.forms import CourseForm
from course.models import Course
from course.serializers import CourseListSerializer
from .permissions import CourseMentorPermissionMixin
from .permissions import MentorPermissionMixin


class CourseList(ListView):
    model = Course
    template_name = 'course/course_list.html'


class CourseDetail(DetailView):
    model = Course
    template_name = 'course/course_detail.html'


class CourseCreate(MentorPermissionMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_create.html'


class CourseUpdate(CourseMentorPermissionMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_update.html'


class CourseDelete(CourseMentorPermissionMixin, DeleteView):
    model = Course
    template_name = 'course/course_delete.html'
    success_url = reverse_lazy('course_list_url')

#
# class CourseListView(APIView):
#     def get(self, request):
#         course = Course.objects.all()
#         serializer = CourseListSerializer(course, many=True)
#         return Response(serializer.data)
#
#
# class CourseDetailView(APIView):
#     def get(self, request, pk):
#         course = Course.objects.get(id=pk)
#         serializer = CourseListSerializer(course)
#         return Response(serializer.data)
