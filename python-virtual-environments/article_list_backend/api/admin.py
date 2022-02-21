from django.contrib import admin
from .models import Article

# Register your models here.

# #step-5a (first way)
# admin.site.register(Article) # and import above
# # then create article in admin interface (chrome) & go to models.py

#step-5 (don't forget import above)
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_display = ('title', 'link', 'description')
    # after this you can see the title, link & description display on the admin interface page

    list_filter = ('title', 'link', 'description')