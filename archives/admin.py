# archives/admin.py
from django.contrib import admin
from .models import MedicalDocument, MedicalConcept, UserQuery, RelevanceLabel, Metadata

@admin.register(MedicalDocument)
class MedicalDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'publication_date', 'document_id')
    search_fields = ('title', 'authors', 'document_id')
    # Add more configuration options as needed

@admin.register(MedicalConcept)
class MedicalConceptAdmin(admin.ModelAdmin):
    list_display = ('concept_name', 'concept_id')
    search_fields = ('concept_name', 'concept_id')
    # Add more configuration options as needed

@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('query_text', 'user_id', 'timestamp', 'query_id')
    search_fields = ('query_text', 'user_id', 'query_id')

@admin.register(RelevanceLabel)
class RelevanceLabelAdmin(admin.ModelAdmin):
    list_display = ('query', 'document', 'relevance_score')
    # Add more configuration options as needed

@admin.register(Metadata)
class MetadataAdmin(admin.ModelAdmin):
    list_display = ('dataset_version', 'dataset_source')
    search_fields = ('dataset_version', 'dataset_source')
    # Add more configuration options as needed
