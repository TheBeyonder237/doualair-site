from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles/list.html", {"articles": articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "articles/detail.html", {"article": article})


def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("article_list")
    else:
        form = ArticleForm()
    return render(request, "articles/form.html", {"form": form})


def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article_detail", pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, "articles/form.html", {"form": form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("article_list")
    return redirect("article_list")
