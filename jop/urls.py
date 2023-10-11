from django.urls import path
from .views import *

urlpatterns = [
    path('', job_list, name='job_list'),
    path('add', add_job, name='add_job'),
    path('job_detail/<str:slug>', job_detail, name='job_detail'),




]
