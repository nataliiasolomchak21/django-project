"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
The comments at the top explain what this file does - it maps URLs to views in the Django app.
We import admin and path from django.urls.
admin will handle the admin site URLs.
urlpatterns is a list that defines the URL routes.
Each path() maps a URL pattern to a view.
The first route is for the admin site at 'admin/'.
admin.site.urls maps the admin site URLs defined by Django.
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_item, name='add'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete')
]
