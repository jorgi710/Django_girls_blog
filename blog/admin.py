from django.contrib import admin

# Register your models here.
import blog.models

admin.site.register(blog.models.Post)
