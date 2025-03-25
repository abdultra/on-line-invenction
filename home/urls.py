from django.urls import path
from .views import home


urlpatterns = [
	# Doador
	path('', home, name='home'),
	]