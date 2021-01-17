from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from django.core.exceptions import PermissionDenied
from django.urls import reverse


class BaseCourseMixin:
    model = None
    form_class = None
    template_name = None
    success_url = None

    @staticmethod
    def permission_check(course, user):
        if user.is_superuser:
            return True
        for mentor in course.mentor.values():
            if user.id == mentor.get('user_id'):
                return True
        return False


class CourseCreateMixin(BaseCourseMixin):
    def get(self, request):
        if request.user.is_superuser:
            bound_form = self.form_class()
            return render(request, self.template_name, context={'form': bound_form})
        raise PermissionDenied()

    def post(self, request):
        if request.user.is_superuser:
            bound_form = self.form_class(request.POST, request.FILES)
            if bound_form.is_valid():
                new_course = bound_form.save()
                return redirect(new_course)
        raise PermissionDenied()


class CourseUpdateMixin(BaseCourseMixin):
    def get(self, request, slug):
        course = get_object_or_404(self.model, slug__iexact=slug)
        if self.permission_check(course, request.user):
            bound_form = self.form_class(instance=course)
            return render(request, self.template_name, context={'form': bound_form})
        raise PermissionDenied()

    def post(self, request, slug):
        course = get_object_or_404(self.model, slug__iexact=slug)
        if self.permission_check(course, request.user):
            bound_form = self.form_class(request.POST, request.FILES, instance=course)
            if bound_form.is_valid():
                new_course = bound_form.save()
                return redirect(new_course)
            return render(request, self.template_name, context={'form': bound_form})
        raise PermissionDenied()


class CourseDeleteMixin(BaseCourseMixin):
    def get(self, request, slug):
        course = get_object_or_404(self.model, slug__iexact=slug)
        if self.permission_check(course, request.user):
            return render(request, self.template_name, context={self.model.__name__.lower(): course})
        raise PermissionDenied()

    def post(self, request, slug):
        course = get_object_or_404(self.model, slug__iexact=slug)
        if self.permission_check(course, request.user):
            course.delete()
            return redirect(reverse(self.success_url))
        raise PermissionDenied()
