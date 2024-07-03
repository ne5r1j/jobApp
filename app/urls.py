from django.urls import path
from . import views

urlpatterns = [
  path('', views.job_list, name='jobs_home'),
  path('hello/', views.hello, name = 'hello'),
  path('job/<int:id>', views.jobDetail, name='jobs_detail'),
  
]