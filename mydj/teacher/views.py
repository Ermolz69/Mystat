from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import Taskform, Lessonform
from main.models import Task, Lesson, Feedback


class HomeworkDetailView(DetailView):
    model = Task
    template_name = 'teacher/templates/teacher/homework_detail_view.html'
    context_object_name = 'task'

class HomeworkUpdateView(UpdateView):
    model = Task
    template_name = 'teacher/templates/teacher/homework_create.html'
    form_class = Taskform
    success_url = '/teacher/homework'

class HomeworkDeleteView(DeleteView):
    model = Task
    success_url = '/teacher/homework'
    template_name = 'teacher/templates/teacher/homework-delete.html'



class ScheduleDetailView(DetailView):
    model = Lesson
    template_name = 'teacher/templates/teacher/schedule_detail_view.html'
    context_object_name = 'lesson'

class ScheduleUpdateView(UpdateView):
    model = Lesson
    template_name = 'teacher/templates/teacher/schedule_create.html'
    form_class = Lessonform
    success_url = '/teacher/schedule'

class ScheduleDeleteView(DeleteView):
    model = Lesson
    success_url = '/teacher/schedule'
    template_name = 'teacher/templates/teacher/schedule_delete.html'


# Create your views here.
def show_createhomework(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_teacher')

    form = Taskform()
    data = {
        'form':form
    }
    return render(request, "teacher/templates/teacher/homework_create.html", data)

def show_createschedule(request):
    if request.method == 'POST':
        form = Lessonform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_teacher')

    form = Lessonform()
    data = {
        'form':form
    }
    return render(request, "teacher/templates/teacher/schedule_create.html", data)

def show_homework(request):
    tasks = Task.objects.all()
    return render(request, "teacher/templates/teacher/homework.html",{'tasks':tasks})

def show_schedule(request):
    lessons = Lesson.objects.all()
    return render(request, "teacher/templates/teacher/schedule.html", {'lessons':lessons})

def show_index(request):
    return render(request, "teacher/templates/teacher/index.html")
