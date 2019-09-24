from django.contrib import admin
from .models import Post, Comment, Jobrequest, Jobnew

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Jobrequest)
admin.site.register(Jobnew)
