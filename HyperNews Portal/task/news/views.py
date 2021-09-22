from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.shortcuts import redirect
from collections import defaultdict
from django.http import HttpResponse
import datetime
import random
import json

class NewsView(View):
    """Load news.json and pass it to render when domain/news/ is accessed. If search form is used, only searches that
    are contained in the title of the news are passed to render"""
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_file:
            news_from_json = json.load(json_file)

        context = {}
        q = request.GET.get('q')
        if q is None:
            context["news"] = news_from_json
        else:
            news_from_json_search = []
            for news in news_from_json:
                if q in news['title']:
                    news_from_json_search.append(news)
            context["news"] = news_from_json_search

        return render(request, "news/index.html", context)


class LinkView(View):
    """If user clicks on the news link it pass to render the correspondent news"""
    def get(self, request, link, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_file:
            news_from_json = json.load(json_file)
        for new in news_from_json:
            if new['link'] == int(link):
                context = {"new": new}
                return render(request, "news/link.html", context=context)


class CreateNews(View):
    """When accessed by GET render the page with the form to create news. When the form is send by POST, it includes
    the new news on news.json and redirects to /news/"""
    def get(self, request, *args, **kwargs):
        return render(request, "news/createnews.html")

    def post(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r") as json_file:
            news_from_json = json.load(json_file)

        news_title = request.POST.get('title')
        news_text = request.POST.get('text')
        date_time = datetime.datetime.now()
        news_created = date_time.strftime("%Y-%m-%d %H:%M:%S")
        news_link = random.randint(1, 9_999_999)

        for i in news_from_json:
            while True:
                if news_link == i["link"]:
                    news_link = random.randint(1, 9_999_999)
                else:
                    break

        news_dict = defaultdict()
        news_dict["created"] = news_created
        news_dict["text"] = news_text
        news_dict["title"] = news_title
        news_dict["link"] = news_link
        news_from_json.append(news_dict)

        with open(settings.NEWS_JSON_PATH, "w") as json_file:
            json.dump(news_from_json, json_file)

        return redirect('/news/')





