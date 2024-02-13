from django.contrib import admin
from .models import Author, Post


@admin.action(description="Reset mail")
def reset_email(modeladmin, request, queryset):
    queryset.update(email='pls@change.this')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['name', '-email']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    search_help_text = 'Search by author name or email'
    actions = [reset_email]

    fields = ['name', 'email']
    readonly_fields = ['email']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
