
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', include('home.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
]
