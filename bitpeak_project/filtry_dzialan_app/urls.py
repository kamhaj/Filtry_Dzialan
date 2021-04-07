from django.urls import path
from . import views

app_name = 'filtry_dzialan_app'

urlpatterns = [
	path('programs/', views.get_all_programs, name='filtry_dzialan_app'),
	path('add_filter/', views.add_action_filter_with_structure, name='filtry_dzialan_app'),
	path('update_filter/', views.update_action_filter_with_structure, name='filtry_dzialan_app'),
]