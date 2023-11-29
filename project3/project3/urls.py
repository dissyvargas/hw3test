"""
URL configuration for project3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.conf import settings
import degree_checklist.views
from django.contrib import admin, auth
from django.urls import include, path
from django.conf.urls.static import static
from project3.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', degree_checklist.views.index),
    path('class-search/', degree_checklist.views.class_search),
    path('', include('degree_checklist.urls')),
    path('media-example/', degree_checklist.views.media_example),
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")),
    path("accounts/password_reset/done/", auth.views.PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("accounts/reset/done/", auth.views.PasswordResetCompleteView.as_view(),name="password_reset_complete",),
    path('accounts/profile/', profile, name='profile')
    
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

