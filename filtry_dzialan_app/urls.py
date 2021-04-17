from django.urls import path
from . import views

app_name = 'filtry_dzialan_app'

urlpatterns = [
	path('', views.api_overview, name='api-overview'),
	path('program-details/<str:pk>/', views.get_program_details, name='program-details'),
	path('programs-list/', views.ProgramsView.as_view(), name='programs-list'),
	path('action_filter/', views.FtdElementyView.as_view(), name='action_filter'),
]