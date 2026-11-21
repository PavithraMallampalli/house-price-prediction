from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('result/<int:prediction_id>/', views.result, name='result'),
    path('history/', views.history, name='history'),
]