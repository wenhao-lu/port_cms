from django.urls import path
from . import views
from .views import ProjectListAPIView, WorkListAPIView, StackListAPIView, EducationListAPIView


urlpatterns = [
    path('api/projects/', ProjectListAPIView.as_view(), name='project-list-api'),
    path('api/works/', WorkListAPIView.as_view(), name='work-list-api'),
    path('api/stacks/', StackListAPIView.as_view(), name='stack-list-api'),
    path('api/educations/', EducationListAPIView.as_view(), name='education-list-api'),
                       
    path('dashboard/', views.dashboard_view, name='dashboard-view'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('projects/', views.project_list_view, name='project-list'),
    path('projects/add/', views.add_project, name='add-project'),
    path('projects/edit/<int:project_id>/', views.edit_project, name='edit-project'),
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete-project'),

    path('works/', views.work_list_view, name='work-list'),
    path('works/add/', views.add_work, name='add-work'),
    path('works/edit/<int:work_id>/', views.edit_work, name='edit-work'),
    path('works/delete/<int:work_id>/', views.delete_work, name='delete-work'),

    path('stacks/', views.stack_list_view, name='stack-list'),
    path('stacks/add/', views.add_stack, name='add-stack'),
    path('stacks/edit/<int:stack_id>/', views.edit_stack, name='edit-stack'),
    path('stacks/delete/<int:stack_id>/', views.delete_stack, name='delete-stack'),

    path('educations/', views.education_list_view, name='education-list'),
    path('educations/add/', views.add_education, name='add-education'),
    path('educations/edit/<int:education_id>/', views.edit_education, name='edit-education'),
    path('educations/delete/<int:education_id>/', views.delete_education, name='delete-education'),

]