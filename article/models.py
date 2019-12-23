from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Author")    # istedigimiz isimde gosterilsin istiyorsak parantez bitmeden ,verbose_name="Yazar" diyebiliriz ve admin sayfasinda degismis oldugunu goruruz. bunu diger basliklar icinde yapabiliriz.
    title = models.CharField(max_length=50, verbose_name="Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now=True, verbose_name="Created Date")            # eklenen makale icin otomatik tarih eklesin
    article_image = models.FileField(default="default", blank=True, null=True, verbose_name="Add Photo for Article")
    def __str__(self):       # baslik ve diger yazilarin admin kanalinda gorunsun istiyorsak bu fonksiyonu yapmaliyiz
        return self.title

    class Meta:
        ordering = ['-created_date']                  # goruntude islem sirasi

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE, verbose_name="Article", related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="Name")
    comment_content = models.CharField(max_length=200, verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date']
