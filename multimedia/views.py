from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from multimedia.tasks import process_video


# Create your views here.

class VideoClipAPI(APIView):
    def post(self, request):
        try:
            data=request.data
            media_dir = "/home"
            video_file_path = media_dir + data['video_file']
            clip_path = media_dir + data['clip_name']
            process_video.delay(video_file_path, data, clip_path)
            data, st, msg = clip_path, 200, "Video clipped successfully"
        except Exception as error:
            print(error)
            data, st, msg = "", 500, "Error while clipping the video"
        resp_json = {"data":data, "st":st, "msg":msg}
        return Response(resp_json)





