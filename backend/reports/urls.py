from django.urls import path
from . import views

urlpatterns = [
    path('generate-pdf/<int:report_id>/', views.generate_pdf, name='generate_pdf'),
    path('view-reports/', views.view_reports, name='view_reports'),
    path('generate-docx/<int:report_id>/', views.generate_docx, name='generate_docx'),
    path('download-docx/<int:report_id>/', views.download_docx, name='download_docx'),
    path('download-pdf/<int:report_id>/', views.download_pdf, name='download_pdf'),
]
