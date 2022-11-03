from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from musicplaylist.models import Music, PlayList
from musicplaylist.serializers import MusicSerializer, PlayListCustomSerializer, PlayListSerializer, PlayListRecommendCreateSerializer, PlayListCreateSerializer


# Create your views here.
# 테스트용 전체 음악 DB 보기 API
class MusicListview(APIView):
    def get(self, request):
        musics = Music.objects.all( )
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MusicSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 1. API 선호하는 음악 선택 
class MusicPlayListUserSelect(APIView):
    def get(self, request, user_id):
        musicplaylist100 = Music.objects.all()
        music_serializer = MusicSerializer(musicplaylist100, many=True)
        return Response(music_serializer.data)


    def post(self, request, user_id):
        print(request.user)
        user_musicplaylist_create_serializer = PlayListRecommendCreateSerializer(data = request.data)
        if user_musicplaylist_create_serializer.is_valid(): 
            user_musicplaylist_create_serializer.save(playlist_user=request.user)
            return Response(user_musicplaylist_create_serializer.data)
        else:
            return Response(user_musicplaylist_create_serializer.errors)

# 2 API 추천 플레이리스트 (추후 변동 예정 - 추천 플레이리스트를 갖고 오는것으로)
class MusicPlayListUserRecommended(APIView):
    def get(self, request, user_id):
        user_musicplaylist = PlayList.objects.all()
        user_musicplaylist_recommend_serializer = PlayListSerializer(user_musicplaylist, many=True)
        return Response(user_musicplaylist_recommend_serializer.data)




# 3. 유저 커스텀 플레이 리스트
class PlayListview(APIView):
    def get(self, request):
        playlist = PlayList.objects.all( )
        serializer = PlayListCustomSerializer(playlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlayListCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(playlist_user = request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  

# 3. 유저 커스텀 플레이 리스트 수정 및 삭제
class PlayListDetailview(APIView):
    # 본인 게시글 가져오기
    def get(self, request, playlist_id):
        playlist = get_object_or_404(PlayList, id=playlist_id)
        serializer = PlayListCustomSerializer(playlist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, playlist_id):
        playlist = get_object_or_404(PlayList, id=playlist_id)
        if request.user == playlist.playlist_user:
            serializer = PlayListCreateSerializer(playlist, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)



    def delete(self, request, playlist_id):
        playlist = get_object_or_404(PlayList, id=playlist_id)
        print(playlist.playlist_user)
        if request.user == playlist.playlist_user:
            playlist.delete()
            return Response("삭제 완료", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)

