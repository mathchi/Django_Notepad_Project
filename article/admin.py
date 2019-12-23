from django.contrib import admin
from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "created_date"]      # admin panelinde genel gorunumde gorunmesini istedigimiz kisim buraya yaziyoruz
    
    list_display_links = ["title", "created_date"]          # admin panelinde genel gorunumu link seklinde gostertmek icin   
    
    search_fields = ["title"]                               # admin panelinde arama ozelligi olusturmak icin
    
    list_filter = ["created_date"]                          # olusturma tarihine gore filtre olusturmak icin baska biseyede yapabiliiriz
    class Meta:                         # bunu yapma sebebimiz yukardaki article ile baglamaktir
        model = Article

