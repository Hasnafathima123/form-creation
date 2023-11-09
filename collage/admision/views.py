from django.shortcuts import render
from django.http import HttpResponse
from . forms import studentform
from.models import student

def index(request):
    name=""
    if 'save' in request.POST:
        name=request.Post['name']
        data=student.objects.filter(name=name)
        return render(request,"index.html",{"name":data})
    if 'delete' in request.post:
        name=request.post['post']
        data=student.objects.get(name=name).delete()
        return  render(request,"index.html")
    if 'edit' in request.post:
        name=request.post['post']
        post=student.objects.get(name=name)
        form=studentform(instance=post)
    return render(request, 'edit.html',{'form':form})
return render(request,"index.html")   
  

def register(request): 
    form=studentform()
    if request.method=='POST':
        form =studentform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> thank you </h1>')
    return render(request,"register.html",{"form":form})

def edit(request, id):
    post=student.objects.get(id=id)
    form=studentform(instance=post)
    if request.method == 'POST':
        form = studentform(request.POST, instance=post)
        if form.is_valid():  
            form.save()
            return rndex(request)
    return render(request, 'edit.html',{'form':form})



       


