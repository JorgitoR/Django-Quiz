from django.urls import path

from .views import inicio, registro, loginView, logout_vista, HomeUsuario, jugar

urlpatterns = [
	
	path('', inicio, name='inicio'),
	path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),


	path('login/', loginView, name='login'),
	path('logout_vista/', logout_vista, name='logout_vista'),
	path('registro/', registro, name='registro'),

	
	path('jugar/', jugar, name='jugar'),

]