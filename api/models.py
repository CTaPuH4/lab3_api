from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=35)

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:35]


class Item(models.Model):
    name = models.CharField('Название', max_length=35)
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание', null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='items',
        verbose_name='Категория',
    )
    image = models.ImageField(
        upload_to='static/images/',
        null=True,
        default=None
    )
    is_published = models.BooleanField('Опубликовано')

    class Meta:
        ordering = ('price',)
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name[:35]
