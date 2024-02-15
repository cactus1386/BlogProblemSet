from django.db import models
from django.utils import timezone

# TODO write all of your code here...
class Author(models.Model):
    name = models.CharField(max_length=50)

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        blog = BlogPost.objects.get(pk=self.pk)
        blog.id = None
        blog.date_created = timezone.now()
        blog.save()

        comments = self.commet_set.all()
        for comment in comments:
            comment.id = None
            comment.blog_post = blog
            comment.save()

        return blog.id

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)