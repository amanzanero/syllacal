from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'syllabus_reader/index.html')