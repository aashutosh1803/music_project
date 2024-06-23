Data Can Be loaded by using commnand - python manage.py load_data -data_path D:\projects\pythonProject\music_project\songs\data\playlist.json

We have used django inbuilt SQLite DB to normalise and save the data

All the APIs exist in music_project/songs/views.py .Following APIs has been written
1. Get All Songs in Paginated Way
2. Get Specific Song based on song title
3. Providing Rating to song

Unit test of above APIs has been written in music_project/songs/tests.py
