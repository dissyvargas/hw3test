
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Degree, requiredCourses, degreeSpecific
from .forms import DegreeForm, SearchForm, ExampleForm, UploadForm
from django.contrib import messages
from django.conf import settings


def index(request):
    return render(request, "base.html")

def class_search(request):
    search_text = request.GET.get("search", "")
    #return render(request, "search_result.html", {"search_text": search_text})
    form = SearchForm(request.GET)
    subjects = set()
    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "degree_name"
        if search_in == "degree_name":
            subjects = Degree.objects.filter(degree_name__icontains=search)
        else: 
            sname_requiredCourses= requiredCourses.objects.filter(subject_name__icontains=search)
            for requiredCourses in sname_requiredCourses:
                for subject in requiredCourses.subject_set.all():
                    subjects.add(subject)
    return render(request, 'search-results.html',{"form": form, "search_text": search_text,"classes": subjects})

def welcome_view(request): 
    message = f'<html><h1>Welcome to Degree Checklist!</h1>\
    <p>{Degree.objects.count()} classes and counting</p></html>'
    return HttpResponse(message)

def course_list(request):
    form = requiredCourses.objects.all()
    context = {'form':form}
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
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            save_path = settings.MEDIA_ROOT / request.FILES["file_upload"].name
            with open(save_path, "wb") as output_file:
                for chunk in form.cleaned_data["file_upload"].chunks():
                    output_file.write(chunk)
    else: 
        form = UploadForm()
    return render(request, "media-example.html", {"form": form})

#view for simple_tag
def greeting_view(request):
    return render(request, 'simple_tag_template.html', {'username': 'jdoe'})



