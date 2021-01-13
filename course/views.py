from django.shortcuts import render
from django.views.generic.base import View

from course.models import Course
from general.mixins import ObjectDetailMixins, ObjectUpdateMixins, ObjectDeleteMixins, ObjectCreateMixins
from course.forms import CourseForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course/course_list.html", context={'courses': courses})


class CourseDetail(ObjectDetailMixins, View):
    model = Course
    template = 'course/course_detail.html'


class CourseCreate(ObjectCreateMixins, View):
    model = Course
    model_form = CourseForm
    template = 'course/course_create.html'


class CourseUpdate(ObjectUpdateMixins, View):
    model = Course
    model_form = CourseForm
    template = 'course/course_update.html'


class CourseDelete(ObjectDeleteMixins, View):
    model = Course
    template = 'course/course_delete.html'
    redirect_url = 'course_list_url'
