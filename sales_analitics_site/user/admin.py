from django.contrib import admin

# Register your models here.
from sales_analitics_site.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
