import os
import json
from django.core.management.base import BaseCommand
from songs.models import Song

FILE_TABLE_COL_MAP = {
    'class': 'song_class',
}

class Command(BaseCommand):
    help = 'Load songs data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('-data_path', '--data_input_path', type=str, help='Input Path for Data')

    def _convertToRowForm(self, json_data):
        song_map = {}
        for song_property in json_data:
            for id in json_data[song_property]:
                if id not in song_map:
                    song_map[id] = {}
                song_map[id][song_property] = json_data[song_property][id]
        return song_map

    def _insertDataToDB(self, json_data):
        try:
            fields = [field.name for field in Song._meta.get_fields()]
            song_map = self._convertToRowForm(json_data)
            songs_list = song_map.values()
            song_db_objects = []

            for song in songs_list:
                song_obj = Song()
                for property in song:
                    col_name = property
                    if property in FILE_TABLE_COL_MAP:
                        col_name = FILE_TABLE_COL_MAP[property]

                    if col_name in fields:
                        setattr(song_obj, col_name, song[property])

                song_db_objects.append(song_obj)

            Song.objects.bulk_create(song_db_objects)
            print("Songs Insertion Done")

        except Exception as e:
            print("Unable to insert in DB due to {}".format(e))

    def handle(self, *args, **kwargs):
        file_path = kwargs['data_input_path']
        with open(file_path, 'r') as file:
            data = json.load(file)
            self._insertDataToDB(json_data=data)