from django.urls import path
from . import views

urlpatterns=[
    path('',views.news_today,name = 'newsToday'),
    path(r'archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews')
]