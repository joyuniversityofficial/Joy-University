from django.core.management.base import BaseCommand
from university.models import Application
import hashlib

class Command(BaseCommand):
    help = 'Normalize email addresses in Application model and regenerate passwords'

    def handle(self, *args, **options):
        applications = Application.objects.all()
        updated_count = 0
        for app in applications:
            original_email = app.email
            normalized_email = original_email.strip().lower() if original_email else original_email
            if original_email != normalized_email:
                app.email = normalized_email
                app.password = hashlib.sha256(normalized_email.encode()).hexdigest()[:8]
                app.save(update_fields=['email', 'password'])
                updated_count += 1
                self.stdout.write(f'Updated {original_email} to {normalized_email} and regenerated password')
        self.stdout.write(self.style.SUCCESS(f'Successfully normalized {updated_count} email addresses and passwords'))
