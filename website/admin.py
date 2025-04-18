from django.contrib import admin
from website.models import Contact , Newsletter

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    search_fields = ["email","subject"]
    empty_value_display = "--"
    date_hierarchy = "create_date"
    list_display = ["name" , "subject" , "email" ,"create_date"]
    list_filter = ["email" , "create_date"]
admin.site.register( Contact ,ContactAdmin)
admin.site.register(Newsletter)