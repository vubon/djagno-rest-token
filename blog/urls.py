from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'^create-article/$', views.NewPost.as_view()),
    url(r'^create-author/$', views.CreateAuthor.as_view()),
]