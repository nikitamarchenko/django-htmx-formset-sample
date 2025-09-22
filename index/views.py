from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArticleFormSet, ArticleForm2Set
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "GET":
        formset = ArticleFormSet(
            initial=[
                {
                    "title": "title",
                    "author": "author",
                }
            ]
        )
        context = {"formset": formset}
        return render(request, "index/index.html", context)
    if request.method == "POST":
        formset = ArticleFormSet(request.POST)
        if not formset.is_valid():
            return render(request, "index/index.html", context = {"formset": formset, "posted": True, "invalid": formset.error_messages})
    
        for f in formset:
            print(f.cleaned_data['title'])
        
        return render(request, "index/index.html", context = {"formset": formset, "posted": True})    

def add_form(request):
    if request.method == "POST":
        formset = ArticleFormSet(request.POST)
        if formset.is_valid():
            d = []
            for form in formset.forms:
                d.append(form.cleaned_data)
            formset = ArticleForm2Set(initial=d)
            context = {
                "formset": formset,
            }
            return render(request, "index/form.html", context)
