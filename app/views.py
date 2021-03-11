from django.shortcuts import render
from .forms import ImageForm
from .models import ImageModel
# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        img = ImageModel.objects.all()

    elif request.method == "GET":
        category_name = request.GET.get('category_name')
        if category_name:
           img = ImageModel.objects.filter(category=category_name)
        else:
           img = ImageModel.objects.all()
    form = ImageForm()
    return render(request,'app/home.html',{'form':form,'img':img})