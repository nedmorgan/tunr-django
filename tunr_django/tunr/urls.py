from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_index, name='artist_index'),
    path('artists/new/', views.artist_new, name='artist_new'),
    path('artists/<int:pk>/', views.artist_show, name='artist_show'),
    path('artists/<int:pk>/edit/', views.artist_edit, name='artist_edit'),
    path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
    path('songs/', views.song_index, name='song_index'),
    path('songs/new/', views.song_new, name='song_new'),
    path('songs/<int:pk>/', views.song_show, name='song_show'),
    path('songs/<int:pk>/edit/', views.song_edit, name='song_edit'),
    path('songs/<int:pk>/delete', views.song_delete, name='song_delete'),
]
