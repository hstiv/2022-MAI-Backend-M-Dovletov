from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


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
        novel_id = request.GET.get("film_id", 47)
        name = request.GET.get("name", "Мир боевых искусств")
        genres = request.GET.get("genres", ["Китай", "Боевые искусства", "Гарем"])
        return JsonResponse({"novel_id": novel_id, "name": name, "genres": genres})
    elif request.method == "POST":
        novel_id = request.GET.get("novel_id", 48)
        name = request.GET.get("name", "Моя Вампирская Система")
        genres = request.GET.get("genres", ["Вампиры", "ГГ идиот", "Военный"])
        # в БД
        return JsonResponse({"novel_id": novel_id, "status": "OK"})
    else:
        return HttpResponseBadRequest("<h2>400 Bad Request</h2>")
