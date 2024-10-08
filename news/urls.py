from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.news_today,name = 'newsToday'),
    path(r'article/(\d+)',views.article,name ='article'),
    path(r'archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews'),
    path(r'search/', views.search_results,name = 'search_results'),
    path(r'new/article', views.new_article, name='new-article'),
    path(r'ajax/newsletter/', views.newsletter, name='newsletter'),
    path(r'api/merch/', views.MerchList.as_view(), name='mech-list'),
    re_path(r'api/merch/merch-id/(?P<pk>[0-9]+)/$', views.MerchDescription.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)