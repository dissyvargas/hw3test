
from django.shortcuts import render, get_object_or_404, redirect
from .models import Degree, requiredCourses, degreeSpecific
from .forms import DegreeForm, SearchForm, ExampleForm
from django.contrib import messages

def index(request):
    return render(request, "base.html")

def class_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})

def course_list(request):
    courses = requiredCourses.objects.all()
    course_list = []
    for course in courses:
        course_list.append({'course': course})
    context = {
        'course_list': course_list
    }
    return render(request, 'course_list.html', context)

def degree_edit(request, pk=None): 
    if pk is not None:
        degree = get_object_or_404(Degree, pk=pk)
    else: 
        degree = None
    if request.method != "POST": 
        form = DegreeForm(request.POST, instance=degree)
        if form.is_valid():
            updated_degree = form.save()
            if degree is None: 
                messages.success(
                    request, 'Degree "{}" was created.'.format(updated_degree)
                )
            else: 
                messages.success(
                    request, 'Degree "{}" was updated.'.format(updated_degree)
                )
            return redirect("degree_edit", updated_degree.pk)
        else:
            form = DegreeForm(instance=degree)
        return render(
            request, "form-example.html", {"method": request.method, "form":form}

        )
    
def form_example(request):
    form = ExampleForm()
    return render(
     request, "form-examples.html", {"method": request.method, "form":form}
    )

def media_example(request):
    return render(
        request, "media-example.html"
    )