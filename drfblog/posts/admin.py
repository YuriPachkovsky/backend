from django.contrib import admin
from posts.models import *
# Register your models here.

admin.site.register(Author)
admin.site.register(AuthorInfo)
admin.site.register(TextPosts)
admin.site.register(ImagePost)
admin.site.register(Comments)