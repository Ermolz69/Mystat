from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .form import Feedbackform
from .models import Lesson, Task, Feedback

def show_index(request):
    return render(request, "main/index.html")

def show_schedule(request):
    lessons = Lesson.objects.all()
    return render(request, "main/schedule.html", {'lessons':lessons})

def show_about(request):
    return render(request, "main/about.html")

def show_feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, "main/feedback.html", {'feedbacks':feedbacks})

def show_homework(request):
    tasks = Task.objects.order_by('id')
    return render(request, "main/homework.html",{'tasks':tasks})

def feedback_create(request):
    if request.method == 'POST':
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_student')

    form = Feedbackform()
    data = {
        'form':form
    }

    return render(request, "main/feedback_create.html", data)