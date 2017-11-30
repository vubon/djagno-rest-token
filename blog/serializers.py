from rest_framework import serializers
from .models import Author, Article


class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):

        return Author.objects.create(**validated_data)

    class Meta:
        model = Author
        fields = '__all__'


# class ArticleSerializers(serializers.ModelSerializer):
#     title = serializers.CharField()
#     details = serializers.CharField()
#     author = AuthorSerializer()
#
#     def create(self, validated_data):
#         """
#         Create and return a new 'Article' instance, given the validated data.
#         """
#         return Article.objects.create(**validated_data)
#
#     class Meta:
#         model = Article
#         fields = '__all__'
