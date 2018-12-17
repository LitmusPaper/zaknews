from django.shortcuts import render,redirect, get_object_or_404, reverse
from .forms import ArticleForm, CommentForm
from django.contrib import messages
from .models import Article, Comment, Tag
from django.utils.text import slugify
from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def add(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.slug = slugify(form.data['title'])
        article.save()
        article.tags.add(form.data['tags'])
        
        messages.success(request,'Məqalə əlavə olundu')
        return redirect('user:dashboard')
    return render(request,'article/add.html',{'form':form})

@login_required
def edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user.has_perm('article.change_article') or article.author==request.user:
        form = ArticleForm(instance=article,data=request.POST or None, files=request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Məqalə redəktə olundu')
            return redirect('article:detail',id=article.id, slug=article.slug)
        return render(request, 'article/edit.html',{'form':form})
    else:
        messages.warning(request,'Buna icazəniz yoxdur')
        return redirect('index')

@login_required
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user.has_perm('article.delete_article') or article.author==request.user:
        article.delete()
        messages.success(request,'Məqalə silindi')
        return redirect('index')
    else:
        messages.warning(request,'Buna icazəniz yoxdur')
        return redirect('index')


def detail(request,id,slug='default'):
    article = get_object_or_404(Article,id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid() and request.user.is_authenticated:
        comment = form.save(commit=False)
        comment.article = article
        comment.author = request.user
        comment.save()
        form = CommentForm()
    return render(request,'article/detail.html',{'article':article,'form':form})

# TAG
def tags(request,name):
    articles = Article.objects.filter(tags__name=name)
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