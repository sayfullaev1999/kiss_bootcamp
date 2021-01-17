from django.core.exceptions import PermissionDenied

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse


class NewsCreateMixin:
    model = None
    form_class = None
    template_name = None

    def get(self, request):
        if request.user.is_superuser:
            bound_form = self.form_class()
            return render(request, self.template_name, context={'form': bound_form})
        raise PermissionDenied

    def post(self, request):
        if request.user.is_superuser:
            bound_form = self.form_class(request.POST, request.FILES)

            if bound_form.is_valid():
                new_obj = bound_form.save()
                return redirect(new_obj)
            return render(request, self.template_name, context={'form': bound_form})
        raise PermissionDenied()


class NewsUpdateMixin:
    model = None
    form_class = None
    template_name = None

    def get(self, request, slug):
        if request.user.is_superuser:
            obj = get_object_or_404(self.model, slug__iexact=slug)
            bound_form = self.form_class(instance=obj)
            return render(request, self.template_name, context={'form': bound_form})
        raise PermissionDenied()

    def post(self, request, slug):
        if request.user.is_superuser:
            obj = get_object_or_404(self.model, slug__iexact=slug)
            bound_form = self.form_class(request.POST, request.FILES, instance=obj)

            if bound_form.is_valid():
                new_obj = bound_form.save()
                return redirect(new_obj)
            return render(request, self.template_name, context={'form': bound_form})
        raise PermissionDenied()


class NewsDeleteMixin:
    model = None
    template_name = None
    success_url = None

    def get(self, request, slug):
        if request.user.is_superuser:
            obj = get_object_or_404(self.model, slug__iexact=slug)
            return render(request, self.template_name, context={self.model.__name__.lower(): obj})
        raise PermissionDenied()

    def post(self, request, slug):
        if request.user.is_superuser:
            obj = get_object_or_404(self.model, slug__iexact=slug)
            obj.delete()
            return redirect(reverse(self.success_url))
        raise PermissionDenied()
