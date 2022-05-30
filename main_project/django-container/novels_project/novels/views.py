import imp
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

from novels.models import Author, Novel

from novels.serializers import AuthorSerializer, NovelSerializer

from rest_framework import status, viewsets
from rest_framework.response import Response

class AuthorViewSet(viewsets.ViewSet):
    __queryset__ = Author.objects.all()

    def list(self, request):
        serializer = AuthorSerializer(self.__queryset__)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        
        if serializer.is_valid():
            author = Author()
            author.name = serializer.validated_data["name"]
            author.bio = serializer.validated_data["bio"]
            author.country = serializer.validated_data["country"]
            author.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        author = None
        try:
            author = get_object_or_404(self.__queryset__, pk=pk)
        except:
            pass
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = NovelSerializer(data=request.data)
        
        if serializer.is_valid():
            novel = Novel()
            novel.title = serializer.validated_data["title"]
            novel.original_title = serializer.validated_data["original_title"]
            novel.description = serializer.validated_data["description"]
            novel.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        novel = None
        try:
            novel = get_object_or_404(self.__queryset__, pk=pk)
        except:
            pass
        serializer = NovelSerializer(novel)
        return Response(serializer.data)

class NovelViewSet(viewsets.ViewSet):
     __queryset__ = Novel.objects.all()

    def list(self, request):
        serializer = NovelSerializer(self.__queryset__)
        return Response(serializer.data)

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
            novel = Novel.objects.get(id=novel_id)
            return JsonResponse({"id": novel.id, "title": novel.title, "original_title": novel.original_title, "author": novel.author_id})
        except Novel.DoesNotExist:
            return JsonResponse({"Error"})

    elif request.method == "POST":

        title = request.GET.get("title", None)
        original_title = request.GET.get("original_title", None)
        author = request.GET.get("author", None)
        description = request.GET.get("description", None)

        if not title:
            return JsonResponse({"status": "Bad name param"})

        try:
            novel = Novel

            novel.title = title
            novel.original_title = original_title
            novel.description = description
            novel.author = author

            try:
                _ = Novel.objects.get(title=title, original_title=original_title, author=author, description=description)
            except Novel.DoesNotExist:
                novel.save()
                return JsonResponse({"status": "OK"})
            except Novel.MultipleObjectsReturned:
                return JsonResponse({"status": "Already exists"})
        except:
            return JsonResponse({"status": "Field error"})

    else:
        return HttpResponseBadRequest("<h2>400 Bad Request</h2>")
