from django.urls import path
from .views import MovieView, MovieDetailView, AddReview

urlpatterns = [
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),
    path('', MovieView.as_view()),
]
