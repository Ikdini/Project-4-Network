
from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("login", views.login_view, name="login"),
  path("logout", views.logout_view, name="logout"),
  path("register", views.register, name="register"),
  path("create_post", views.create_post, name="create_post"),
  path("toggle_likes/<int:post_id>/", views.toggle_likes, name="toggle_likes"),
  path("profile/<poster>/", views.profile, name="profile"),
]