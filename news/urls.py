from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.news_today,name = 'newsToday'),
    path(r'article/(\d+)',views.article,name ='article'),
    path(r'archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews'),
    path(r'search/', views.search_results,name = 'search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)