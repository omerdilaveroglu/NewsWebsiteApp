from django.shortcuts import render,get_object_or_404
from .models import News,Category

# Create your views here.

def home_page(request):
    news_queryset = News.objects.all()
    category= Category.objects.all()
    latest_news = News.objects.order_by('-datetime')[:3]

    content = {"category":category,
               "latest_news":latest_news,
               "news_queryset":news_queryset
    }

    return render(request,'index.html',content)

def category_page(request,category_id):
    news_queryset = News.objects.all()
    category= Category.objects.all()
    latest_news = News.objects.filter(category_id = category_id).order_by('-datetime')[:3]

    content ={
        "category": category,
        "latest_news": latest_news,
        "news_queryset": news_queryset
    }

    return render(request,"detail.html",content)

def detail_page(request,news_id):
    news_queryset = News.objects.all()
    category= Category.objects.all()
    latest_news = News.objects.order_by('-datetime')[:3]
    single_news = get_object_or_404(News,pk=news_id)
    content ={
        "category": category,
        "news_queryset": news_queryset,
        "single_news":single_news,
        "latest_news":latest_news
    }
    return render(request,"single_news_page.html",content)
