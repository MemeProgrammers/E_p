from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('login/', userLogin, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('course/<slug:slug>/', courseDetails, name='course'),
    path('topic/<slug:slug>/', topicDetails, name='topic'),
    path('article/<slug:slug>/', article, name='article'),
    path('video/<slug:slug>/', video, name='video'),
    path('discussion/<slug:slug>/', discussion, name='discussion'),
    path('quiz/<slug:slug>/',quiz, name='quiz'),
]
