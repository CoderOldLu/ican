from django.contrib import admin
from .models import *


# Register your models here.
class VideosInline(admin.StackedInline):
    model = Video
    extra = 3
    filter_horizontal = ('tags',)


class TutorialAdmin(admin.ModelAdmin):
    inlines = [VideosInline]


admin.site.register(Tag)
admin.site.register(Slide)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Commodity)
