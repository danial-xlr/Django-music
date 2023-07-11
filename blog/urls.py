from django.urls import path
from . import views

#app_name = 'blog'
urlpatterns=[
    path('',views.home ,name='home'),
    path('profile/<int:id>/<slug:slug>',views.profile_detail,name='profile_detail'),
    path('song/<int:id>/<slug:slug>', views.song_detail, name='song_detail'),
    path('upload/', views.upload_music, name='upload_music'),
]