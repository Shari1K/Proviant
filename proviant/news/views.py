from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from .models import News
from .serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


def get_all_news(request):
    all_news = News.objects.all()
    news_list = []
    for news in all_news:
        news_list.append({
            'image_url': news.image.url,
            'date': news.date.strftime('%Y-%m-%d'),
            'time': news.time.strftime('%H:%M:%S'),
            'title': news.title,
            'content': news.content,
        })
    return JsonResponse({'news': news_list})

# def get_news(request):
