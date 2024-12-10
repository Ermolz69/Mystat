from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name="home_student"),
    path('about/', views.show_about, name="about"),
    path('schedule/', views.show_schedule, name="schedule"),
    path('feedback/', views.show_feedback, name="feedback"),
    path('homework/', views.show_homework, name="homework"),
    path('feedbackcreate/', views.feedback_create, name="create"),
]
