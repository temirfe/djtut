from django.contrib import admin

from blog.models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)