from django.shortcuts import render
from .models import ClassBox

# Create your views here.
def index(request):
    classboxes = ClassBox.objects.all().order_by('class_name')
    return render(request, 'index2.html', {'classboxes':classboxes})
    # change index2 to index to put back to original

def add_material(request):
    classboxes = ClassBox.objects.all()
    return render(request, 'add_material.html', {'classboxes':classboxes})
