from django.urls import path
from course.views import course_list, CourseDetail, CourseUpdate, CourseDelete, CourseCreate

urlpatterns = [
    path('', course_list, name="course_list_url"),
    path('course/create/', CourseCreate.as_view(), name='course_create_url'),
    path('course/<str:slug>/', CourseDetail.as_view(), name='course_detail_url'),
    path('course/<str:slug>/update/', CourseUpdate.as_view(), name='course_update_url'),
    path('course/<str:slug>/delete/', CourseDelete.as_view(), name='course_delete_url'),

]