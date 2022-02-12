from django import template
from movies.models import Category, Movie


register = template.Library()


@register.simple_tag()
def get_categories():
    """Get all categories"""
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movies.html')
def get_last_movies(count=5):
    """Get last added movies"""
    movies = Movie.objects.order_by('-id')[:count]
    return {'last_movies': movies}
