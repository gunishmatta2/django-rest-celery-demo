from django.urls import path

from multimedia.views import VideoClipAPI

urlpatterns = [
    path("clip_video/", VideoClipAPI.as_view())
]