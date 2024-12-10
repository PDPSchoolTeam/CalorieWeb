from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=100)
    content = models.SlugField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts',
    )

    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.Draft
    )

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['published']),
        ]

    def __str__(self) -> str:
        return self.title


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=[('Food', 'Food'), ('Drink', 'Drink'), ('Dessert', 'Dessert')])

    def __str__(self):
        return self.name