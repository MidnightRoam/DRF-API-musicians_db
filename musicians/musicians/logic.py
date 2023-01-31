from django.db.models import Avg

from .models import UserFavoriteMusicians


def set_rating(musician):
    """Set musician rating"""
    rating = UserFavoriteMusicians.objects.filter(musician=musician).aggregate(rating=Avg('rate')).get('rating')
    musician.rating = rating
    musician.save()
