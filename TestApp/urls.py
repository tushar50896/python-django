from django.urls import path,include
from django.conf.urls import url
from . import views
from .models import Post
from django.views.generic import DetailView

urlpatterns = [
    path('', views.home, name='Site-Home'),
    path('blog/', views.blog, name='Site-Blog'),
    path('contact/',views.contact,name='Site-Contact'),
    path("blog/<slug>",views.post,name="Posts")
    #url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model=Post,template_name='TestApp/post.html')),
]