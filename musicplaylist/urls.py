from django.urls import path
from musicplaylist import views

urlpatterns = [
    path('<int:user_id>/playlist/select/', views.MusicPlayListUserSelect.as_view(), name='musicplaylistuserselect_view'),
    path('<int:user_id>/playlist/recommended/', views.MusicPlayListUserRecommended.as_view(), name='musicplaylistuserrecommnded_view'),
]