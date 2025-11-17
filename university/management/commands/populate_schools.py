from django.core.management.base import BaseCommand
from university.models import School

class Command(BaseCommand):
    help = 'Populate School model with initial data'

    def handle(self, *args, **options):
        school_data = [
            {
                "icon": "fas fa-seedling",
                "title": "School of Agricultural Sciences",
                "description": "Dedicated to advancing knowledge in agriculture, focusing on sustainable practices, crop science, and rural development.",
            },
            {
                "icon": "fas fa-atom",
                "title": "School of Arts & Natural Sciences",
                "description": "Exploring the wonders of arts, humanities, and natural sciences through interdisciplinary research and education.",
            },
            {
                "icon": "fas fa-brain",
                "title": "School of Computational Intelligence",
                "description": "Leading in artificial intelligence, machine learning, and computational technologies for innovative solutions.",
            },
            {
                "icon": "fas fa-palette",
                "title": "School of Design",
                "description": "Fostering creativity and innovation in design, from graphic arts to product development.",
            },
            {
                "icon": "fas fa-cogs",
                "title": "School of Engineering & Technology",
                "description": "Engineering excellence in various disciplines, driving technological advancements and industry solutions.",
            },
            {
                "icon": "fas fa-briefcase",
                "title": "School of Entrepreneurship & Management",
                "description": "Cultivating entrepreneurial skills and management expertise for business leaders of tomorrow.",
            },
            {
                "icon": "fas fa-gavel",
                "title": "School of Law",
                "description": "Providing comprehensive legal education and promoting justice, ethics, and legal scholarship.",
            },
            {
                "icon": "fas fa-heartbeat",
                "title": "School of Life & Health Sciences",
                "description": "Advancing health sciences, biotechnology, and life sciences for better human well-being.",
            },
            {
                "icon": "fas fa-user-md",
                "title": "School of Nursing",
                "description": "Training compassionate nurses and healthcare professionals with a focus on patient care and medical ethics.",
            },
            {
                "icon": "fas fa-pills",
                "title": "School of Pharmacy",
                "description": "Innovating in pharmaceutical sciences, drug development, and healthcare delivery systems.",
            },
        ]

        for school in school_data:
            obj, created = School.objects.get_or_create(
                title=school["title"],
                defaults={
                    "icon": school["icon"],
                    "description": school["description"],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added school: {school["title"]}'))
            else:
                self.stdout.write(f'School already exists: {school["title"]}')
