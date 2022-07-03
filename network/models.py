from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
  following = models.ManyToManyField("User", blank=True, related_name="fllwing")
  follower = models.ManyToManyField("User", blank=True, related_name="fllwer")

class Post(models.Model):
  content = models.TextField()
  poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_post", null=True)
  created = models.DateTimeField(auto_now_add=True, null=True)
  likes = models.ManyToManyField(User, blank=True, related_name="liked")

  def __str__(self):
    return f"{self.poster} Posted ({self.pk})"
  
  def serialize(self):
    return {
      "id": self.id,
      "content": self.content,
      "poster": self.poster.username,
      "created": self.created.strftime("%b %d %Y, %I:%M %p"),
      "likes": [user.username for user in self.likes.all()]
    }