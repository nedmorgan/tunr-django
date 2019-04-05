from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_index, name='artist_index'),
    path('artists/<int:pk>/', views.artist_show, name='artist_show'),
    path('artists/new/', views.artist_new, name='artist_new'),
    path('artists/<int:pk>/edit/', views.artist_edit, name='artist_edit'),
    path('songs/', views.song_index, name='song_index'),
    path('songs/<int:pk>/', views.song_show, name='song_show'),
    path('songs/<int:pk>/edit/', views.song_edit, name='song_edit'),
    path('songs/new/', views.song_new, name='song_new'),
]
