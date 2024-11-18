from django.contrib import admin
from .models import Client, Project

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', 'created_at')  # Fields to display in the admin list view
    search_fields = ('name',)  # Enables searching by client name
    list_filter = ('created_at',)  # Adds filtering by creation date


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'client', 'created_by', 'created_at')  # Fields to display in the admin list view
    search_fields = ('name',)  # Enables searching by project name
    list_filter = ('created_at', 'client')  # Adds filtering by creation date and client
