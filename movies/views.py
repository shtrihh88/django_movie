from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie


# class MovieView(View):
#     """List Movies"""
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'movies/movie_list.html', {'movie_list': movies})


# class MovieDetailView(View):
#     """Description movie"""
#
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'movies/movie_detail.html', {'movie': movie})


class MovieView(ListView):
    """List Movies"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = 'movies/movies.html'


class MovieDetailView(DetailView):
    """Description movie"""

    model = Movie
    slug_field = 'url'
