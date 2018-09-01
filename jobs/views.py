from django.shortcuts import render
from technologies.models import Technologies
from .models import Job
# Create your views here.



def home(request):
    jobs = Job.objects
    technologies = Technologies.objects
    return render(request, 'jobs/home.html', {'jobs': jobs, 'technologies': technologies})
