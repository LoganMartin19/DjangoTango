from django.views import generic
from .models import NewsArticle

class NewsArticleList(generic.ListView):
    queryset = NewsArticle.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class NewsArticleDetail(generic.DetailView):
    model = NewsArticle
    template_name = 'news_detail.html'

