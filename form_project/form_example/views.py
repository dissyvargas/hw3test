from django.shortcuts import render
from .forms import ExampleForm

# Create your views here.
def form_example(request):
    form = ExampleForm()
    return render(
     request, "form-example.html", {"method": request.method, "form":form}
    )