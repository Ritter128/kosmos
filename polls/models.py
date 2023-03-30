from django.db import models

# Create your models here.

class Person(models.Model):
  name = models.CharField(max_length=20, default='anon')
  age = models.IntegerField(default=0)
  desc = models.TextField(default='empty')
  wealth = models.IntegerField(default=0)
  ethnicity = models.CharField(max_length=20, default='Not specified')
  gender = models.BooleanField(default=True)
  def __str__(self):
      return self.name
  

class House(models.Model):
  owner = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
  acres = models.IntegerField(default=0)
  price = models.IntegerField(default=0)
  desc = models.TextField(default='empty')
  forsale = models.BooleanField(default=True)
  def __str__(self):
      return self.owner

class Post(models.Model):
  author = models.CharField(max_length=20, default='anon')
  content = models.TextField('blank')
  likes = models.IntegerField(default=0)
  timestamp = models.DateTimeField(null=True, auto_now_add=True)
  def __str__(self):
      return f"{self.author} at {self.timestamp}"

class Room(models.Model):
  name = models.CharField(max_length=100, default="No name")
  desc = models.TextField('blank')
  content = models.TextField('blank')
  host = models.CharField(max_length=20, default="Anon")
  def __str__(self):
      return self.name

class Check(models.Model):
  reciever = models.CharField(max_length=20, default="Anon")
  sender = models.CharField(max_length=20, default="Anon")
  amount = models.IntegerField(default=0)
  def __str__(self):
      return f"{self.reciever} => {self.amount} => {self.sender}"
  


