from django.views.generic.base import View
from django.views.generic.detail import DetailView

from course.mixins import CourseCreateMixin, CourseUpdateMixin, CourseDeleteMixin
from course.models import Course
from course.forms import CourseForm
from django.views.generic.list import ListView


class CourseList(ListView):
    queryset = Course.objects.all()
    context_object_name = 'courses'
    template_name = 'course/course_list.html'


class CourseDetail(DetailView):
    model = Course
    template_name = 'course/course_detail.html'
    extra_context = {'is_course_mentor': True}


class CourseCreate(CourseCreateMixin, View):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_create.html'


class CourseUpdate(CourseUpdateMixin, View):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_update.html'


class CourseDelete(CourseDeleteMixin, View):
    model = Course
    template_name = 'course/course_delete.html'
    success_url = 'course_list_url'
