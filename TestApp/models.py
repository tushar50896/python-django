from django.db import models
from django.utils import timezone
import math

# Create your models here.

class PostCategory(models.Model):
    post_category=models.CharField(max_length=200)
    category_slug=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.post_category


class Post(models.Model):
    title = models.CharField( max_length=200)
    preface = models.CharField(max_length=500, default="Hello")
    content = models.TextField()
    date_posted = models.DateTimeField( auto_now=False, auto_now_add=True)
    post_category=models.ForeignKey(PostCategory,default=0,verbose_name="Categories",on_delete=models.SET_DEFAULT)
    post_slug = models.SlugField(max_length=100)


    def __str__(self):
        return self.title


    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.date_posted

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            return "Just now."

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return "A minute ago."
            
            else:
                return str(minutes) + " minutes ago."



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return "An hour ago."

            else:
                
                return str(hours) + " hours ago."

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return "Yesterday. "

            else:
                return str(days) + " days ago."

        if diff.days >= 30 and diff.days < 365:
            return self.date_posted

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email_id=models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name

