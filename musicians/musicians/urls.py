from django.urls import path

from .views import MusicianAPIList, MusicianAPIDetail

app_name = "musicians"
urlpatterns = [
    path('all/', MusicianAPIList.as_view()),
    path('detail/<int:pk>/', MusicianAPIDetail.as_view())
]
