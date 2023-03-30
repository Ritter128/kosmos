from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('mission', views.mission, name='mission'),
  path('posts', views.posts, name='posts'),
  path('rooms/<str:prikey>', views.rooms, name='rooms')
]