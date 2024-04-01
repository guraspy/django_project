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
from accounts.views import login_view, logout_view, register_view, user_profile_view, edit_profile_view
from tweets.views import delete_tweet, home_view, find_tweet_by_id, tweet_create_view, tweet_view,search_tweet, about, like_tweet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view),
    path('tweet/<int:tweet_id>', find_tweet_by_id),
    path('create-tweet', tweet_create_view),
    path('view-tweet', tweet_view),
    path('delete-tweet/<int:tweet_id>', delete_tweet, name='delete_post'),
    path('search-tweet', search_tweet, name='search_post'),
    path('about', about),
    path('like-tweet', like_tweet, name='like-tweet'),


    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    
    path('profile/<str:username>/', user_profile_view, name='user_profile'),
    path('profile/<str:username>/edit-profile/', edit_profile_view, name='edit_profile'),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)