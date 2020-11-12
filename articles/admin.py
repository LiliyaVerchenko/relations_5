from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from articles.models import Article, Relationship, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            dict = form.cleaned_data
            if not dict.get('main_bool'):
                continue
            elif dict['main_bool'] is True:
                i += 1
        if i == 0:
            raise ValidationError('Укажите основной раздел')
        elif i > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Scope)
class ArticleAdmin(admin.ModelAdmin):
    pass
