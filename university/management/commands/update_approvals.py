from django.core.management.base import BaseCommand
from university.models import Approval

class Command(BaseCommand):
    help = 'Update Approval model instances with correct image URLs and alt texts'

    def handle(self, *args, **kwargs):
        approvals_data = [
            {'img_url': 'images/approvals/lsc_logo.png', 'alt': 'Logistics Skill Council'},
            {'img_url': 'images/approvals/tansam_logo.png', 'alt': 'TANSAM Powered by Siemens'},
            {'img_url': 'images/approvals/ndli_logo.png', 'alt': 'National Digital Library of India'},
            {'img_url': 'images/approvals/intel_logo.png', 'alt': 'Intel'},
            {'img_url': 'images/approvals/ibm_logo.png', 'alt': 'IBM'},
        ]

        # Clear existing approvals
        Approval.objects.all().delete()

        # Create new approvals
        for approval in approvals_data:
            Approval.objects.create(img_url=approval['img_url'], alt=approval['alt'])

        self.stdout.write(self.style.SUCCESS('Successfully updated Approval entries'))
