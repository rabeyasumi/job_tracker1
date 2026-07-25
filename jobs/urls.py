from django.urls import path
from . import views


urlpatterns = [

    path("", views.home, name="home"),
    path("jobs/", views.job_list, name="job_list" ),
    path("jobs/add/", views.job_create, name="job_create"),
    path("jobs/<int:id>/", views.job_detail, name="job_detail"),
    path("jobs/<int:id>/edit/", views.job_update, name="job_update"),
    path("jobs/<int:id>/delete/", views.job_delete, name="job_delete"),
]