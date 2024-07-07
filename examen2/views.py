from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from examen2.models import *
from examen2.serializer import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from examen2.forms import *

# Create your views here.
def Index(request):
    return render(request, 'home/index.html')

def dashboard(request):
    return render(request, 'home/dashboard.html')

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.data.get('username'))
        if not user.check_password(request.data.get('password')):
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return redirect('dashboard')
    
@login_required
def create_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('dashboard')
    else:
        form = ToDoForm()
    return render(request, 'core/create_todo.html', {'form': form})
    
@login_required
def todo_list(request):
    todos = ToDo.objects.all()
    return render(request, 'core/todo_list.html', {'todos': todos})

@login_required
def todo_id_title_list(request):
    todos = ToDo.objects.all().values('id', 'title')
    return render(request, 'core/todo_id_title_list.html', {'todos': todos})

@login_required
def todo_unresolved_list(request):
    todos = ToDo.objects.filter(completed=False).values('id', 'title')
    return render(request, 'core/todo_unresolved_list.html', {'todos': todos})

@login_required
def todo_resolved_list(request):
    todos = ToDo.objects.filter(completed=True).values('id', 'title')
    return render(request, 'core/todo_resolved_list.html', {'todos': todos})

@login_required
def todo_user_list(request):
    todos = ToDo.objects.all().values('id', 'user_id')
    return render(request, 'core/todo_user_list.html', {'todos': todos})

@login_required
def todo_resolved_user_list(request):
    todos = ToDo.objects.filter(completed=True).values('id', 'user_id')
    return render(request, 'core/todo_resolved_user_list.html', {'todos': todos})

@login_required
def todo_unresolved_user_list(request):
    todos = ToDo.objects.filter(completed=False).values('id', 'user_id')
    return render(request, 'core/todo_unresolved_user_list.html', {'todos': todos})