from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie
from .forms import ReviewForm


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


class MovieDetailView(DetailView):
    """Description movie"""

    model = Movie
    slug_field = 'url'


class AddReview(View):
    """Add review"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)  # second method
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            # form.movie_id = pk
            form.save()
        return redirect(movie.get_absolute_url())
