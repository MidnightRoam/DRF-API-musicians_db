from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import SongsViewSet, MusicianViewSet, UserMusicianRelationsView

app_name = "musicians"

router = SimpleRouter()
router.register(r'all', MusicianViewSet, basename='all')
router.register(r'songs', SongsViewSet, basename='songs')
router.register(r'musician_relation', UserMusicianRelationsView, basename='rate')

urlpatterns = [
    # path('all/', MusicianAPIList.as_view(), name='list'),
    # path('detail/<int:pk>/', MusicianAPIDetail.as_view(), name='detail'),
    # path('songs/', SongsViewSet.as_view()),
]

urlpatterns += router.urls
