import os
from googleapiclient.discovery import build

class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        api_key: str = os.getenv('YT_API_KEY')  # API_KEY скопирован из гугла и вставлен в переменные окружения
        youtube = build('youtube', 'v3', developerKey=api_key)  # создать специальный объект для работы с API
        video = youtube.videos().list(part='snippet, statistics', id=self.video_id).execute()['items'][0]['snippet']
        self.title = video['title']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['viewCount'])
        self.like_count = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.title

class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.video_id = video_id
        api_key: str = os.getenv('API_KEY')  # API_KEY скопирован из гугла и вставлен в переменные окружения
        youtube = build('youtube', 'v3', developerKey=api_key)  # создать специальный объект для работы с API
        video = youtube.videos().list(part='snippet, statistics', id=self.video_id).execute()['items'][0]['snippet']
        self.title = video['title']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['viewCount'])
        self.like_count = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.title