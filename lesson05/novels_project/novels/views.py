import imp
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from novels import models

def index(request):
    http = \
        """
    <html lang="ru">
    <head>
        <title>FooNovels</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></meta>
    </head>
    <body>
        <h1>Hello from FooNovels!</h1>
    </html>
    """
    return HttpResponse(http)

@csrf_exempt
def catalog(request):
    if request.method == "GET":
        novel_id = request.GET.get("novel_id", 1)

        try:
            novel = models.Novel.objects.get(id=novel_id)
            return JsonResponse({"id": novel.id, "title": novel.title, "original_title": novel.original_title, "author": novel.author_id})
        except models.Novel.DoesNotExist:
            return JsonResponse({"Error"})

    elif request.method == "POST":

        title = request.GET.get("title", None)
        original_title = request.GET.get("original_title", None)
        author = request.GET.get("author", None)
        description = request.GET.get("description", None)

        if not title:
            return JsonResponse({"status": "Bad name param"})

        try:
            novel = models.Novel

            novel.title = title
            novel.original_title = original_title
            novel.description = description
            novel.author = author

            try:
                _ = models.Novel.objects.get(title=title, original_title=original_title, author=author, description=description)
            except models.Novel.DoesNotExist:
                novel.save()
                return JsonResponse({"status": "OK"})
            except models.Novel.MultipleObjectsReturned:
                return JsonResponse({"status": "Already exists"})
        except:
            return JsonResponse({"status": "Field error"})

    else:
        return HttpResponseBadRequest("<h2>400 Bad Request</h2>")
