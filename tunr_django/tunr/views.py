from django.shortcuts import render, redirect
from .models import Artist, Song
from .forms import ArtistForm

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

# Song Functions


def song_index(request):
    context = {'songs': Song.objects.all()}
    return render(request, 'tunr/song_index.html', context)


def song_show(request, pk):
    context = {'song': Song.objects.get(pk=pk)}
    return render(request, 'tunr/song_show.html', context)
