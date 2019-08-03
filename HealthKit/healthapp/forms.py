from django.contrib.auth.models import User
from django import forms
from healthapp.models import UserDoctor, UserPatient, Schedule


class DoctorRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDoctor
        fields = ['doctor_name', 'doctor_email', 'doctor_workplace', 'doctor_category', 'doctor_degree', 'doctor_gender', 'doctor_age', 'doctor_phone', 'username']


class PatientRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserPatient
        fields = ['patient_name', 'patient_email', 'patient_area', 'patient_blood', 'patient_gender', 'patient_age', 'patient_phone', 'username']


class DoctorLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDoctor
        fields = ['username']


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['start_time', 'end_time', 'hospital_name', 'doctor_id']
