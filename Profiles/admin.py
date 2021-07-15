from django.contrib import admin

from Profiles.models import Profile


# Register your models here.
@admin.register(Profile)
class MyAdmin(admin.ModelAdmin):
    pass
