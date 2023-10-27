from django.contrib import admin
from django.urls import path
from lists import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index_page, name="index"),
]
