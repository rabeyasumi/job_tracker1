from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication
        fields = [
            "company_name",
            "position",
            "job_location",
            "salary",
            "status",
            "application_date",
            "deadline",
            "notes",
        ]

        widgets = {
            "application_date": forms.DateInput(attrs={"type": "date"}),
            "deadline": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 5}),
        }

    def clean_company_name(self):
        company = self.cleaned_data.get("company_name")

        if not company.strip():
            raise forms.ValidationError("Company name is required.")

        return company

    def clean_position(self):
        position = self.cleaned_data.get("position")

        if not position.strip():
            raise forms.ValidationError("Position is required.")

        return position

    def clean_salary(self):
        salary = self.cleaned_data.get("salary")

        if salary is not None and salary < 0:
            raise forms.ValidationError("Salary cannot be negative.")

        return salary

    def clean_notes(self):
        notes = self.cleaned_data.get("notes")

        if len(notes) > 500:
            raise forms.ValidationError("Notes cannot exceed 500 characters.")

        return notes

    def clean(self):
        cleaned_data = super().clean()

        application_date = cleaned_data.get("application_date")
        deadline = cleaned_data.get("deadline")

        if application_date and deadline:
            if deadline < application_date:
                self.add_error(
                    "deadline",
                    "Deadline cannot be earlier than application date."
                )

        return cleaned_data