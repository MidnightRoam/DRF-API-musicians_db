from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Genre(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    url = models.URLField(verbose_name='URL', max_length=255)

    def __str__(self):
        return self.title


class Musician(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Last name', max_length=255, blank=True)
    nickname = models.CharField(verbose_name='Nickname', max_length=255, blank=True, db_index=True)
    content = models.TextField(blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='Age', blank=True)
    city = models.CharField(verbose_name='City', max_length=124, blank=True)
    country = models.CharField(verbose_name='Country', max_length=124, blank=True)
    image = models.ImageField(verbose_name='Image', blank=True)
    is_published = models.BooleanField(verbose_name='Is published', default=True)
    genre = models.ManyToManyField('Genre', verbose_name='Genres of music', blank=True)
    songs = models.ManyToManyField('Song', verbose_name='Songs', blank=True)
    post_author = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    verbose_name='Author of post',
                                    default=User,
                                    related_name='my_posts')
    listeners = models.ManyToManyField(User,
                                       through='UserFavoriteMusicians',
                                       related_name='musicians')

    def __str__(self):
        return self.nickname


class UserFavoriteMusicians(models.Model):
    class Rate(models.IntegerChoices):
        """Rating choices class"""
        Awesome = 5
        Good = 4
        Ok = 3
        Meh = 2
        Bad = 1

    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_favorite = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=Rate.choices, null=True)

    class Meta:
        verbose_name_plural = "User musicians rating"

    def __str__(self):
        return f'{self.user}: {self.musician}: {self.rate}'


class UserSongRelation(models.Model):
    class Rate(models.IntegerChoices):
        """Rating choices class"""
        Awesome = 5
        Good = 4
        Ok = 3
        Meh = 2
        Bad = 1

    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_favorite = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=Rate.choices, null=True)

    def __str__(self):
        return f'{self.user}: {self.song}: {self.rate}'

    class Meta:
        verbose_name_plural = 'User songs rating'
