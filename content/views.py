from django.shortcuts import render
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
