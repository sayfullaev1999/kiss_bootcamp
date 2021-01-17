from django.urls import path
from news.views import NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
    path('', NewsList.as_view(), name='news_list_url'),
    path('create/', NewsCreate.as_view(), name='news_create_url'),
    path('<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('<str:slug>/update/', NewsUpdate.as_view(), name='news_update_url'),
    path('<str:slug>/delete/', NewsDelete.as_view(), name='news_delete_url'),
]