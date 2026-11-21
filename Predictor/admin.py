from django.contrib import admin
from .models import Prediction


class PredictionAdmin(admin.ModelAdmin):
    list_display = ('location', 'area', 'bhk', 'estimated_price', 'created_at')


admin.site.register(Prediction, PredictionAdmin)