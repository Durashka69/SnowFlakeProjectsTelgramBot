from django.db import models

from uuid import uuid4


def generate_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{str(uuid4())}.{ext}"
    return f"{filename}"


class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        upload_to=generate_filename,
        verbose_name='Изображение'
    )
    link = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Appeal(models.Model):
    name = models.CharField(max_length=50, verbose_name='Автор')
    email = models.EmailField(verbose_name='Почта')
    message = models.TextField(verbose_name='Обращение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Связаться с нами'
        verbose_name_plural = 'Связаться с нами'
