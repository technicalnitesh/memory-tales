from django.db import models


class Category(models.Model):

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=200)

    slug = models.SlugField(max_length=200, unique=True)

    description = models.TextField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='category/',
        blank=True,
        null=True
    )

    sort_order = models.IntegerField(default=0)

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "mt_categories"
        ordering = ['sort_order', 'name']

    def __str__(self):
        return self.name