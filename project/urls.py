from django.urls import path

from .views import ProjectList
from .views import ProjectDetail

urlpatterns = [
    path('', ProjectList.as_view(), name='project_list_url'),
    path('<str:slug>/', ProjectDetail.as_view(), name='project_detail_url')
]
