from django.urls import path, include

from account.views import Register, MentorList, MentorDetail

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('mentors/', MentorList.as_view(), name='mentor_list_url'),
    path('mentor/<str:slug>/', MentorDetail.as_view(), name='mentor_detail_url'),
]
