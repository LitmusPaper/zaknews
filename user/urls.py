from django.urls import path, include
from user import views

app_name='user'

urlpatterns = [
    path('register/', views.register, name ='register'),
    path('login/', views.loginView, name ='login'),
    path('logout/', views.logoutView, name ='logout'),
    path('', views.dashboard, name ='dashboard'),
    path('articles', views.articles, name ='articles'),

]