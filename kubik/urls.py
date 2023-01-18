from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('startpage.urls')),
    path('main/', include('mainpage.urls')),
    path('admin/', admin.site.urls),
]