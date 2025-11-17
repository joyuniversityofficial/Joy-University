
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
import secrets

class School(models.Model):
    icon = models.CharField(max_length=50)  # FontAwesome icon class
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title





class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    country_code = models.CharField(max_length=10, default='+91')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    course = models.CharField(max_length=200, blank=True)
    specialization = models.CharField(max_length=200, blank=True)
    captcha = models.CharField(max_length=10)  # Assuming simple captcha
    authorization = models.BooleanField(default=False)
    password = models.CharField(max_length=128, blank=True, null=True)  # Self-generated password
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    application_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('initiated', 'Application Initiated'),
            ('completed', 'Application Completed'),
            ('enrolled', 'Enrolled'),
        ],
        default='initiated'
    )
    how_heard = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        pass

    def save(self, *args, **kwargs):
        if not self.password:
            import hashlib
            self.password = hashlib.sha256(self.email.encode()).hexdigest()[:8]
        self.email = self.email.strip().lower() if self.email else self.email
        super().save(*args, **kwargs)
        if not self.application_number:
            prefix = getattr(settings, "APPLICATION_PREFIX", "JU")
            start = int(getattr(settings, "APPLICATION_START", 10000))
            seq = start + (self.pk or 0)
            self.application_number = f"{prefix}{seq}"
            super().save(update_fields=['application_number'])

    def __str__(self):
        return f"{self.name} - {self.email}"


class SchoolDetail(models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE, related_name='details')
    overview = models.TextField(blank=True)
    programmes_offered = models.TextField(blank=True)
    programme_structure_eligibility = models.TextField(blank=True)
    gallery = models.TextField(blank=True)  # Could be JSON for image URLs
    learning_outcomes = models.TextField(blank=True)
    expected_graduate_attributes = models.TextField(blank=True)
    new_targeted_skill_sets = models.TextField(blank=True)
    philosophy = models.TextField(blank=True)
    objectives = models.TextField(blank=True)
    faculty_staff = models.TextField(blank=True)

    def __str__(self):
        return f"Details for {self.school.title}"

class Update(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Approval(models.Model):
    img_url = models.CharField(max_length=255)  # Path to image
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.alt

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='events/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.date})"

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='faculty_photos/')
    qualifications = models.TextField()
    designation = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class StudentClub(models.Model):
    name = models.CharField(max_length=200)
    faculty_advisor = models.CharField(max_length=200)
    about = models.TextField()

    def __str__(self):
        return self.name

class CampusTourRegistration(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    date_of_visit = models.DateField()
    time_of_visit = models.TimeField()
    no_of_people = models.PositiveIntegerField()
    purpose_of_visit = models.TextField()
    degree_interested = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date_of_visit}"

class ExecutiveCouncil(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    membership_in_council = models.TextField()

    def __str__(self):
        return self.name

class AcademicCouncil(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    membership_in_council = models.TextField()

    def __str__(self):
        return self.name

class GoverningCouncil(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    membership_in_council = models.TextField()

    def __str__(self):
        return self.name



class Infrastructure(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='infrastructure/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class InfrastructureImage(models.Model):
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='infrastructure/gallery/')

    def __str__(self):
        return f"Image for {self.infrastructure.title}"

class Library(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='library/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class LibraryImage(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='library/gallery/')

    def __str__(self):
        return f"Image for {self.library.title}"

class Hostel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hostels/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class HostelImage(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='hostels/gallery/')

    def __str__(self):
        return f"Image for {self.hostel.title}"

class Transportation(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='transportation/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class TransportationImage(models.Model):
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='transportation/gallery/')

    def __str__(self):
        return f"Image for {self.transportation.title}"

class Sports(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sports/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class SportsImage(models.Model):
    sports = models.ForeignKey(Sports, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='sports/gallery/')

    def __str__(self):
        return f"Image for {self.sports.title}"

class Facilities(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='facilities/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class FacilitiesImage(models.Model):
    facilities = models.ForeignKey(Facilities, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='facilities/gallery/')

    def __str__(self):
        return f"Image for {self.facilities.title}"

class PressMedia(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='press_media/')

    def __str__(self):
        return self.title

class Course(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.school.title})"

class Specialization(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='specializations')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.course.name})"





class Enrollment(models.Model):
    # Step 1 – personal & academic
    application = models.OneToOneField(Application, on_delete=models.PROTECT, related_name="enrollment", null=True, blank=True)
    nationality = models.CharField(max_length=50, default="Indian")
    program_level = models.CharField(max_length=50)  # UG/PG/...
    course = models.CharField(max_length=100)
    specialization = models.CharField(max_length=120)
    accommodation_status = models.CharField(max_length=20, choices=[("Day Scholar", "Day Scholar"), ("Hosteller", "Hosteller")])

    # personal
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=15)
    aadhaar = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{12}$', 'Aadhaar must be 12 digits')])
    religion = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

    # address
    country = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    district = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    pincode = models.CharField(max_length=10)

    # parent
    parent_name = models.CharField(max_length=120)
    parent_mobile = models.CharField(max_length=20)
    parent_email = models.EmailField(blank=True, null=True)

    # academics – X / 10th
    x_school = models.CharField(max_length=160)
    x_board = models.CharField(max_length=40)
    x_state = models.CharField(max_length=60)
    x_city = models.CharField(max_length=60)
    x_percentage = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    x_after_qualification = models.CharField(max_length=20)  # HSC/Diploma/Both

    # academics – 10+2
    hs_school = models.CharField(max_length=160)
    hs_state = models.CharField(max_length=60)
    hs_city = models.CharField(max_length=60)
    hs_board = models.CharField(max_length=40)
    hs_percentage = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    hs_result_status = models.CharField(max_length=20)  # Declared/Awaited

    # academics – Diploma
    diploma_university = models.CharField(max_length=160, blank=True, null=True)
    diploma_status = models.CharField(max_length=20, blank=True, null=True)  # Declared/Awaited
    diploma_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])

    # referral
    has_consultant_code = models.BooleanField(default=False)
    consultant_code = models.CharField(max_length=20, blank=True)

    # passport details
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    passport_country = models.CharField(max_length=60, blank=True, null=True)
    passport_place = models.CharField(max_length=100, blank=True, null=True)
    passport_issue_date = models.DateField(blank=True, null=True)
    passport_expiry_date = models.DateField(blank=True, null=True)

    # Step 2 – declaration & final
    declaration_agreed = models.BooleanField(default=False)
    application_number = models.CharField(max_length=40, blank=True, null=True, unique=True)
    submitted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.application_number or f"Enrollment for {self.first_name} {self.last_name}"

    def generate_application_number(self):
        prefix = getattr(settings, "APPLICATION_PREFIX", "JU")
        start = int(getattr(settings, "APPLICATION_START", 10000))
        seq = start + (self.pk or 0)
        return f"{prefix}{seq}"


