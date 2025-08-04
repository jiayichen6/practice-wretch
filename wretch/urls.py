from django.contrib import admin
from django.urls import path
from wretch.view import about, home


urlpatterns = [
    path("about/", about),
    path("", home),
    path("admin/", admin.site.urls),
]
