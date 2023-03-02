from django.contrib import admin
from demoapp.models import Blog

# Register your models here.
#admin.site.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'tags', 'keywords')
    list_filter = ('created_at',)

admin.site.register(Blog, BlogAdmin)
