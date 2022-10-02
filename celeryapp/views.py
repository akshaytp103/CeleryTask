from django.shortcuts import render,redirect
from .task import generate_file
from celery.result import AsyncResult

# Create your views here.

def index(request):
    
    if request.method == 'POST':       
        file_name = request.POST.get('file_name')
        rows = request.POST.get('count')
  
        task = generate_file.delay(file_name,rows)
        return redirect('success')
    return render(request,'home.html')



def success(request):
    return render(request,'result.html')