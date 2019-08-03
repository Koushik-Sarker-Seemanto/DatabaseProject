from django.db import models

# Create your models here.
from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse


class UserDoctor(User):
    isDoctor = models.BooleanField(default=True)
    doctor_name = models.CharField(max_length=50)
    doctor_email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    doctor_workplace = models.CharField(max_length=100)
    doctor_category = models.CharField(max_length=50)
    doctor_degree = models.CharField(max_length=100)
    doctor_gender = models.CharField(max_length=10)
    doctor_age = models.CharField(max_length=3)
    doctor_phone = models.CharField(max_length=14)

    REQUIRED_FIELDS = [doctor_name, doctor_email, doctor_workplace, doctor_category, doctor_degree, doctor_gender, doctor_age, doctor_phone]

    def get_absolute_url(self):
        return reverse('healthapp:doctor_profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.doctor_name


class UserPatient(User):
    patient_name = models.CharField(max_length=50)
    patient_email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    patient_area = models.CharField(max_length=30)
    patient_blood = models.CharField(max_length=5)
    patient_gender = models.CharField(max_length=10)
    patient_age = models.CharField(max_length=3)
    patient_phone = models.CharField(max_length=14)

    REQUIRED_FIELDS = [patient_name, patient_email, patient_area, patient_blood, patient_gender, patient_age, patient_phone]

    def __str__(self):
        return self.patient_name


class Schedule(models.Model):
    start_time = models.CharField(max_length=30, default='')
    end_time = models.CharField(max_length=30, default='')
    hospital_name = models.CharField(max_length=50)
    doctor_id = models.ForeignKey(UserDoctor, default=None, on_delete=models.CASCADE)

    REQUIRED_FIELDS = [start_time, end_time, hospital_name, doctor_id]

    def __str__(self):
        return self.doctor_id
