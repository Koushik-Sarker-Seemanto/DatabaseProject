from django.conf.urls import url
from . import views

app_name = 'healthapp'

urlpatterns = [
    #  / healthapp/
    url(r'^$', views.indexView, name='index'),

    url(r'^doctor_reg/$', views.DoctorFormView.as_view(), name='doctor_reg'),

    url(r'^patient_reg/$', views.PatientFormView.as_view(), name='patient_reg'),

    url(r'^doctor_profile/(?P<pk>[0-9]+)/$', views.DoctorProfileView.as_view(), name='doctor_profile'),

    url(r'^patient_profile/(?P<pk>[0-9]+)/$', views.PatientProfileView.as_view(), name='patient_profile'),

    url(r'^doctor_login/$', views.DoctorLoginView.as_view(), name='doctor_login'),

    url(r'^patient_login/$', views.PatientLoginView.as_view(), name='patient_login'),

    url(r'^patient_profile/search/$', views.SearchView.as_view(), name='search'),

    url(r'^patient_profile/search/doctor_profile/(?P<pk>[0-9]+)/$', views.DoctorProfileViewAsPatient.as_view(),
        name='doctor_profile_patient'),

    url(r'^patient_profile/search/area/$', views.AreaSearchView.as_view(), name='area_search'),

    url(r'^patient_profile/search/category/$', views.CategorySearchView.as_view(), name='category_search'),

    url(r'^patient_profile/search/filter/$', views.FilterSearchView.as_view(), name='filter_search'),

    url(r'^doctor_profile/(?P<pk>[0-9]+)/schedule_list/$', views.ScheduleList, name='schedule_list'),

    url(r'^doctor_profile/(?P<pk>[0-9]+)/schedule_list/schedule_add/$', views.ScheduleAddView.as_view(), name='schedule_add')

]