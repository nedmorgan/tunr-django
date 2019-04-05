from django.shortcuts import render, redirect
from .models import Artist, Song
from .forms import ArtistForm
from .forms import SongForm

# Create your views here.

# Artist Functions


def artist_index(request):
    context = {'artists': Artist.objects.all()}
    return render(request, 'tunr/artist_index.html', context)


def artist_show(request, pk):
    context = {'artist': Artist.objects.get(pk=pk)}
    return render(request, 'tunr/artist_show.html', context)


def artist_new(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_index')
    else:
        form = ArtistForm()
    return render(request, 'tunr/artist_form.html', {'form': form})


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


def song_new(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('song_index')
    else:
        form = SongForm()
    return render(request, 'tunr/song_form.html', {'form': form})


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


def song_delete(request, pk):
    Song.objects.get(pk=pk).delete()
    return redirect('song_index')
