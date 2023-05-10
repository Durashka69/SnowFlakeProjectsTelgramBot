from django.contrib import admin
from .models import Project, Appeal


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    search_fields = ("title",)


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name",)
