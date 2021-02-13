from django.urls import path, include

from account.views import Register, MentorList, MentorDetail, SponsorList, SponsorDetail

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls')),
    path('register/', Register.as_view(), name='register'),
    path('mentors/', MentorList.as_view(), name='mentor_list_url'),
    path('mentor/<str:slug>/', MentorDetail.as_view(), name='mentor_detail_url'),
    path('sponsors/', SponsorList.as_view(), name='sponsor_list_url'),
    path('sponsor/<str:slug>/', SponsorDetail.as_view(), name='sponsor_detail_url'),
]
