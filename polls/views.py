from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Person, House, Post, Room
from django.template import loader

# Create your views here.
def index(request):
  if request.POST:
    print('POST!!!!!!!!')

  persons_data = Person.objects.all().values()
  houses_data = House.objects.all().values()
  rooms_data = Room.objects.all().values()


  template = loader.get_template('main/housepolls.htmx')
  context = {
    'persons': persons_data,
    'houses': houses_data,
    'rooms': rooms_data,
  }
  return HttpResponse(template.render(context, request)) 

def about(request):
  return render(request, 'main/about.htmx', {})

def mission(request):
  return render(request, 'main/mission.htmx', {})

def posts(request):
  posts_data = Post.objects.all().values()

  template = loader.get_template('main/posts.htmx')
  context = {
    'posts': posts_data,
  }
  return HttpResponse(template.render(context, request)) 

def rooms(request, prikey):
  current_room = Room.objects.filter(name=prikey)

  template = loader.get_template('main/rooms.htmx')
  context = {
    'name': current_room.values_list('name', flat=True).get(),
    'desc': current_room.values_list('desc', flat=True).get(),
    'content': current_room.values_list('content', flat=True).get(),
    'host': current_room.values_list('host', flat=True).get(),
  }
  return HttpResponse(template.render(context, request)) 
