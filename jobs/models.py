from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Interview", "Interview"),
        ("Offer", "Offer"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    ]

    company_name = models.CharField(max_length=100)

    position = models.CharField(max_length=100)

    job_location = models.CharField(max_length=100)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Applied"
    )

    application_date = models.DateField()

    deadline = models.DateField()

    notes = models.TextField(
        blank=True,
        max_length=500
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.deadline < self.application_date:
            raise ValidationError({
                "deadline": "Deadline cannot be earlier than application date."
            })

    def __str__(self):
        return f"{self.company_name} - {self.position}"