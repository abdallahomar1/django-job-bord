from django.shortcuts import render
from .models import jop
from django.core.paginator import Paginator
from .forms import Apllyform
from .filters import jobFilter
# Create your views here.

def jop_list(request):
    jop_list = jop.objects.all()
    myfilter = jobFilter(request.GET, queryset=jop_list)
    jop_list = myfilter.qs
    context={'jobs': jop_list, 'myfilter': myfilter}
    return render(request, 'jop\jop_list.html', context)


def jop_deteil(request, id):
    jop_deteil = jop.objects.get(id= id)
    if request.method == 'POST':
        form = Apllyform(request.POST, request.FILES)
        
        if form.is_valid():
            myform = form.save(commit=False)
            myform.jobs = jop_deteil
            myform.save()
            print('ok')

    else:
        form  = Apllyform()
    
    context={'job': jop_deteil, 'form':form}
    return render(request, 'jop\jop_detail.html', context)

def add_job(request):
    

    return render(request, 'jop/add_job.html', {})


