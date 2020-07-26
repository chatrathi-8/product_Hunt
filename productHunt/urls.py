
from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.home, name='home'),
    path('accounts/', include('accounts.urls')),

]
