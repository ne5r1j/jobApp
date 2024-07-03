from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

from app.models import JobPost

job_title= [
  'First Job', 'Second Job', 'Third Job'
]

job_desciption = [
  'Job 1 description', 'Job 2 description', 'Job 3 description'
]

# Create your views here.
# def hello(request):
#   return HttpResponse("Hello World")
class tempClass:
  x = 5


def hello(request):
  is_aunthenticated = True
  demo_list = ["alpha", "beta", "gamma"]
  temp = tempClass()
  context = {"name":"Neeraj", "list_content": demo_list, "class_content": tempClass, "is_aunthenticated":is_aunthenticated}
  return render(request, 'app/hello.html', context)


def job_list(request):
  jobs = JobPost.objects.all()
  context = {"jobs":jobs}
  return render(request, 'app/index.html', context)

  # list_of_jobs = "<ul>"
  # for jobs in job_title:
  #   job_id = job_title.index(jobs)
  #   detail_url = reverse('jobs_detail', args=(job_id,))
  #   list_of_jobs += f"<a href='{detail_url}'><li>{jobs}</a></li>"
  # list_of_jobs += "</ul>"
  # return HttpResponse(list_of_jobs)

def jobDetail(request, id):
  # return HttpResponse(f"Job detail page {id}")
  try:
    if id == 0:
      return redirect(reverse('jobs_home'))
    # context = {"job_title":job_title[id], "job_description":job_desciption[id]}
    # return_html = f"<h1>{}</h1> <h3>{job_desciption[int(id)]}</h3>"
    job = JobPost.objects.get(id=id)
    context = {"job":job}
    return render(request, 'app/jobdetail.html', context)
  except:
    # return HttpResponse("Not Found")
    return HttpResponseNotFound("Not Found")