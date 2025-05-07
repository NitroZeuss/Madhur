from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description')


from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone_number", "event_date", "number_of_guests", "created_at")
    search_fields = ("full_name", "email", "phone_number")
    list_filter = ("event_date", "created_at")
    readonly_fields = ("created_at",)
