from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from musicplaylist.models import Music, MusicPlayList
from musicplaylist.serializers import MusicSerializer, MusicPlayListSerializer, MusicPlayListCreateSerializer


# Create your views here.

class MusicPlayListUserSelect(APIView):
    def get(self, request, user_id):
        musicplaylist100 = Music.objects.all()
        music_serializer = MusicSerializer(musicplaylist100, many=True)
        return Response(music_serializer.data)

    def post(self, request, user_id):
        print(request.user)
        user_musicplaylist_create_serializer = MusicPlayListCreateSerializer(data = request.data)
        if user_musicplaylist_create_serializer.is_valid(): 
            user_musicplaylist_create_serializer.save(music_playlist_user=request.user)
            return Response(user_musicplaylist_create_serializer.data)
        else:
            return Response(user_musicplaylist_create_serializer.errors)

class MusicPlayListUserRecommended(APIView):
    def get(self, request, user_id):
        user_musicplaylist = MusicPlayList.objects.all()
        user_musicplaylist_recommend_serializer = MusicPlayListSerializer(user_musicplaylist, many=True)
        return Response(user_musicplaylist_recommend_serializer.data)