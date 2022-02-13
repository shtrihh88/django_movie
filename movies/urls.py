from django.urls import path
from . import views

urlpatterns = [
    path('filter/', views.FilterMoviesView.as_view(), name='filter_movies'),
    path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),
    path('json-filter/', views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>', views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', views.ActorDetailView.as_view(), name='actor_detail'),
    path('', views.MovieView.as_view()),
]
