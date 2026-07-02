from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


def root_redirect(request):
    return redirect('http://localhost:3000/')

urlpatterns = [
    path('', root_redirect),
    path('admin/', admin.site.urls),
    path('api/', include('devconnector.urls')),
]
