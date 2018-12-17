from django.urls import path, include
from article import views

app_name = 'article'
urlpatterns = [
    path('add/',views.add, name='add'),
    path('<int:id>-<slug:slug>/',views.detail, name='detail'),
    path('<int:id>/edit/',views.edit, name='edit'),
    path('<int:id>/delete/',views.delete, name='delete'),

]