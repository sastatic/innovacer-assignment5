from django.urls import path
from . import views

app_name = 'q5'

urlpatterns = [
	path('', views.index, name='index'),
	path('subscribe/', views.subscription, name='subscription'),
]
