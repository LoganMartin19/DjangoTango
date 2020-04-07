from . import views
from django.urls import path

urlpatterns = [
    path('', views.NewsArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.NewsArticleDetail.as_view(), name='news_detail'),
]