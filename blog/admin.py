from django.contrib import admin
from blog.models import Post
# Register your models here.

class Postadmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-"
    list_display = ["id","title","status","content_view" , "poblished_date","created_date"]
    list_filter = ["status","created_date"]
    #ordering = ["created_date"]
    search_fields = ["title" ,"content"]

admin.site.register(Post , Postadmin)