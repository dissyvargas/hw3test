from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('', views.welcome_view,
    #name='welcome_view'),
   # path('admin/', admin.site.urls),
    path('courses/', views.course_list,
        name='course_list'),
    path("degrees/<int:pk>/", views.degree_edit, name="degree_edit"),
    path("degrees/new/", views.degree_edit, name="degree_create"),
    path('form-examples/', views.form_example, name="form_upload")
]   