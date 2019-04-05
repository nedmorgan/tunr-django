from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Artist, Song
from .forms import ArtistForm
from .forms import SongForm

# Create your views here.

# Log-in function


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('artist_index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Artist Functions


def artist_index(request):
    context = {'artists': Artist.objects.all()}
    return render(request, 'tunr/artist_index.html', context)


def artist_show(request, pk):
    context = {'artist': Artist.objects.get(pk=pk)}
    return render(request, 'tunr/artist_show.html', context)


@login_required
def artist_new(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_index')
    else:
        form = ArtistForm()
    return render(request, 'tunr/artist_form.html', {'form': form})


@login_required
def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_show', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_form.html', {'form': form})


@login_required
def artist_delete(request, pk):
    Artist.objects.get(pk=pk).delete()
    return redirect('artist_index')

# Song Functions


def song_index(request):
    context = {'songs': Song.objects.all()}
    return render(request, 'tunr/song_index.html', context)


def song_show(request, pk):
    context = {'song': Song.objects.get(pk=pk)}
    return render(request, 'tunr/song_show.html', context)


@login_required
def song_new(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('song_index')
    else:
        form = SongForm()
    return render(request, 'tunr/song_form.html', {'form': form})


@login_required
def song_edit(request, pk):
    song = Song.objects.get(pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save()
            return redirect('song_show', pk=song.pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'tunr/song_form.html', {'form': form})


@login_required
def song_delete(request, pk):
    Song.objects.get(pk=pk).delete()
    return redirect('song_index')
