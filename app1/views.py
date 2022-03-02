from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .forms import *
# Create your views here.

def home(request):
    courses = Course.objects.all()
    p = Paginator(courses, 2)
    page_number = request.GET.get('page')
    
    try:
        course = p.get_page(page_number)
    except PageNotAnInteger:
        course = p.page(1)
    except EmptyPage:
        course = p.page(p.num_pages)
    context = {'courses':course}
    
    return render(request, 'app1/home.html', context)

def userLogin(request):
    return render(request, 'app1/login.html')

def register(request):
    return render(request, 'app1/signup.html')

def profile(request):
    return render(request, 'app1/signup.html')

def courseDetails(request, slug):
    course = Course.objects.get(slug = slug)
    context = {'course':course}
    return render(request, 'app1/course.html', context)

def topicDetails(request, slug):
    topic = Topic.objects.get(slug = slug)
    context = {'topic':topic}
    return render(request, 'app1/topics.html', context)

def article(request, slug):
    topic = Topic.objects.get(slug = slug)
    context = {'article':topic.article}
    return render(request, 'app1/article.html', context)

def video(request, slug):
    topic = Topic.objects.get(slug = slug)
    context = {'video':topic.video}
    return render(request, 'app1/video.html', context)

def discussion(request, slug):
    topic = Topic.objects.get(slug = slug)
    context = {'discussions':topic.discussion_set.all()}
    return render(request, 'app1/discuss.html', context)

def quiz(request, slug):
    topic = Topic.objects.get(slug = slug)
    context = {'quizes':topic.quiz_set.all()}
    return render(request, 'app1/quiz.html', context)