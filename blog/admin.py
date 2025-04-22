from django.contrib import admin
from blog.models import Post , category , Comments
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class Postadmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-"
    list_display = ["id","title","author","status","login_require","content_view" , "poblished_date","created_date"]
    list_filter = ["status","author","created_date"]
    #ordering = ["created_date"]
    search_fields = ["title" ,"content"]
    summernote_fields = ("content")

class commentsADMIN(admin.ModelAdmin ):
    date_hierarchy = "created_date"
    list_display = ["name","post","approved","email"]
    search_fields = ["name" , "subect"]
    list_filter = ["approved"]
    empty_value_display = "-"


admin.site.register(Comments,commentsADMIN)
admin.site.register(category)
admin.site.register(Post , Postadmin)