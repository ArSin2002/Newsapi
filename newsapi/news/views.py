from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
from django.views.decorators.http import require_POST

from news.util import is_api_call_required
from news.const import API_CALLED_WITH_SAME_PARAMETER, ARTICLE_NOT_FOUND, NEWS_API_KEY


def index(request):
    return render(request, "index.html")


@require_POST
def res(request):
    data = {
        "q": request.POST["keyword"],
        "country": request.POST["country"],
        "category": request.POST["categories"],
    }
    max_page = int(request.POST["page_size"])
    if is_api_call_required(data):
        try:
            res = urllib.request.urlopen(
                "https://newsapi.org/v2/top-headlines?q="
                + data["q"]
                + "&country="
                + data["country"]
                + "&category="
                + data["category"]
                + "&apiKey="
                + NEWS_API_KEY
            )
        except Exception as e:
            return HttpResponse(e)
        json_data = json.loads(res.read())
        response = json_data["articles"][:max_page]
        if response == []:
            response = [ARTICLE_NOT_FOUND]

    else:
        response = [API_CALLED_WITH_SAME_PARAMETER]
    return render(request, "index.html", {"response": response})
