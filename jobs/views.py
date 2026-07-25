from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import JobApplication
from .forms import JobApplicationForm


def home(request):

    jobs = JobApplication.objects.all()

    context = {
        "total": jobs.count(),
        "applied": jobs.filter(status="Applied").count(),
        "interview": jobs.filter(status="Interview").count(),
        "offer": jobs.filter(status="Offer").count(),
        "accepted": jobs.filter(status="Accepted").count(),
        "rejected": jobs.filter(status="Rejected").count(),
    }

    return render(request, "home.html", context)


def job_list(request):

    jobs = JobApplication.objects.all().order_by("-created_at")

    return render(
        request,
        "jobs/list.html",
        {"jobs": jobs}
    )


def job_detail(request, id):

    job = get_object_or_404(JobApplication, id=id)

    return render(
        request,
        "jobs/detail.html",
        {"job": job}
    )


def job_create(request):

    if request.method == "POST":

        form = JobApplicationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Job application added successfully."
            )

            return redirect("job_list")

    else:

        form = JobApplicationForm()

    return render(
        request,
        "jobs/create.html",
        {"form": form}
    )


def job_update(request, id):

    job = get_object_or_404(JobApplication, id=id)

    if request.method == "POST":

        form = JobApplicationForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Application updated successfully."
            )

            return redirect("job_list")

    else:

        form = JobApplicationForm(instance=job)

    return render(
        request,
        "jobs/update.html",
        {
            "form": form,
            "job": job,
        }
    )


def job_delete(request, id):

    job = get_object_or_404(JobApplication, id=id)

    if request.method == "POST":

        job.delete()

        messages.success(
            request,
            "Application deleted successfully."
        )

        return redirect("job_list")

    return render(
        request,
        "jobs/delete.html",
        {"job": job}
    )