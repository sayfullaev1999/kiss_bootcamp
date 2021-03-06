from django.urls import path

from course.views import CourseList
from .views import CourseCreate
from .views import CourseDelete
from .views import CourseDetail
# from .views import CourseDetailView
# from .views import CourseListView
from .views import CourseUpdate

urlpatterns = [
    # rest_framework
    # path('course/', CourseListView.as_view()),
    # path('course/<int:pk>', CourseDetailView.as_view()),

    # django
    path('', CourseList.as_view(), name="course_list_url"),
    path('create/', CourseCreate.as_view(), name='course_create_url'),
    path('<str:slug>/', CourseDetail.as_view(), name='course_detail_url'),
    path('<str:slug>/update/', CourseUpdate.as_view(), name='course_update_url'),
    path('<str:slug>/delete/', CourseDelete.as_view(), name='course_delete_url'),

]
