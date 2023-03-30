from django.contrib import admin

# Register your models here.
from .models import Person, House, Post, Room, Check

admin.site.register(Person)
admin.site.register(House)
admin.site.register(Post)
admin.site.register(Room)
admin.site.register(Check)