from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    path('accounts/',include('registration.backends.simple.urls')),
    path(r'tinymce/', include('tinymce.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path(r'api-token-auth/', obtain_auth_token)
]