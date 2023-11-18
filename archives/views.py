from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MedicalDocument, MedicalConcept, UserQuery, RelevanceLabel, Metadata
from django.contrib import messages
from django.core.paginator import Paginator

@login_required(login_url='/authentication/login')
def index(request):
    documents = MedicalDocument.objects.all()
    paginator = Paginator(documents, 10)  # Display 10 documents per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'archives/index.html', {'page_obj': page_obj})

@login_required(login_url='/authentication/login')
def document_detail(request, document_id):
    document = get_object_or_404(MedicalDocument, id=document_id)
    return render(request, 'archives/document_detail.html', {'document': document})

@login_required(login_url='/authentication/login')
def document_add(request):
    if request.method == 'POST':
        # Process form data and save to the database
        title = request.POST['title']
        authors = request.POST['authors']
        publication_date = request.POST['publication_date']
        abstract = request.POST['abstract']
        body_text = request.POST['body_text']
        keywords = request.POST['keywords']
        references = request.POST['references']
        document_id = request.POST['document_id']

        MedicalDocument.objects.create(
            title=title,
            authors=authors,
            publication_date=publication_date,
            abstract=abstract,
            body_text=body_text,
            keywords=keywords,
            references=references,
            document_id=document_id
        )
        messages.success(request, 'Document added successfully')
        return redirect('index')

    return render(request, 'archives/document_add.html')

@login_required(login_url='/authentication/login')
def document_edit(request, document_id):
    document = get_object_or_404(MedicalDocument, id=document_id)

    if request.method == 'POST':
        # Process form data and update the database
        document.title = request.POST['title']
        document.authors = request.POST['authors']
        document.publication_date = request.POST['publication_date']
        document.abstract = request.POST['abstract']
        document.body_text = request.POST['body_text']
        document.keywords = request.POST['keywords']
        document.references = request.POST['references']
        document.document_id = request.POST['document_id']

        document.save()
        messages.success(request, 'Document updated successfully')
        return redirect('index')

    return render(request, 'archives/document_edit.html', {'document': document})

@login_required(login_url='/authentication/login')
def document_statistics(request):
    # Add your statistical calculations here
    # For example, you can calculate the total number of documents, average publication date, etc.
    total_documents = MedicalDocument.objects.count()
    # Add more statistical calculations as needed

    return render(request, 'archives/document_statistics.html', {'total_documents': total_documents})
