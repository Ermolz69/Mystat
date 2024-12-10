from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name="home_teacher"),
    path('homework/', views.show_homework, name="homework_t"),
    path('schedule/', views.show_schedule, name="schedule_t"),
    path('create_homework', views.show_createhomework, name="create_homework"),
    path('create_schedule', views.show_createschedule, name="create_schedule"),

    path('homework/<int:pk>/', views.HomeworkDetailView.as_view(), name="homework-detail"),
    path('homework/<int:pk>/update', views.HomeworkUpdateView.as_view(), name="homework-update"),
    path('homework/<int:pk>/delete', views.HomeworkDeleteView.as_view(), name="homework-delete"),

    path('schedule/<int:pk>/', views.ScheduleDetailView.as_view(), name="schedule-detail"),
    path('schedule/<int:pk>/update', views.ScheduleUpdateView.as_view(), name="schedule-update"),
    path('schedule/<int:pk>/delete', views.ScheduleDeleteView.as_view(), name="schedule-delete")
]
