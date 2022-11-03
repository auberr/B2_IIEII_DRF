from rest_framework import serializers
from musicplaylist.models import Music, MusicPlayList

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        

class MusicPlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicPlayList
        fields = '__all__'

class MusicPlayListCreateSerializer(serializers.ModelSerializer):
    music_playlist_user = serializers.SerializerMethodField()

    def get_music_playlist_user(self, obj):
        return obj.music_playlist_user.id

    class Meta:
        model = MusicPlayList
        fields = ("music_playlist_song", "music_playlist_user")
