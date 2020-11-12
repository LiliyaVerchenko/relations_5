from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Relationship, Scope


def articles_list(request):
    template = 'articles/news.html'
    context = {'object_list': Article.objects.all().order_by('-published_at')}
    return render(request, template, context)
