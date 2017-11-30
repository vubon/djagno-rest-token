from .models import Author, Article
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthorSerializer
# Create your views here.


class CreateAuthor(APIView):
    """
        URL: /blog/create-author/
        Method: POST

                {
                    "first_name": "Vubon",
                    "last_name": "Roy"
                }
    """
    def get(self, request, format=None):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewPost(APIView):
    """
        List or create new Article

        {
            "title": "Hello world",
            "details":"this is a test post",
            "author":4
        }
    """
    def post(self, request, format=None):
        request_data = request.data
        result = Article.objects.create_article(request_data)
        return Response(result, status=status.HTTP_201_CREATED)
