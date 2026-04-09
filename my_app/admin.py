from django.contrib import admin
from .models import post
# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    

admin.site.register(post, postAdmin)
