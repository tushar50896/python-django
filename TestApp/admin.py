from django.contrib import admin
from .models import Post, Visitor,PostCategory
from django.db import models
#tinymce widget
from tinymce.widgets import TinyMCE
class PostAdmin(admin.ModelAdmin):
    formfield_overrides={
        models.TextField:{'widget':TinyMCE()}
    }

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Visitor)
admin.site.register(PostCategory)