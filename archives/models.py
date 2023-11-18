# archives/models.py
from django.db import models

class MedicalDocument(models.Model):
    title = models.CharField(max_length=255)
    authors = models.TextField()
    publication_date = models.DateField()
    abstract = models.TextField()
    body_text = models.TextField()
    keywords = models.TextField()
    references = models.TextField()
    document_id = models.CharField(max_length=50, unique=True)

class MedicalConcept(models.Model):
    concept_name = models.CharField(max_length=255)
    concept_id = models.CharField(max_length=50, unique=True)
    definition = models.TextField()
    synonyms = models.TextField()
    hierarchical_relationships = models.TextField()

class UserQuery(models.Model):
    query_text = models.TextField()
    user_id = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    query_id = models.CharField(max_length=50, unique=True)

class RelevanceLabel(models.Model):
    query = models.ForeignKey(UserQuery, on_delete=models.CASCADE)
    document = models.ForeignKey(MedicalDocument, on_delete=models.CASCADE)
    relevance_score = models.IntegerField()

class Metadata(models.Model):
    dataset_version = models.CharField(max_length=50)
    licensing_information = models.TextField()
    dataset_source = models.CharField(max_length=255)
    data_preprocessing_details = models.TextField()

# Add more models as needed
