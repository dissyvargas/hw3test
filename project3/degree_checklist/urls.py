from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('', views.welcome_view,
    #name='welcome_view'),
    path('courses/', views.course_list,
        name='course_list'),
    path("degrees/<int:pk>/", views.degree_edit, name="degree_edit"),
    path("degrees/new/", views.degree_edit, name="degree_create")
]   