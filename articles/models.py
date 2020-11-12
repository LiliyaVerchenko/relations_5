from django.db import models

class Scope(models.Model):
    topic = models.CharField(max_length=50, verbose_name='Тема')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.topic

class Relationship(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='relations')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)
    main = models.BooleanField(default=False, verbose_name='Основной')

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField(Scope, related_name='articles', through='Relationship', through_fields=('article', 'scope', 'main'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
