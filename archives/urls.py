from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('document/<int:document_id>/', views.document_detail, name='document_detail'),
    path('document/add/', views.document_add, name='document_add'),
    path('document/edit/<int:document_id>/', views.document_edit, name='document_edit'),
    path('document/statistics/', views.document_statistics, name='document_statistics'),
]

# Note: Adjust the URL patterns according to your project structure and requirements.
