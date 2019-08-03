from builtins import id

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View, DetailView, RedirectView
from django.http import HttpResponseRedirect, Http404
from .forms import DoctorRegForm, PatientRegForm, DoctorLoginForm, ScheduleForm
from .models import UserDoctor, UserPatient, Schedule
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse


def indexView(request):
    return render(request, "healthapp/index.html")


class DoctorFormView(View):
    form_class = DoctorRegForm
    template_name = 'healthapp/DoctorRegistration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            doctor_name = form.cleaned_data['doctor_name']
            doctor_email = form.cleaned_data['doctor_email']
            doctor_workplace = form.cleaned_data['doctor_workplace']
            doctor_catrgory = form.cleaned_data['doctor_category']
            doctor_degree = form.cleaned_data['doctor_degree']
            doctor_gender = form.cleaned_data['doctor_gender']
            doctor_age = form.cleaned_data['doctor_age']
            doctor_phone = form.cleaned_data['doctor_phone']

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            print('iiiiii AM dOCTOR')
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('healthapp:doctor_profile', user.id)

        return render(request, self.template_name, {'form': form})


class DoctorLoginView(View):
    form_class = DoctorLoginForm
    template_name = 'healthapp/DoctorLogin.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print("laaaaaaaaaaaakkkkkkkkkkkaaaaaa")
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse('error'))
        if not user.is_active:
            return HttpResponseRedirect(reverse('error'))
        login(request, user)
        return redirect('healthapp:doctor_profile', user.id)


class PatientLoginView(View):
    form_class = DoctorLoginForm
    template_name = 'healthapp/PatientLogin.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print("laaaaaaaaaaaakkkkkkkkkkkaaaaaa")
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse('error'))
        if not user.is_active:
            return HttpResponseRedirect(reverse('error'))

        # Correct password, and the user is marked "active"
        login(request, user)
        # Redirect to a success page.
        return redirect('healthapp:patient_profile', user.id)


class PatientFormView(View):
    form_class = PatientRegForm
    template_name = 'healthapp/PatientRegistration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            patient_name = form.cleaned_data['patient_name']
            patient_email = form.cleaned_data['patient_email']
            patient_area = form.cleaned_data['patient_area']
            patient_blood = form.cleaned_data['patient_blood']
            patient_gender = form.cleaned_data['patient_gender']
            patient_age = form.cleaned_data['patient_age']
            patient_phone = form.cleaned_data['patient_phone']

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('healthapp:patient_profile', user.id)
                    # return HttpResponseRedirect('doctor_profile')

        return render(request, self.template_name, {'form': form})


class PatientProfileView(generic.DetailView):
    model = UserPatient
    template_name = 'healthapp/PatientProfile2.html'
    context_object_name = 'user'


class DoctorProfileView(generic.DetailView):
    model = UserDoctor
    template_name = 'healthapp/DoctorProfile2.html'
    context_object_name = 'user'


class DoctorProfileViewAsPatient(generic.DetailView):
    model = UserDoctor
    template_name = 'healthapp/DoctorProfileAsPatient.html'
    context_object_name = 'user'


class AreaSearchView(generic.ListView):
    model = UserDoctor
    template_name = 'healthapp/SearchByArea.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('area')
        object_list = UserDoctor.objects.filter(doctor_workplace=query)
        return object_list


class CategorySearchView(generic.ListView):
    model = UserDoctor
    template_name = 'healthapp/SearchByCategory.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('category')
        object_list = UserDoctor.objects.filter(doctor_category=query)
        return object_list


class FilterSearchView(generic.ListView):
    model = UserDoctor
    template_name = 'healthapp/SearchByFilter.html'

    def get_queryset(self):
        query1 = self.request.GET.get('area_filter')
        query2 = self.request.GET.get('category_filter')
        object_list = UserDoctor.objects.filter(doctor_workplace=query1).filter(doctor_category=query2)
        return object_list


class SearchView(generic.ListView):
    template_name = 'healthapp/DoctorSearch.html'
    context_object_name = 'all_doctor'

    def get_queryset(self):
        return UserDoctor.objects.all()


class ScheduleAddView(CreateView):
    model = Schedule
    fields = ['start_time', 'end_time', 'hospital_name', 'doctor_id']
    template_name = 'healthapp/schedule_form.html'


def ScheduleList(request, pk):
    object_list = Schedule.objects.filter(doctor_id_id=pk)
    return render(request, 'healthapp/ScheduleList.html', {'object_list': object_list})


