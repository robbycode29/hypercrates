from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    doctor = models.ForeignKey(Doctor, related_name='patients', on_delete=models.CASCADE)
    assistants = models.ManyToManyField('Assistant', related_name='patients', blank=True)

    def __str__(self):
        return self.name

class Assistant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Treatment(models.Model):
    patient = models.ForeignKey(Patient, related_name='treatments', on_delete=models.CASCADE)
    assistant = models.ForeignKey(Assistant, related_name='treatments', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Treatment for {self.patient.name} by {self.assistant.name}"