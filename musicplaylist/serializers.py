from rest_framework import serializers
from musicplaylist.models import Music, PlayList

# 테스트용 전체 음악 DB 보기 API 에서 쓰이는 Seriazlier
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
   
# 테스트용  Seriazlier

class MusicTestSerializer(serializers.ModelSerializer):
    playlist_user = serializers.SerializerMethodField()

    def get_playlist_user(self, obj):
        return obj.playlist_user.id

    class Meta:
        model = PlayList
        fields = ("playlist_select_musics", "playlist_user")


# 1. API - 선호하는 음악 선택에서 플레이리스트 create 만드는 것
class PlayListRecommendCreateSerializer(serializers.ModelSerializer):
    playlist_user = serializers.SerializerMethodField()

    def get_playlist_user(self, obj):
        return obj.playlist_user.id

    class Meta:
        model = PlayList
        fields = ("playlist_select_musics", "playlist_user")


# 2. API - 추천 플레이리스트 에서 쓰이는 Seriazlier
class PlayListRecommendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = '__all__'



# 3,4 API - 유저가 만든 플레이리스트 및 상세 get 용 seriailizer
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


# 3 API - 유저가 만든 플레이리스트 및 상세 create 용 seriailizer
class PlayListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = ("playlist_title", "playlist_select_musics","playlist_content")




