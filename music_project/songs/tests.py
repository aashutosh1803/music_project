import json

from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Song
from .views import list_songs, get_song_by_title, rate_song

class TestSongs(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Song.objects.bulk_create([
            Song(id="5vYA1mW9g2Coh1HUFUSmlb", title="3AM"),
            Song(id="2klCjJcucgGQysgH170npL", title="4 Walls"),
        ])

    def test_all_songs_pagination(self):
        request = self.factory.get(reverse('list_songs'), {'page': 1, 'limit': 2})
        response = list_songs(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['songs']), 2)
        self.assertEqual(data['total_items'], 2)
        self.assertEqual(data['current_page'], 1)

    def test_song_details(self):
        song_title = '3AM'
        request = self.factory.get(reverse('get_song_by_title', args=[song_title]))
        response = get_song_by_title(request, song_title)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['title'], '3AM')

    def test_rate_song(self):
        request = self.factory.post(
            reverse('rate_song', args=['5vYA1mW9g2Coh1HUFUSmlb']),
            {'rating': 5},
        )
        response = rate_song(request, '5vYA1mW9g2Coh1HUFUSmlb')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['message'], 'Rating updated successfully')
        song = Song.objects.filter(id="5vYA1mW9g2Coh1HUFUSmlb").first()
        self.assertEqual(song.rating, 5.0)