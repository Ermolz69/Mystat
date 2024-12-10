from django.db import models

class Task(models.Model):  # homework
    id = models.IntegerField("ID", primary_key=True)
    description = models.TextField("Description")
    deadline = models.DateField("Deadline")

    def get_absolute_url(self):
        return f'homework/{self.id}'

    def __str__(self):
        return self.description

class Lesson(models.Model):
    id = models.IntegerField("ID", primary_key=True)
    subject = models.CharField("Subject", max_length=15)
    topic = models.CharField("Topic", max_length=15)
    date = models.DateField("Date")

    def get_absolute_url(self):
        return f'schedule/{self.id}'

    def __str__(self):
        return self.subject

class Feedback(models.Model):
    id = models.IntegerField("ID", primary_key=True)
    topic = models.CharField("Topic", max_length=15)
    description = models.TextField("Description")

    def __str__(self):
        return self.topic



