from django.db import models
from user.models import User

# Create your models here.

class Music(models.Model):
    music_artist = models.CharField(max_length=25, default='')
    music_title = models.CharField(max_length=255, default='')
    music_genre = models.CharField(max_length=25, default='')
    # music_img = models.ImageField(null=True, upload_to='images/', blank=True, editable=True)

    def __str__(self):
        return str(self.music_title)
    

class PlayList(models.Model):
    playlist_user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_select_musics = models.ManyToManyField(Music, related_name='select_musics_set')
    playlist_title = models.CharField(max_length=50, null=True)
    playlist_content = models.TextField(null=True)
    
    playlist_create_at = models.DateTimeField(auto_now_add=True)
    playlist_update_at = models.DateTimeField(auto_now=True)

    playlist_likes = models.ManyToManyField(User, related_name="playlist_likes_set")

    is_main = models.BooleanField(default = False)
    is_main_recom = models.BooleanField(default = False)

    def __str__(self):
        return str(self.playlist_title)


