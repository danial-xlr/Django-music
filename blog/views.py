from django.shortcuts import render,get_object_or_404,redirect

from .models import Profile
from .models import Song, Comment

from .forms import SongForm,CommentForm

def profile_detail(request,id,slug):
    profile = get_object_or_404(Profile, id=id, slug=slug)
    songs = Song.objects.filter(user=profile.user)
    return render(request, 'blog/profile_detail.html', {'profile': profile, 'songs': songs})

def home(request):
    all_songs = Song.objects.order_by('-created')
    return render(request, 'blog/home.html', {'all_songs': all_songs})

def song_detail(request, id, slug):
    song = get_object_or_404(Song, id=id, slug=slug)
    return render(request, 'blog/song_detail.html', {'song': song})

def upload_music(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user
            song.slug=""
            song.save()
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'blog/upload_music.html', {'form': form})

def song_detail(request, id, slug):
    song = get_object_or_404(Song, id=id, slug=slug)
    comments = Comment.objects.filter(song=song)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.song = song
                comment.user = request.user
                comment.save()
                return redirect('song_detail', id=id, slug=slug)
        else:
            return redirect('login')  # Redirect to login page if user is not authenticated
    else:
        form = CommentForm()
    return render(request, 'blog/song_detail.html', {'song': song, 'comments': comments, 'form': form})