from django.shortcuts import render,redirect
from django.conf import settings
from .forms import RegisterForm, LoginForm
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from article.models import Article
User = settings.AUTH_USER_MODEL

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Uğurla Qeydiyyatdan keçdiniz')
        return redirect('index')
    return render(request, 'register.html', context = {'form':form})

def loginView(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Uğurla daxil oldunuz')
            return redirect('index')
        else:
            messages.warning(request, 'İstifadəçi adı və ya şifrə səhvdir')
    return render(request, 'login.html',{'form':form})

def logoutView(request):
    logout(request)
    messages.success(request,'Uğurlu çıxış')
    return redirect('index')

@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)[:3]
    return render(request,'user/dashboard.html',{'articles':articles})

@login_required
def articles(request):
    articles = Article.objects.filter(author=request.user)
    paginator = Paginator(articles, 10)
    page = request.GET.get('page', 1)
    try:
        articles = paginator.get_page(page)
    except PageNotAnInteger:
        articles = paginator.get_page(1)
    except EmptyPage:
        articles = paginator.get_page(paginator.num_pages)
    return render(request,'user/articles.html',{'articles':articles})
