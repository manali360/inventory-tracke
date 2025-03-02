from django.contrib import admin
from tracker.models import Contact,Category,Item

class category(admin.ModelAdmin):
    list_display=['name','description']
    search_fields=['created_at']

class item(admin.ModelAdmin):
    list_display=['name','category','quantity','description']
    search_fields=['name']

admin.site.register(Contact)
admin.site.register(Category,category)
admin.site.register(Item,item)
