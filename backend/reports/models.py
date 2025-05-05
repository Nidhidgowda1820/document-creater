# reports/models.py
from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    docx_file = models.FileField(upload_to='reports/docx/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='reports/pdf/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
