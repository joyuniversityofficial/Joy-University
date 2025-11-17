import os
from django.conf import settings

def pdfs_context(request):
    pdf_dir = os.path.join(settings.BASE_DIR, 'staticfiles', 'pdfs')
    pdfs = []
    if os.path.exists(pdf_dir):
        for file in os.listdir(pdf_dir):
            if file.endswith('.pdf'):
                # Clean up the name by replacing underscores and capitalizing
                name = file.replace('.pdf', '').replace('_', ' ').title()
                pdfs.append({'name': name, 'file': file})
    return {'pdfs': pdfs}
