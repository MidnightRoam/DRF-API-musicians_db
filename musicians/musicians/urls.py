from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import MusicianAPIList, MusicianAPIDetail, SongsApiList, MusicianViewSet

app_name = "musicians"

router = SimpleRouter()
router.register(r'all', MusicianViewSet, basename='all')

urlpatterns = [
    # path('all/', MusicianAPIList.as_view(), name='list'),
    path('detail/<int:pk>/', MusicianAPIDetail.as_view(), name='detail'),
    path('songs/', SongsApiList.as_view()),
]

urlpatterns += router.urls
