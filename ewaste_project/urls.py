from django.contrib import admin
from django.urls import path
from collector import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create_item, name='create'),
    path('update/<int:id>/', views.update_item, name='update'),
    path('delete/<int:id>/', views.delete_item, name='delete'),
]
