from django.contrib import admin
# from .models import Article

from .models import Profile
from .models import Song
from .models import Comment

admin.site.register(Profile)
admin.site.register(Song)
admin.site.register(Comment)