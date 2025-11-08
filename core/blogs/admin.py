from django.contrib import admin
from .models import Blogs,Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=('title','author','status','published_at')
    #list_filter=('status','category','published_at')
   # search_fields=('title','author__email','content')

admin.site.register(Blogs,BlogAdmin)
admin.site.register(Category)