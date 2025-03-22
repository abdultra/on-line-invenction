from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
]

urlpatterns += [
	path('', include(('home.urls', 'home'), namespace='home')),
	path('paciente/', include(('paciente.urls', 'paciente'), namespace='paciente')),
	path('blood_bank/', include(('blood_bank.urls', 'blood_bank'), namespace='blood_bank')),
	path('estoque/', include(('estoque.urls', 'estoque'), namespace='estoque')),
	path('exame/', include(('exame.urls', 'exame'), namespace='exame')),
	]