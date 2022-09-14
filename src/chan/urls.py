from django.urls import path

from . import views


urlpatterns = [
    path('news/<int:news_id>', views.news, name='news'),
    path('news/', views.newslist, name='news'),
    path('rules/', views.rules, name='rules'),
    path('faq/', views.faq, name='faq'),
    path('', views.index, name='index'),
    path('<str:board_url>/', views.board, name='board'),
    path('<str:board_url>/thread/<str:thread_id>', views.thread, name='thread'),
]
