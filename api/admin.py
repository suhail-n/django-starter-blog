from django.contrib import admin
from django import forms
from django.forms.fields import MultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

from . import models


class ArticleAdminForm(forms.ModelForm):
    """
    This adds a horizontal filter choice to a many to many relationship

    Explanation: https://stackoverflow.com/questions/11657682/django-admin-interface-using-horizontal-filter-with-inline-manytomany-field

    A little walkthrough is probably in order. First, we define a userprofiles form field. It will use a ModelMultipleChoiceField, which by default will result in a multiple select box. Since this isn't an actual field on the model, we can't just add it to filter_horizontal, so we instead tell it to simply use the same widget, FilteredSelectMultiple, that it would use if it were listed in filter_horizontal.
    We initially set the queryset as the entire UserProfile set, you can't filter it here, yet, because at this stage of the class definition, the form hasn't been instantiated and thus doesn't have it's instance set yet. As a result, we override __init__ so that we can set the filtered queryset as the field's initial value.
    Finally, we override the save method, so that we can set the related manager's contents to the same as what was in the form's POST data, and you're done.


    """
    class Meta:
        model = models.Article
        exclude = ()

    tags = forms.ModelMultipleChoiceField(
        queryset=models.Tag.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Article Tags',
            is_stacked=False,
        )
    )

    def __init__(self, *args, **kwargs):
        super(ArticleAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tags'].initial = self.instance.tags.all()

    def save(self, commit=True):
        # call super.save with commit false to get an instance of the filled out article form. Commit False will prevent save_m2m() (Save the many-to-many fields and generic relations for this form).
        # save_m2m will be added to the instance to be called later
        article = super(ArticleAdminForm, self).save(commit=False)

        # commit will be sent as false by default and article was saved earlier
        if commit:
            article.save()

        # only if article is being saved with a PK meaning a single article.
        if article.pk:
            # now use the tags model 'set' method to replace all the current tags with the new ones from the form
            # cleaned_data refers to the current form data submitted as part of the post request
            article.tags.set(self.cleaned_data['tags'])
            # save_m2m was created when .save(commit=False) was called
            self.save_m2m()

        return article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'owner', 'tags']
    # list_display = ('title', 'content', 'owner')
    list_display = ('title', 'content', 'owner', 'get_tags')
    # filter_horizontal = ['tags']
    # add the new form here to gain the horizontal filter option
    form = ArticleAdminForm

    def get_tags(self, obj):
        return "\n".join([tag.name for tag in obj.tags.all()])


class TagAdmin(admin.ModelAdmin):
    fields = ['name', 'articles']
    list_display = ('name',)
    # inlines = [
    #     ArticleTagInline
    # ]
    filter_horizontal = ['articles']
    # exclude = ('articles',)


admin.site.register(models.Article, ArticleAdmin)
# admin.site.register(models.Article)
admin.site.register(models.Comment)
admin.site.register(models.Tag, TagAdmin)
