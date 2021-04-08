from django.urls import path
from . import views

app_name = 'filtry_dzialan_app'

urlpatterns = [
	path('', views.api_overview, name='api-overview'),
	path('program-details/<str:pk>/', views.get_program_details, name='program-detail'),
	path('programs-list/', views.get_all_programs, name='programs-list'),
	path('add_action_filter/', views.add_action_filter_with_structure, name='add_action_filter'),
	path('update_action_filter/', views.update_action_filter_with_structure, name='update_action_filter'),
]