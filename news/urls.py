from django.urls import path
from .views import NewsList
from .views import NewsDetail
from .views import NewsCreate
from .views import NewsUpdate
from .views import NewsDelete
from .views import Subscribe
from .views import Confirm


urlpatterns = [
    path('', NewsList.as_view(), name='news_list_url'),
    path('subscribe/', Subscribe.as_view(), name='subscribe_url'),
    path('subscribe/confirm/<str:status>/<str:uuid>/', Confirm.as_view(), name='confirm_url'),
    path('create/', NewsCreate.as_view(), name='news_create_url'),
    path('<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('<str:slug>/update/', NewsUpdate.as_view(), name='news_update_url'),
    path('<str:slug>/delete/', NewsDelete.as_view(), name='news_delete_url'),
]
