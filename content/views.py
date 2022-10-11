from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed


# Create your views here.
class Main(APIView):
    def get(self, request):
        print("called get")
        feed_list = Feed.objects.all().order_by('-id')
        for feed in feed_list:
            print(feed.content)
        return render(request, "unstagram/main.html", context=dict(feed_list=feed_list))


class UploadFeed(APIView):
    def post(self, request):
        file = request.data.get('file')
        image = request.data.get('image')
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.geet('profile_image')


        return Response(status=200)