from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Actor, Genre, Movie
from .forms import ReviewForm


class GenresYears:
    """Genres and release dates"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MovieView(GenresYears, ListView):
    """List Movies"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)

    # def get_context_data(self, *args, **kwargs):  # вся обработка через template_tag
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class MovieDetailView(GenresYears, DetailView):
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


class ActorDetailView(GenresYears, DetailView):
    """Bio actor or director"""

    model = Actor
    slug_field = 'name'


class FilterMoviesView(GenresYears, ListView):
    """Filter movies"""

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        )
        print(queryset)
        return queryset
