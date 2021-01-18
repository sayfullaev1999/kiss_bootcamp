from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('general.urls')),
    path('news/', include('news.urls')),
    path('bot/', include('bot.urls')),
    path('accounts/', include('account.urls')),
    path('course/', include('course.urls')),
    path('project/', include('project.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                            document_root=settings.MEDIA_ROOT)
