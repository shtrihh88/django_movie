from django.urls import path
from .views import MovieView, MovieDetailView, AddReview, ActorDetailView, FilterMoviesView

urlpatterns = [
    path('filter/', FilterMoviesView.as_view(), name='filter_movies'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', ActorDetailView.as_view(), name='actor_detail'),
    path('', MovieView.as_view()),
]
