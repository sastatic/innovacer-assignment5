from django.contrib import admin

# Register your models here.

from .models import series, user, subscription

admin.site.register(series)
admin.site.register(user)
admin.site.register(subscription)