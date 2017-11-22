from django.contrib import admin
from .models import post

# Register your models here.
# From post.models import post




class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'publishing_date']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']
    list_editable = ['title']

    class Meta:
        model = post


admin.site.register(post, PostAdmin)