from django.contrib import admin
from .import models


# Register your models here.
# Type pass to not have any additional configurations for this module
class NotesAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title')

admin.site.register(models.Notes, NotesAdmin)