from django.shortcuts import render, redirect
from .models import Fruits
from .forms import FruitForm



def index(request):
    fruits = Fruits.objects.all()
    return render(request, 'fruits.html', {'fruits': fruits})


def create(request):
    if request.method == 'POST':
        data = Fruits(
            name=request.POST['name'],
            description=request.POST['description'],
            img=request.POST['img']
        )
        data.save()
        return redirect('index')
    form = FruitForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)