from django.shortcuts import render,redirect
from .models import newuser
# Create your views here.
def appview(request):
    if request.method == 'POST':
        print(request.POST["name"])
        name = newuser(name=request.POST["name"], mobile=request.POST["mobile"], email=request.POST["email"])
        name.save()
        # return redirect('fromapp1') #.objects.create
    return render(request, 'App/appview.html', {})
def viewdata(request, id):
    data = newuser.objects.get(id=id)
    return render(request, "App/viewdata.html", {"a":data})