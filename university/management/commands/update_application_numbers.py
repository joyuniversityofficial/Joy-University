from django.core.management.base import BaseCommand
from university.models import Application, Enrollment

class Command(BaseCommand):
    help = 'Update application numbers to use JU prefix'

    def handle(self, *args, **options):
        applications = Application.objects.filter(application_number__startswith='APP')
        for app in applications:
            # Extract the number part
            num_part = app.application_number[3:]  # Remove 'APP'
            new_number = f'JU{num_part}'
            app.application_number = new_number
            app.save(update_fields=['application_number'])
            self.stdout.write(f'Updated Application {app.id} application_number to {new_number}')

        enrollments = Enrollment.objects.filter(application_number__startswith='APP')
        for enr in enrollments:
            # Extract the number part
            num_part = enr.application_number[3:]  # Remove 'APP'
            new_number = f'JU{num_part}'
            enr.application_number = new_number
            enr.save(update_fields=['application_number'])
            self.stdout.write(f'Updated Enrollment {enr.id} application_number to {new_number}')

        self.stdout.write('Done updating application numbers.')
