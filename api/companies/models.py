from django.db import models

class Company(models.Model):

    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, choices=CompanyStatus.choices, default=CompanyStatus.HIRING)
    last_update = models.DateTimeField(auto_now=True, editable=True)
    application_link = models.URLField(blank=True)
    notes = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.name