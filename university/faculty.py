from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Faculty

def faculty(request):
    faculty_members = Faculty.objects.all()
    paginator = Paginator(faculty_members, 10)  # Show 10 faculty per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'faculty.html', {'page_obj': page_obj})
