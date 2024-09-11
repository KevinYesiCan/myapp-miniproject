from django.contrib import admin
from django.urls import path, include
from myapp import views
from .views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Changed 'home' to 'index'
    path('login/', login_view, name='login'),
    # path('success/', success_view, name='success_page'),
]
