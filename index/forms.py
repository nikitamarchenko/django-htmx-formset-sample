from django import forms


from django.forms import formset_factory


class ArticleForm(forms.Form):
    CHOICES = [
        (1, "val1"),
        (2, "val2"),
    ]
    title = forms.CharField()
    author = forms.CharField()
    choice = forms.ChoiceField(choices=CHOICES)


ArticleFormSet = formset_factory(ArticleForm, extra=0)
ArticleForm2Set = formset_factory(ArticleForm, extra=1)


def getFactory(extra=0):
    return formset_factory(ArticleForm, extra=extra)
