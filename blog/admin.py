from django.contrib import admin
from blog.models import Post , category , comments
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class Postadmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-"
    list_display = ["id","title","author","status","content_view" , "poblished_date","created_date"]
    list_filter = ["status","author","created_date"]
    #ordering = ["created_date"]
    search_fields = ["title" ,"content"]
    summernote_fields = ("content")

class commentsADMIN(admin.ModelAdmin ):
    pass

admin.site.register(comments,commentsADMIN)
admin.site.register(category)
admin.site.register(Post , Postadmin)