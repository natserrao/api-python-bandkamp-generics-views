from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics


class SongView(generics.ListCreateAPIView, PageNumberPagination):

    serializer_class = SongSerializer
    queryset = Song.objects.all()
    lookup_url_kwarg = "album_id"

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album = self.kwargs.get(self.lookup_url_kwarg)
        return Song.objects.filter(album_id=album)

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get("album_id"))
