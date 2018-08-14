from django import template

register = template.Library()

from article.models import ArticlePost, Comment
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()

@register.simple_tag
def author_total_articles(user):
    return user.article.count()

@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by("-created")[:n]
    return {"latest_articles": latest_articles}

@register.simple_tag
def most_commented_articles(n=3):
    # a = ArticlePost.objects.get(id=11).comments.all()
    # b = Comment.objects.filter(article_id=11)
    # print(a)
    # print(b)
    return ArticlePost.objects.annotate(total_comments=Count('comments'))\
        .order_by("-total_comments")[:n]
@register.filter(name='markdown')
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))




