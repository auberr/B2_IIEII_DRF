from rest_framework import serializers
from musicplaylist.models import Music, PlayList

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        
        
class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = '__all__'

class PlayListRecommendCreateSerializer(serializers.ModelSerializer):
    playlist_user = serializers.SerializerMethodField()

    def get_playlist_user(self, obj):
        return obj.playlist_user.id

    class Meta:
        model = PlayList
        fields = ("playlist_select_musics", "playlist_user")


class PlayListCustomSerializer(serializers.ModelSerializer):
    playlist_user = serializers.SerializerMethodField()
    playlist_likes = serializers.SerializerMethodField()

    def get_playlist_user(self, obj):
        return obj.playlist_user.id

    def get_playlist_likes(self, obj):
        return obj.playlist_likes.count()

    class Meta:
        model = PlayList
        fields = ("pk", "playlist_title", "playlist_select_musics", "playlist_update_at", "playlist_user", "playlist_likes")



class PlayListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = ("playlist_title", "playlist_select_musics","playlist_content")




