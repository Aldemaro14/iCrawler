from django.contrib import admin
from .models import ScrapyItem

class ScrapyItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScrapyItem, ScrapyItemAdmin)
