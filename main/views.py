from django.shortcuts import render, HttpResponse,get_object_or_404
from article.models import Article,Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
import json

def idslug(id,slug):
    return str(id)+ '-' + slug

def index(request,exarticles=None, tagname=None):
    key = request.GET.get('term',None)
    tags = Tag.objects.all()
    articles = Article.objects.all()
    if exarticles is not None:
        articles = exarticles
    if key:
        articles = articles.filter(title__icontains=key)        
    paginator = Paginator(articles, 4)
    page = request.GET.get('page', 1)
    try:
        articles = paginator.get_page(page)
    except PageNotAnInteger:
        articles = paginator.get_page(1)
    except EmptyPage:
        articles = paginator.get_page(paginator.num_pages)
    return render(request, 'index.html',{'articles':articles,'tags':tags,'TagName':tagname})

def search(request):
    key = request.GET.get('term',None)
    if key:
        articles = Article.objects.filter(title__icontains=key)
    else:
        articles = Article.objects.all()
    result = [{'label':article.title, 'id':idslug(article.id,article.slug)} for article in articles]
    return JsonResponse(result,safe=False)

def tags(request,name):
    tag = get_object_or_404(Tag,slug=name)
    articles = Article.objects.filter(tags=tag)
    '''
    paginator = Paginator(articles, 4)
    page = request.GET.get('page', 1)
    tags = Tag.objects.all()
    try:
        articles = paginator.get_page(page)
    except PageNotAnInteger:
        articles = paginator.get_page(1)
    except EmptyPage:
        articles = paginator.get_page(paginator.num_pages)
    return render(request,'index.html',{'articles':articles,'tags':tags})
    '''
    return index(request,exarticles=articles,tagname=tag.name)

def about(request):
    return render(request,'about.html')