from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class CourseMentorPermissionMixin(AccessMixin):
    def has_permissions(self, request):
        return hasattr(self.request.user, 'mentor') and self.request.user.mentor in self.get_object().mentor.all() or self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not self.has_permissions(request):
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class MentorPermissionMixin(CourseMentorPermissionMixin):
    def has_permissions(self, request):
        return hasattr(self.request.user, 'mentor') or self.request.user.is_superuser
