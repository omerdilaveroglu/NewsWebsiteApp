from django.shortcuts import render,get_object_or_404
from .models import News,Category

# Create your views here.

def home_page(request):
    news_queryset = News.objects.all()
    category= Category.objects.all()
    latest_news = News.objects.order_by('-datetime')[:3]
    return render(request,'index.html',{"category":category,"latest_news":latest_news,"news_queryset":news_queryset})

def detail_page(request,news_id):
    news_queryset = News.objects.all()
    category= Category.objects.all()
    latest_news = News.objects.filter(category_id = news_id).order_by('-datetime')[:3]
    return render(request,"detail.html",{"category":category,"latest_news":latest_news,"news_queryset":news_queryset})