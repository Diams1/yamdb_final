from django.db import models

from titles.validators import validate_year


class Title(models.Model):
    """Произведения"""
    name = models.CharField(
        verbose_name='Наименование', max_length=255, db_index=True
    )
    year = models.IntegerField(
        verbose_name='Год выпуска', validators=[validate_year], db_index=True
    )
    description = models.TextField(
        verbose_name='Описание', blank=True, null=True
    )
    category = models.ForeignKey(
        'titles.Category',
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles'
    )
    genre = models.ManyToManyField(
        'Genre',
        verbose_name='Жанр',
        blank=True,
        related_name='titles')

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категории"""
    name = models.CharField(
        verbose_name='Наименование', max_length=256, db_index=True
    )
    slug = models.SlugField(verbose_name='Slag', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Жанры"""
    name = models.CharField(
        verbose_name='Наименование', max_length=255, db_index=True
    )
    slug = models.SlugField(verbose_name='Slag', unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
