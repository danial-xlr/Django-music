from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=120)    
    slug = models.SlugField(max_length=120, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    intro = models.TextField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile_detail", args=[self.id, self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)  # Generate slug from the name field
        super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,name=instance.username,age=20,intro="")

post_save.connect(create_user_profile, sender=User)

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=120)
    audio_file = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("song_detail", args=[self.id, self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Generate slug from the title field
        super().save(*args, **kwargs)


class Comment(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.content)  # Generate slug from the content field
        super().save(*args, **kwargs)

    def __str__(self):
        return self.content
