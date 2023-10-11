from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.


def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 1)  # Show  contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
        'allbooks': Job.objects.all().count(),
    }
    return render(request, 'jobs_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApllyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            print('DOne')
    else:
        form = ApllyForm()

    context = {'job': job_detail, 'form1': form}
    return render(request, 'job_detail.html', context)


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect('job_list')

    else:
        form = JobForm()

    return render(request, 'add_job.html', {'form': form})
