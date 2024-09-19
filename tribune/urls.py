from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    path('accounts/',include('registration.backends.simple.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]