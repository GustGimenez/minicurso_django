from django.urls import path
from . import views

# Caminho, view a ser chamada, e nome que daremos
urlpatterns = [
	path('', views.post_list, name='post_list')
]