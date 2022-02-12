from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Actor, Category, Genre, Movie, MovieShots, Rating,
                     RatingStar, Reviews)

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Desc', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


# class ReviewInLine(admin.StackedInline):
#     model = Reviews
#     extra = 1


class ReviewInLine(admin.TabularInline):
    """Review on movies page"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110">')

    get_image.shot_description = 'Image'


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Actors"""
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Image"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category of movies"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genres of movies"""
    list_display = ('name', 'description', 'url')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Movies"""
    list_display = ('title', 'tagline', 'year', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    # inlines = [MovieShotsInline, ReviewInLine, ]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ('publish', 'unpublish')
    form = MovieAdminForm
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', ('get_image', 'poster'),),
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'),)
        }),
        ('Actors', {
            'classes': ('collapse',),
            'fields': (('actors', 'director', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110">')

    def publish(self, request, queryset):
        """Publish movie"""

        row_update = queryset.update(draft=False)
        if row_update == 1:
            message = '1 запись была обновлена'
        else:
            message = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message}')

    def unpublish(self, request, queryset):
        """Unpublish movie"""

        row_update = queryset.update(draft=True)
        if row_update == 1:
            message = '1 запись была обновлена'
        else:
            message = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message}')

    publish.short_description = 'Publish'
    publish.allowed_permissions = ('change',)

    unpublish.short_description = 'Unpublish'
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = 'Poster'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Frame of movies"""
    list_display = ('title', 'description', 'id_movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.shot_description = 'Image'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Rating movies"""
    list_display = ('ip', 'star', 'movie')


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    """Star rating of movies"""
    list_display = ('value',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Reviews"""
    list_display = ('name', 'email', 'text', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'
