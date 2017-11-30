from django.db import models


# Create your models here.
class ArticleManager(models.Manager):
    @staticmethod
    def create_article(request_data):
        title = request_data['title']
        details = request_data['details']
        author = request_data['author']

        article = Article(
            title=title,
            details=details,
            author_id=author
        )
        article.save()
        message = {"message": "Article created successfully!"}
        return message



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)
    author = models.ForeignKey(Author)
    objects = ArticleManager()

    def __str__(self):
        return self.title + " | " + str(self.author)
