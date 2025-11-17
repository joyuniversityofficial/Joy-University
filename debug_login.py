import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'joy.settings')
django.setup()

from university.models import Application

print("Checking applications in database:")
applications = Application.objects.all()
if not applications:
    print("No applications found in database.")
else:
    for app in applications:
        print(f"ID: {app.id}, Email: '{app.email}', Password: '{app.password}'")
