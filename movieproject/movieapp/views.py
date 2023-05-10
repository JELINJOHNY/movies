from django.shortcuts import render, redirect

from .forms import MOVIEForm
from . models import Movie

# Create your views here.
def testf(request):
    task1 = Movie.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        year=request.POST['year']
        img=request.FILES['img']
        a=Movie(name=name,description=description,year=year,img=img)
        a.save()
    return render(request ,'task.html',{'task1':task1})


def delete(request,task_id):
    task1 = Movie.objects.get(id=task_id)
    if request.method =="POST":
        task1.delete()
        return redirect('/')
    return  render(request,'delete.html')


def update(request,id):
    task=Movie.objects.get(id=id)
    f=MOVIEForm(request.POST or None,request.FILES, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})