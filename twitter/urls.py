"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from accounts.views import login_view, logout_view, register_view
from tweets.views import delete_message, home_view, all_message_view, message_create_view, message_view,search_message, about

urlpatterns = [
    path('', home_view),
    path('message/<int:tweet_id>', all_message_view),
    path('create-message', message_create_view),
    path('view-message', message_view),
    path('delete-message/<int:tweet_id>', delete_message, name='delete_post'),
    path('search-message', search_message, name='search_post'),
    path('about', about),


    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),

    path('admin/', admin.site.urls),
]
