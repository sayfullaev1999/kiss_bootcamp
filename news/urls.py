from django.urls import path
from news.views import news_list, NewsDetail, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
    path('', news_list, name='news_list_url'),
    path('news/create/', NewsCreate.as_view(), name='news_create_url'),
    path('news/<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('news/<str:slug>/update/', NewsUpdate.as_view(), name='news_update_url'),
    path('news/<str:slug>/delete/', NewsDelete.as_view(), name='news_delete_url'),
]