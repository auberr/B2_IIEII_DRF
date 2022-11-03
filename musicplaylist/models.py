from django.db import models
from django.contrib.auth.models import User # 나중에 커스텀 유저를 사용할때 다 바꿔야 된다.

# Create your models here.
class Music(models.Model):
    music_user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_artist = models.CharField(max_length=25)
    music_title = models.CharField(max_length=255)
    music_genre = models.CharField(max_length=25)
    # music_img = models.ImageField(null=True, upload_to='images/', blank=True, editable=True)

    def __str__(self):
        return str(self.music_title)
    

class MusicPlayList(models.Model):
    music_playlist_user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_playlist_song = models.ManyToManyField(Music, related_name='music')

    def __str__(self):
        return str(self.music_playlist_user)
