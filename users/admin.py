from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_active', 'is_staff')
