from django.urls import path

from .views import SongView

urlpatterns = [path("songs/<int:album_id>/", SongView.as_view())]
