from django.shortcuts import render
from django.http import HttpResponse
from .fetchingbot import getnewposts
from .models import Videos
from .serializer import VideosSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Create your views here.


def fetch_new_posts(request):
    try:
        getnewposts()
        return HttpResponse("Refresh Localhost to view newly added videos")
    except:
        return HttpResponse("An error was encountered")


class VideoList(generics.ListAPIView):
    queryset = Videos.objects.all()
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)

    # Search and filter fields added
    search_fields = ['title']
    filter_fields = ['channelTitle']

    # Sorting the videos' data in reverse chronological order by default
    ordering = ['-publishingDateTime']
    serializer_class = VideosSerializer
    pagination_class = PageNumberPagination
