from django.urls import path
from .views import list_songs,get_song_by_title, rate_song

urlpatterns = [
    path('v1/songs/', list_songs, name='list_songs'),
    path('v1/songs/title/<title>/', get_song_by_title, name='get_song_by_title'),
    path('v1/songs/<song_id>/rate/', rate_song, name='rate_song'),
]
