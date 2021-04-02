from django.urls import path

from .views import inicio, registro, loginView, logout_vista

urlpatterns = [
	
	path('', inicio, name='inicio'),
	path('login/', loginView, name='login'),
	path('logout_vista/', logout_vista, name='logout_vista'),
	path('registro/', registro, name='registro'),

]