from django.urls import path
from course.views import CourseList, CourseDetail, CourseUpdate, CourseDelete, CourseCreate

urlpatterns = [
    path('', CourseList.as_view(), name="course_list_url"),
    path('create/', CourseCreate.as_view(), name='course_create_url'),
    path('<str:slug>/', CourseDetail.as_view(), name='course_detail_url'),
    path('<str:slug>/update/', CourseUpdate.as_view(), name='course_update_url'),
    path('<str:slug>/delete/', CourseDelete.as_view(), name='course_delete_url'),

]
