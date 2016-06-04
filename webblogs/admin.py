from django.contrib import admin
from webblogs.models import *

class Commentinline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [Commentinline]

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)

# Register your models here.
