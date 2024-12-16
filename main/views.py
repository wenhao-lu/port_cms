from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Work, Stack, Education
from .serializers import ProjectSerializer, WorkSerializer, StackSerializer, EducationSerializer
from .forms import ProjectForm, WorkForm, StackForm, EducationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Authentication
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard/')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')




@login_required
def dashboard_view(request):
    return render(request, 'main/dashboard.html')

# Controller
# Project
@login_required
def project_list_view(request):
    projects = Project.objects.prefetch_related('stacks').all() 
    return render(request, 'main/projects/project_list.html', {'projects': projects})
# Project Add
@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  
        if form.is_valid():
            project = form.save(commit=False)
            selected_stacks = request.POST.getlist("stacks")
            form.save()
            if selected_stacks:
                project.stacks.set(selected_stacks)
            return redirect('project-list')  
    else:
        form = ProjectForm()
        stacks = Stack.objects.all() 
    return render(request, 'main/projects/add_project.html', {'form': form,"stacks": stacks})
# Project Edit
@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            selected_stacks = request.POST.getlist("stacks")
            form.save()  
            if selected_stacks:
                project.stacks.set(selected_stacks)
            return redirect('project-list') 
    else:
        form = ProjectForm(instance=project)  
        stacks = Stack.objects.all() 
    return render(request, 'main/projects/edit_project.html', {'form': form, 'project': project, "stacks": stacks})
# Project Delete
@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully")
        return redirect('project-list') 
    return render(request, 'main/projects/delete_project.html', {'project': project})



# Work
@login_required
def work_list_view(request):
    works = Work.objects.prefetch_related('stacks').all() 
    return render(request, 'main/works/work_list.html', {'works': works})
# Work Add
@login_required
def add_work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)  
        if form.is_valid():
            work = form.save(commit=False)
            selected_stacks = request.POST.getlist("stacks")
            form.save()
            if selected_stacks:
                work.stacks.set(selected_stacks)
            return redirect('work-list')  
    else:
        form = WorkForm()
        stacks = Stack.objects.all() 
    return render(request, 'main/works/add_work.html', {'form': form,"stacks": stacks})
# Work Edit
@login_required
def edit_work(request, work_id):
    work = get_object_or_404(Work, id=work_id)
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            selected_stacks = request.POST.getlist("stacks")
            form.save()  
            if selected_stacks:
                work.stacks.set(selected_stacks)
            return redirect('work-list') 
    else:
        form = WorkForm(instance=work)  
        stacks = Stack.objects.all() 
    return render(request, 'main/works/edit_work.html', {'form': form, 'work': work, "stacks": stacks})
# Work Delete
@login_required
def delete_work(request, work_id):
    work = get_object_or_404(Work, id=work_id)
    if request.method == 'POST':
        work.delete()
        messages.success(request, "Work deleted successfully")
        return redirect('work-list') 
    return render(request, 'main/works/delete_work.html', {'work': work})



# Education
@login_required
def education_list_view(request):
    educations = Education.objects.all() 
    return render(request, 'main/educations/education_list.html', {'educations': educations})
# Education Add
@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('education-list')  
    else:
        form = EducationForm()
    return render(request, 'main/educations/add_education.html', {'form': form})
# Education Edit
@login_required
def edit_education(request, education_id):
    education = get_object_or_404(Education, id=education_id)
    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES, instance=education)
        if form.is_valid():
            form.save()  
            return redirect('education-list') 
    else:
        form = EducationForm(instance=education)  
    return render(request, 'main/educations/edit_education.html', {'form': form, 'education': education})
# Education Delete
@login_required
def delete_education(request, education_id):
    education = get_object_or_404(Education, id=education_id)
    if request.method == 'POST':
        education.delete()
        messages.success(request, "Education deleted successfully")
        return redirect('education-list') 
    return render(request, 'main/educations/delete_education.html', {'education': education})




# Stack
@login_required
def stack_list_view(request):
    stacks = Stack.objects.all() 
    return render(request, 'main/stacks/stack_list.html', {'stacks': stacks})
# Stack Add
@login_required
def add_stack(request):
    if request.method == 'POST':
        form = StackForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('stack-list')  
    else:
        form = StackForm()
    return render(request, 'main/stacks/add_stack.html', {'form': form})
# Stack Edit
@login_required
def edit_stack(request, stack_id):
    stack = get_object_or_404(Stack, id=stack_id)
    if request.method == 'POST':
        form = StackForm(request.POST, request.FILES, instance=stack)
        if form.is_valid():
            form.save()  
            return redirect('stack-list') 
    else:
        form = StackForm(instance=stack)  
    return render(request, 'main/stacks/edit_stack.html', {'form': form, 'stack': stack})
# Stack Delete
@login_required
def delete_stack(request, stack_id):
    stack = get_object_or_404(Stack, id=stack_id)
    if request.method == 'POST':
        stack.delete()
        messages.success(request, "Stack deleted successfully")
        return redirect('stack-list') 
    return render(request, 'main/stacks/delete_stack.html', {'stack': stack})




# API
class ProjectListAPIView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
class WorkListAPIView(APIView):
    def get(self, request):
        works = Work.objects.all()
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)

class EducationListAPIView(APIView):
    def get(self, request):
        educations = Education.objects.all()
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)
    


    
class StackListAPIView(APIView):
    def get(self, request):
        stack_id = request.GET.get('id')
        
        if stack_id:
            try:
                # Retrieve the stack by id
                stack = Stack.objects.get(id=stack_id)
                serializer = StackSerializer(stack)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Stack.DoesNotExist:
                return Response({'error': 'Stack not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # return all stacks
        stacks = Stack.objects.all()
        serializer = StackSerializer(stacks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


