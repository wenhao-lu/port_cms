from django.urls import path
from . import views
from .views import ProjectListView


urlpatterns = [
    path('api/projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/', views.project_list_view, name='project-list-ui'),
]