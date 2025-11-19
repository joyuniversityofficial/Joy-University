from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.templatetags.static import static
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.conf import settings as django_settings
from .models import (
    School, Update, Approval, Event, Application, ExecutiveCouncil,
    AcademicCouncil, GoverningCouncil, StudentClub, Infrastructure,
    Library, Hostel, Transportation, Sports, Facilities, PressMedia,
    Enrollment
)
from .forms import (
    OTPLoginForm, OTPVerifyForm, ApplicationForm, LoginForm, ForgotPasswordForm, ContactForm, EnrollmentDetailsForm, DeclarationForm
)
import random
import string
import json
import os

def home(request):
    schools = School.objects.all()
    updates = Update.objects.all()
    approvals = Approval.objects.all()
    context = {
        'schools': schools,
        'updates': updates,
        'approvals': approvals,
    }
    return render(request, 'home.html', context)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            # Send email notification to host
            subject = "New Contact Message from Joy University Website"
            message = f"""
New contact message received:

Name: {contact_message.name}
Email: {contact_message.email}
Phone: {contact_message.phone}
Message: {contact_message.message}

Sent at: {contact_message.created_at}
"""
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],  # Send to host email; adjust if needed
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send contact email: {e}")
            messages.success(request, 'Your message has been sent successfully. We will get back to you soon!')
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def who_we_are(request):
    return render(request, 'who_we_are.html')

def about_us(request):
    return render(request, 'who_we_are/about_us.html')

def chancellor_message(request):
    return render(request, 'who_we_are/chancellor_message.html')

def vice_chancellor_message(request):
    return render(request, 'who_we_are/vice_chancellor_message.html')

def university_organogram(request):
    return render(request, 'who_we_are/university_organogram.html')

def leadership(request):
    return render(request, 'leadership.html')

def pro_chancellor(request):
    return render(request, 'leadership/pro_chancellor.html')

def pro_vice_chancellor_academics(request):
    return render(request, 'leadership/pro_vice_chancellor_academics.html')

def executive_council(request):
    councils = ExecutiveCouncil.objects.all()
    return render(request, 'leadership/executive_council.html', {'councils': councils})

def academic_council(request):
    councils = AcademicCouncil.objects.all()
    return render(request, 'leadership/academic_council.html', {'councils': councils})

def governing_council(request):
    councils = GoverningCouncil.objects.all()
    return render(request, 'leadership/governing_council.html', {'councils': councils})

def schools(request):
    schools = School.objects.all()
    return render(request, 'schools.html', {'schools': schools})

def admissions(request):
    return render(request, 'admissions.html')

def phd_admissions(request):
    return render(request, 'phd-admissions.html')

def placements(request):
    return render(request, 'placements.html')

def student_life(request):
    return render(request, 'student_life.html')

def student_clubs(request):
    clubs = StudentClub.objects.all()
    return render(request, 'student_clubs.html', {'clubs': clubs})

def infrastructure(request):
    infrastructures = Infrastructure.objects.all()
    return render(request, 'student_life/infrastructure.html', {'infrastructures': infrastructures})

def infrastructure_detail(request, slug):
    item = get_object_or_404(Infrastructure, slug=slug)
    gallery_images = [img.image.url for img in item.gallery_images.all()]
    return render(request, 'student_life/infrastructure_detail.html', {'item': item, 'gallery_images': gallery_images})

def library(request):
    libraries = Library.objects.all()
    return render(request, 'student_life/library.html', {'libraries': libraries})

def library_detail(request, slug):
    library = get_object_or_404(Library, slug=slug)
    gallery_images = [img.image.url for img in library.gallery_images.all()]
    return render(request, 'student_life/library_detail.html', {'library': library, 'gallery_images': gallery_images})

def hostels(request):
    hostels = Hostel.objects.all()
    return render(request, 'student_life/hostels.html', {'hostels': hostels})

def hostels_detail(request, slug):
    hostel = get_object_or_404(Hostel, slug=slug)
    gallery_images = [img.image.url for img in hostel.gallery_images.all()]
    return render(request, 'student_life/hostels_detail.html', {'hostel': hostel, 'gallery_images': gallery_images})

def transportation(request):
    transportations = Transportation.objects.all()
    return render(request, 'student_life/transportation.html', {'transportations': transportations})

def transportation_detail(request, slug):
    transportation = get_object_or_404(Transportation, slug=slug)
    gallery_images = [img.image.url for img in transportation.gallery_images.all()]
    return render(request, 'student_life/transportation_detail.html', {'transportation': transportation, 'gallery_images': gallery_images})

def sports(request):
    sports = Sports.objects.all()
    return render(request, 'student_life/sports.html', {'sports': sports})

def sports_detail(request, slug):
    sport = get_object_or_404(Sports, slug=slug)
    gallery_images = [img.image.url for img in sport.gallery_images.all()]
    return render(request, 'student_life/sports_detail.html', {'sport': sport, 'gallery_images': gallery_images})

def virtual_tours(request):
    return render(request, 'student_life/virtual_tours.html')

def facilities(request):
    facilities = Facilities.objects.all()
    return render(request, 'student_life/facilities.html', {'facilities': facilities})

def facilities_detail(request, slug):
    facility = get_object_or_404(Facilities, slug=slug)
    gallery_images = [img.image.url for img in facility.gallery_images.all()]
    return render(request, 'student_life/facilities_detail.html', {'facility': facility, 'gallery_images': gallery_images})

def events(request):
    events = Event.objects.order_by('-date')  # Latest first
    return render(request, 'events.html', {'events': events})

def iqac(request):
    tab = request.GET.get('tab', 'introduction')
    return render(request, 'iqac.html', {'tab': tab})

def alumni(request):
    return render(request, 'alumni.html')

# JU Documents Views
def committees(request):
    context = {'page_title': 'JU Committees', 'current_page': 'committees'}
    return render(request, 'ju_documents/committees.html', context)

def statutes(request):
    context = {'page_title': 'JU Statutes', 'current_page': 'statutes'}
    return render(request, 'ju_documents/statutes.html', context)

def ordinances(request):
    context = {'page_title': 'JU Ordinances', 'current_page': 'ordinances'}
    return render(request, 'ju_documents/ordinances.html', context)

def academic_regulations(request):
    context = {'page_title': 'JU Academic Regulations', 'current_page': 'academic_regulations'}
    return render(request, 'ju_documents/academic_regulations.html', context)

def examination_regulation(request):
    context = {'page_title': 'JU Examination Regulation', 'current_page': 'examination_regulation'}
    return render(request, 'ju_documents/examination_regulation.html', context)

def academic_calendar(request):
    context = {'page_title': 'JU Academic Calendar AY 2025-26', 'current_page': 'academic_calendar'}
    return render(request, 'ju_documents/academic_calendar.html', context)

def leave_rules(request):
    context = {'page_title': 'JU Leave Rules', 'current_page': 'leave_rules'}
    return render(request, 'ju_documents/leave_rules.html', context)

def ndli_member(request):
    context = {'page_title': 'Member, NDLI, Min of Education, Govt of India', 'current_page': 'ndli_member'}
    return render(request, 'ju_documents/ndli_member.html', context)

def ict_academy(request):
    context = {'page_title': 'Member ICT Academy Govt of India', 'current_page': 'ict_academy'}
    return render(request, 'ju_documents/ict_academy.html', context)

def newsletter(request):
    context = {'page_title': 'JU Newsletter', 'current_page': 'newsletter'}
    return render(request, 'ju_documents/newsletter.html', context)

def annual_report(request):
    context = {'page_title': 'JU Annual Report', 'current_page': 'annual_report'}
    return render(request, 'ju_documents/annual_report.html', context)

def mandatory_disclosure(request):
    context = {'page_title': 'Mandatory Disclosure', 'current_page': 'mandatory_disclosure'}
    return render(request, 'ju_documents/mandatory_disclosure.html', context)

def downloads(request):
    pdf_dir = os.path.join(settings.BASE_DIR, 'staticfiles', 'pdfs')
    pdfs = []
    if os.path.exists(pdf_dir):
        for file in os.listdir(pdf_dir):
            if file.endswith('.pdf'):
                # Clean up the name by replacing underscores and capitalizing
                name = file.replace('.pdf', '').replace('_', ' ').title()
                pdfs.append({'name': name, 'file': file})
    context = {'page_title': 'Downloads', 'current_page': 'downloads', 'pdfs': pdfs}
    return render(request, 'ju_documents/downloads.html', context)

def admission_regulations(request):
    context = {'page_title': 'JU Admission Regulations', 'current_page': 'admission_regulations'}
    return render(request, 'ju_documents/admission_regulations.html', context)

def admission_flyer(request):
    context = {'page_title': 'JU Admission Flyer', 'current_page': 'admission_flyer'}
    return render(request, 'ju_documents/admission_flyer.html', context)

def aishe_code(request):
    context = {'page_title': 'AISHE Code', 'current_page': 'aishe_code'}
    return render(request, 'ju_documents/aishe_code.html', context)

def annual_report_24_25(request):
    context = {'page_title': 'JU Annual Report 2024-25', 'current_page': 'annual_report_24_25'}
    return render(request, 'ju_documents/annual_report_24_25.html', context)

def bci(request):
    context = {'page_title': 'BCI', 'current_page': 'bci'}
    return render(request, 'ju_documents/bci.html', context)

def disclaimer(request):
    context = {'page_title': 'Disclaimer', 'current_page': 'disclaimer'}
    return render(request, 'ju_documents/disclaimer.html', context)

def hostel_policy(request):
    context = {'page_title': 'JU Hostel Policy', 'current_page': 'hostel_policy'}
    return render(request, 'ju_documents/hostel_policy.html', context)

def newsletter_24_25(request):
    context = {'page_title': 'JU Newsletter 2024-25', 'current_page': 'newsletter_24_25'}
    return render(request, 'ju_documents/newsletter_24_25.html', context)

def pci(request):
    context = {'page_title': 'PCI', 'current_page': 'pci'}
    return render(request, 'ju_documents/pci.html', context)

def student_code_of_conduct(request):
    context = {'page_title': 'JU Student Code of Conduct', 'current_page': 'student_code_of_conduct'}
    return render(request, 'ju_documents/student_code_of_conduct.html', context)

def tn_gov_gaz_comm(request):
    context = {'page_title': 'TN Government Gazette Committee', 'current_page': 'tn_gov_gaz_comm'}
    return render(request, 'ju_documents/tn_gov_gaz_comm.html', context)

def tn_gov_gaz(request):
    context = {'page_title': 'TN Government Gazette', 'current_page': 'tn_gov_gaz'}
    return render(request, 'ju_documents/tn_gov_gaz.html', context)

def tn_gov_ugc(request):
    context = {'page_title': 'TN Government UGC', 'current_page': 'tn_gov_ugc'}
    return render(request, 'ju_documents/tn_gov_ugc.html', context)

def tn_gov(request):
    context = {'page_title': 'TN Government', 'current_page': 'tn_gov'}
    return render(request, 'ju_documents/tn_gov.html', context)

def tn_pu(request):
    context = {'page_title': 'TN PU', 'current_page': 'tn_pu'}
    return render(request, 'ju_documents/tn_pu.html', context)

def tn_ugc(request):
    context = {'page_title': 'TN UGC', 'current_page': 'tn_ugc'}
    return render(request, 'ju_documents/tn_ugc.html', context)

def transportation_route(request):
    context = {'page_title': 'Transportation Route', 'current_page': 'transportation_route'}
    return render(request, 'ju_documents/transportation_route.html', context)

def ugc(request):
    context = {'page_title': 'UGC', 'current_page': 'ugc'}
    return render(request, 'ju_documents/ugc.html', context)

# Admissions Views

def fee_structure(request):
    return render(request, 'admissions/fee_structure.html')

def international_admissions(request):
    return render(request, 'admissions/international_admissions.html')

def hostel_fee(request):
    return render(request, 'admissions/hostel_fee.html')

def transportation_fee(request):
    return render(request, 'admissions/transportation_fee.html')

def ju_scholarships(request):
    return render(request, 'admissions/ju_scholarships.html')

def tn_government_scholarships(request):
    return render(request, 'admissions/tn_government_scholarships.html')

def achievements(request):
    return render(request, 'other_links/achievements.html')

def visitors(request):
    return render(request, "other_links/visitors.html")

def pressandmedia(request):
    from .models import PressMedia
    press_media = PressMedia.objects.all()
    return render(request, "other_links/press_and_media.html", {'press_media': press_media})

def m_o_u(request):
    return render(request, "other_links/m-o-u.html")

def school_agricultural_sciences(request):
    school = get_object_or_404(School, slug='school-of-agricultural-sciences')
    return render(request, 'school_agricultural_sciences.html', {'school': school})

def school_arts_natural_sciences(request):
    school = get_object_or_404(School, slug='school-of-arts-natural-sciences')
    return render(request, 'school_arts_natural_sciences.html', {'school': school})

def school_computational_intelligence(request):
    school = get_object_or_404(School, slug='school-of-computational-intelligence')
    return render(request, 'school_computational_intelligence.html', {'school': school})

def school_design(request):
    school = get_object_or_404(School, slug='school-of-design')
    return render(request, 'school_design.html', {'school': school})

def school_engineering_technology(request):
    school = get_object_or_404(School, slug='school-of-engineering-technology')
    return render(request, 'school_engineering_technology.html', {'school': school})

def school_entrepreneurship_management(request):
    school = get_object_or_404(School, slug='school-of-entrepreneurship-management')
    return render(request, 'school_entrepreneurship_management.html', {'school': school})

def school_law(request):
    school = get_object_or_404(School, slug='school-of-law')
    return render(request, 'school_law.html', {'school': school})

def school_life_health_sciences(request):
    school = get_object_or_404(School, slug='school-of-life-health-sciences')
    return render(request, 'school_life_health_sciences.html', {'school': school})

def school_nursing(request):
    school = get_object_or_404(School, slug='school-of-nursing')
    return render(request, 'school_nursing.html', {'school': school})

def school_pharmacy(request):
    school = get_object_or_404(School, slug='school-of-pharmacy')
    return render(request, 'school_pharmacy.html', {'school': school})

def application_form(request):
    edit = request.GET.get('edit') == '1'
    app_id = request.GET.get('app_id')

    if edit and app_id:
        # Editing existing application
        try:
            application = Application.objects.get(id=app_id)
            # Security check: ensure the application belongs to the logged-in user
            if request.session.get('application_id') != application.id:
                messages.error(request, 'You do not have permission to edit this application.')
                return redirect('dashboard')
        except Application.DoesNotExist:
            messages.error(request, 'Application not found.')
            return redirect('dashboard')
    else:
        application = None

    # Generate captcha server-side
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    request.session['captcha'] = captcha_text

    # Data for dropdowns
    states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu and Kashmir', 'Ladakh', 'Puducherry', 'Dadra and Nagar Haveli and Daman and Diu', 'Lakshadweep', 'Andaman and Nicobar Islands'
    ]

    schools = list(set(list(School.objects.exclude(slug='school-of-engineering-technology').values_list('title', flat=True)) + ['School of Doctorate']))

    courses = {
    'School of Arts & Natural Sciences': [
        'B.A.',
        'B.Sc.',
        'B.P.Ed.',
        'B.LI.Sc.'
    ],
    'School of Agricultural Sciences': [
        'B.Sc. (Hons.)',
        'B.Tech',
        'M.Sc Agriculture',
        'M.Sc Horticulture'
    ],
    'School of Pharmacy': [
        'B.Pharm.',
        'B.Pharm Lateral'
    ],
    'School of Nursing': [
        'B.Sc.'
    ],
    'School of Entrepreneurship & Management': [
        'BBA',
        'MBA',
        'B.Com',
        'B Com - Face Prep',
        'BBA - Face Prep'
    ],
    'School of Law': [
        'B.B.A. LL.B (Hons)',
        'LL.B (Hons)',
        'B.A. LL.B (Hons)',
        'LL.M'
    ],
    'School of Design': [
        'B.Des'
    ],
    'School of Life & Health Sciences': [
        'B.Sc.',
        'B.Tech',
        'BPT',
        'M.Sc'
    ],
    'School of Computational Intelligence': [
        'B.Tech',
        'B.Tech Lateral',
        'BCA',
        'BCA - Face Prep'
    ],
    'School of Doctorate': [
        'Ph.D'
    ]
    }

    specializations = {
    'School of Arts & Natural Sciences': {
        'B.A.': ['English', 'History', 'Criminology and Police Administration', 'Tamil', 'Economics'],
        'B.Sc.': ['Mathematics', 'Applied Physics', 'Electronics', 'Forensic Science', 'Media & Journalism', 'Psychology'],
        'B.P.Ed.': ['Physical Education'],
        'B.LI.Sc.': ['Library Science'],
    },
    'School of Agricultural Sciences': {
        'B.Sc. (Hons.)': ['Agriculture', 'Horticulture'],
        'B.Tech': ['Agriculture Engineering', 'Dairy Technology'],
        'M.Sc Agriculture': ['Agricultural Entomology', 'Agronomy', 'Agricultural Extension Education'],
        'M.Sc Horticulture': ['Floriculture and Landscaping', 'Vegetable Science'],
    },
    'School of Pharmacy': {
        'B.Pharm.': ['Pharmacy'],
        'B.Pharm Lateral': ['Pharmacy'],
    },
    'School of Nursing': {
        'B.Sc.': ['Nursing'],
    },
    'School of Entrepreneurship & Management': {
        'BBA': ['Business Analytics', 'Digital Marketing', 'Financial Management', 'Logistics and Supply Chain Management', 'Entrepreneurial Management'],
        'MBA': ['Business Analytics', 'Human Resource Management', 'Marketing Management', 'Entrepreneurial Management', 'Digital Transformation', 'Hospital & Health care System Mgmt', 'International Business'],
        'B.Com': ['Accounting & Finance', 'Computer Applications', 'General'],
        'BBA - Face Prep': ['E-Commerce & Digital Marketing'],
        'B Com - Face Prep': ['Fintech with Blockchain'],
    },
    'School of Law': {
        'B.B.A. LL.B (Hons)': ['Law'],
        'LL.B (Hons)': ['Law'],
        'B.A. LL.B (Hons)': ['Law'],
        'LL.M': ['Cyber Crime', 'Taxation'],
    },
    'School of Design': {
        'B.Des': ['Fashion Design', 'Transportation and Automobile Design'],
    },
    'School of Life & Health Sciences': {
        'B.Sc.': ['Biotechnology', 'Operation Theatre and Anaesthesia Technology', 'Cardiac Perfusion Technology', 'Medical Radiology and Imaging Technology', 'Optometry', 'Medical Laboratory Technology', 'Physician Assistant', 'Psychology'],
        'B.Tech': ['Biotechnology', 'Biomedical Engineering'],
        'BPT': ['Bachelor of Physiotherapy'],
        'M.Sc': ['Biotechnology', 'Operation Theatre and Anaesthesia Technology', 'Cardiac Perfusion Technology'],
    },
    'School of Computational Intelligence': {
        'B.Tech': ['CSE (AI & Data Science)', 'CSE (AI and Machine Learning)', 'Computer Science and Engineering', 'CSE (Artificial Intelligence & Machine Learning) INTEL -NEC', 'CSE (Artificial Intelligence & IoT) INTEL -NEC', 'CSE (Cyber Security)', 'CSE (AI & Robotics)', 'Information Communication Technology', 'Civil Engineering', 'Electronics and Communication Engineering', 'Mechanical Engineering', 'Mechatronics', 'Aeronautical Engineering', 'Mathematics & Computing', 'ECE (AI & Machine Learning)', 'CSE (AI & IOT)'],
        'B.Tech Lateral': ['Computer Science and Engineering', 'CSE (AI & Data Science)', 'CSE (AI and Machine Learning)', 'CSE (Artificial Intelligence & Machine Learning) INTEL -NEC', 'CSE (Artificial Intelligence & IoT) INTEL -NEC', 'CSE (Cyber Security)', 'CSE (AI & Robotics)', 'Information Communication Technology', 'Civil Engineering', 'Electronics and Communication Engineering', 'Mechanical Engineering', 'Mechatronics', 'Aeronautical Engineering', 'CSE (AI & IOT)', 'Mathematics & Computing', 'ECE (AI & Machine Learning)'],
        'BCA': ['Artificial Intelligence', 'Cyber Security'],
        'BCA - Face Prep': ['Artificial Intelligence', 'Data Science'],
    },
    'School of Doctorate': {
        'Ph.D': ['Mathematics', 'Physics', 'Psychology', 'History', 'Tamil', 'English', 'Agriculture', 'Computer Science', 'Management', 'Life & Health Sciences', 'Horticulture', 'Civil Engineering', 'Electronics and Communication Engineering', 'Mechanical Engineering', 'Robotics and Automation', 'Economics', 'Commerce', 'Nursing', 'Pharmacy', 'Law', 'Library & Information Science', 'Physical Education'],
    }
}

    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application if edit else None)
        if form.is_valid():
            # Get school title and remove from cleaned_data to prevent save error
            school_title = form.cleaned_data.pop('school')

            # Save application
            application = form.save(commit=False)

            # Generate password for new applications
            if not edit:
                application.password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

            # Set school from title
            if school_title != 'School of Doctorate':
                try:
                    application.school = School.objects.get(title=school_title)
                except School.DoesNotExist:
                    messages.error(request, 'Invalid school selected.')
                    context = {
                        'form': form,
                        'states': states,
                        'schools': schools,
                        'courses_json': json.dumps(courses),
                        'specializations_json': json.dumps(specializations),
                        'captcha_text': captcha_text,
                    }
                    return render(request, 'application_form.html', context)
            else:
                application.school = None  # Handle Doctorate separately if needed
            application.save()

            if edit:
                messages.success(request, 'Application updated successfully.')
                return redirect('dashboard')
            else:
                # Send email with password
                subject = "Welcome to Joy University - Your Application Credentials"
                apply_url = request.build_absolute_uri(reverse('home'))
                message = f"""
<img src="{request.build_absolute_uri(static('images/mailimg.png'))}" alt="Welcome Image"><br>
<p>Now kick-start your academic journey with Joy University!</p>

<p><a href="{apply_url}">Apply Now</a></p>
<p>Step 1: Click on the above link.</p>
<p>Step 2: Access your application dashboard using your login ID & password
(these credentials were shared with you via email earlier at the beginning of the application process and are also mentioned below in this mail)</p>

<p>Username: {application.email}</p>
<p>Password: {application.password}</p>

<p>Best Wishes,</p>
<p>Team Admissions</p>
"""
                try:
                    send_mail(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [application.email],
                        html_message=message,
                        fail_silently=False,
                    )
                    print(f"Email sent successfully to {application.email}")
                except Exception as e:
                    print(f"Failed to send email to {application.email}: {e}")

                messages.success(request, 'Application submitted successfully. Check your email for login credentials.')
                return redirect('thank_you')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ApplicationForm(instance=application if edit else None)
    if edit:
        form.initial['school'] = application.school.title if application.school else 'School of Doctorate'

    context = {
        'form': form,
        'states': states,
        'schools': schools,
        'courses_json': json.dumps(courses),
        'specializations_json': json.dumps(specializations),
        'captcha_text': captcha_text,
    }
    return render(request, 'application_form.html', context)

def get_states(request):
    country = request.GET.get('country')
    states_data = {
        'India': [
            'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu and Kashmir', 'Ladakh', 'Puducherry', 'Dadra and Nagar Haveli and Daman and Diu', 'Lakshadweep', 'Andaman and Nicobar Islands'
        ],
        # Add other countries if needed
    }
    states = states_data.get(country, [])
    return JsonResponse({'states': states})

def get_districts(request):
    state = request.GET.get('state')
    # For simplicity, return empty list as districts are not used extensively
    districts = []
    return JsonResponse({'districts': districts})

def get_cities(request):
    state = request.GET.get('state')
    cities_data = {
        'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Rajahmundry', 'Tirupati', 'Kakinada', 'Anantapur', 'Kadapa', 'Eluru', 'Ongole', 'Chittoor', 'Srikakulam', 'Vizianagaram', 'Parvathipuram', 'Narsipatnam', 'Bhimavaram', 'Tadepalligudem', 'Amalapuram'],
        'Arunachal Pradesh': ['Itanagar', 'Naharlagun', 'Pasighat', 'Along', 'Bomdila', 'Tawang', 'Ziro', 'Tezu', 'Roing', 'Namsai', 'Aalo', 'Daporijo', 'Anini', 'Mechuka', 'Chowkham', 'Dirang', 'Kalaktang', 'Seppa', 'Yingkiong', 'Tuting'],
        'Assam': ['Guwahati', 'Silchar', 'Dibrugarh', 'Jorhat', 'Nagaon', 'Tinsukia', 'Tezpur', 'Bongaigaon', 'Karimganj', 'Sivasagar', 'Goalpara', 'Barpeta', 'Dhubri', 'Diphu', 'North Lakhimpur', 'Hailakandi', 'Morigaon', 'Nalbari', 'Rangia', 'Margherita'],
        'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Darbhanga', 'Arrah', 'Begusarai', 'Chhapra', 'Katihar', 'Munger', 'Purnia', 'Saharsa', 'Sasaram', 'Hajipur', 'Dehri', 'Bettiah', 'Motihari', 'Bagaha', 'Siwan', 'Kishanganj'],
        'Chhattisgarh': ['Raipur', 'Bhilai', 'Bilaspur', 'Korba', 'Durg', 'Rajnandgaon', 'Jagdalpur', 'Raigarh', 'Ambikapur', 'Mahasamund', 'Dhamtari', 'Chirmiri', 'Bhatapara', 'Tilda Newra', 'Naila Janjgir', 'Akaltara', 'Mungeli', 'Baloda Bazar', 'Saraipali', 'Basna'],
        'Goa': ['Panaji', 'Margao', 'Vasco da Gama', 'Mapusa', 'Ponda', 'Bicholim', 'Curchorem', 'Sanquelim', 'Valpoi', 'Quepem', 'Canacona', 'Sanguem', 'Pernem', 'Aldona', 'Tiswadi', 'Bardez', 'Salcete', 'Mormugao', 'Dharbandora', 'Sattari'],
        'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar', 'Jamnagar', 'Junagadh', 'Gandhinagar', 'Nadiad', 'Morvi', 'Surendranagar', 'Gandhidham', 'Veraval', 'Gondal', 'Botad', 'Amreli', 'Deesa', 'Wankaner', 'Limbdi', 'Mahuva'],
        'Haryana': ['Faridabad', 'Gurgaon', 'Panipat', 'Ambala', 'Yamunanagar', 'Rohtak', 'Hisar', 'Karnal', 'Sonipat', 'Panchkula', 'Bhiwani', 'Sirsa', 'Bahadurgarh', 'Jind', 'Thanesar', 'Kaithal', 'Rewari', 'Narnaul', 'Fatehabad', 'Gohana'],
        'Himachal Pradesh': ['Shimla', 'Mandi', 'Solan', 'Nahan', 'Hamirpur', 'Una', 'Palampur', 'Kullu', 'Chamba', 'Bilaspur', 'Kangra', 'Kinnaur', 'Lahaul and Spiti', 'Sirmaur', 'Shimla Rural', 'Mandi Rural', 'Solan Rural', 'Hamirpur Rural', 'Una Rural', 'Palampur Rural'],
        'Jharkhand': ['Ranchi', 'Jamshedpur', 'Dhanbad', 'Bokaro Steel City', 'Deoghar', 'Phusro', 'Adityapur', 'Hazaribagh', 'Giridih', 'Ramgarh', 'Medininagar', 'Chirkunda', 'Sahibganj', 'Saunda', 'Simdega', 'Chatra', 'Gumla', 'Lohardaga', 'Pakur', 'Latehar'],
        'Karnataka': ['Bengaluru', 'Mysuru', 'Hubballi', 'Mangaluru', 'Belagavi', 'Kalaburagi', 'Ballari', 'Vijayapura', 'Shivamogga', 'Tumakuru', 'Raichur', 'Bidar', 'Hospet', 'Gadag', 'Robertsonpet', 'Chitradurga', 'Udupi', 'Mandya', 'Hassan', 'Bagalkot'],
        'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Thrissur', 'Kollam', 'Palakkad', 'Alappuzha', 'Kottayam', 'Idukki', 'Ernakulam', 'Malappuram', 'Wayanad', 'Kannur', 'Kasaragod'],
        'Madhya Pradesh': ['Indore', 'Bhopal', 'Jabalpur', 'Gwalior', 'Ujjain', 'Sagar', 'Dewas', 'Satna', 'Ratlam', 'Rewa', 'Murwara', 'Singrauli', 'Burhanpur', 'Khandwa', 'Bhind', 'Chhindwara', 'Guna', 'Shajapur', 'Sehore', 'Morena'],
        'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Thane', 'Nashik', 'Kalyan-Dombivli', 'Vasai-Virar', 'Aurangabad', 'Navi Mumbai', 'Solapur', 'Mira-Bhayandar', 'Bhiwandi', 'Amravati', 'Nanded', 'Kolhapur', 'Ulhasnagar', 'Sangli-Miraj', 'Malegaon', 'Jalgaon', 'Akola'],
        'Manipur': ['Imphal', 'Thoubal', 'Lilong', 'Mayang Imphal', 'Kakching', 'Ukhrul', 'Churachandpur', 'Bishnupur', 'Moirang', 'Nambol', 'Kumbi', 'Yairipok', 'Wangjing', 'Sugnu', 'Jiribam', 'Moreh', 'Lamlai', 'Tamenglong', 'Chandel', 'Senapati'],
        'Meghalaya': ['Shillong', 'Tura', 'Jowai', 'Nongstoin', 'Williamnagar', 'Baghmara', 'Resubelpara', 'Nongpoh', 'Mairang', 'Khliehriat', 'Mawkyrwat', 'Pynursla', 'Amlarem', 'Madanrting', 'Nongthymmai', 'Cherrapunjee', 'Mawsynram', 'Sohra', 'Byrnihat', 'Ranikor'],
        'Mizoram': ['Aizawl', 'Lunglei', 'Saiha', 'Champhai', 'Serchhip', 'Kolasib', 'Lawngtlai', 'Mamit', 'Hnahthial', 'Khawzawl', 'North Vanlaiphai', 'Saitual', 'Vairengte', 'Darlawn', 'Biate', 'Reiek', 'S Bungtlang', 'Thingsulthliah', 'Phullen', 'Tlabung'],
        'Nagaland': ['Kohima', 'Dimapur', 'Mokokchung', 'Tuensang', 'Wokha', 'Zunheboto', 'Mon', 'Phek', 'Kiphire', 'Longleng', 'Peren', 'Chumukedima', 'Medziphema', 'Pfutsero', 'Chakhesang', 'Tseminyu', 'Noklak', 'Shamator', 'Tuli', 'Satoi'],
        'Odisha': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Berhampur', 'Sambalpur', 'Puri', 'Balasore', 'Bhadrak', 'Baripada', 'Jharsuguda', 'Jeypore', 'Brajarajnagar', 'Angul', 'Talcher', 'Sundargarh', 'Subarnapur', 'Kendujhar', 'Paradip', 'Dhenkanal', 'Bargarh'],
        'Punjab': ['Ludhiana', 'Amritsar', 'Jalandhar', 'Patiala', 'Bathinda', 'Hoshiarpur', 'Mohali', 'Batala', 'Pathankot', 'Moga', 'Abohar', 'Malerkotla', 'Khanna', 'Phagwara', 'Muktsar', 'Barnala', 'Rajpura', 'Firozpur', 'Kapurthala', 'Faridkot'],
        'Rajasthan': ['Jaipur', 'Jodhpur', 'Kota', 'Bikaner', 'Ajmer', 'Udaipur', 'Bhilwara', 'Alwar', 'Bharatpur', 'Sikar', 'Pali', 'Tonk', 'Kishangarh', 'Beawar', 'Hanumangarh', 'Dhaulpur', 'Gangapur City', 'Sawai Madhopur', 'Churu', 'Jhunjhunu'],
        'Sikkim': ['Gangtok', 'Namchi', 'Gyalshing', 'Mangan', 'Singtam', 'Rangpo', 'Jorethang', 'Soreng', 'Pakyong', 'Ravangla', 'Naya Bazar', 'Samdrup Jongkhar', 'Geyzing', 'Lachung', 'Yumthang', 'Dentam', 'Rinchenpong', 'Temi', 'Martam', 'Bermiok'],
        'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Tirunelveli', 'Salem', 'Erode', 'Tiruppur', 'Vellore', 'Thoothukudi', 'Kanyakumari', 'Ramanathapuram', 'Sivaganga', 'Virudhunagar', 'Theni', 'Dindigul', 'Karur', 'Namakkal', 'Dharmapuri', 'Krishnagiri', 'Tiruvannamalai', 'Cuddalore', 'Villupuram', 'Kancheepuram', 'Tiruvallur', 'Nilgiris'],
        'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Khammam', 'Karimnagar', 'Ramagundam', 'Mahbubnagar', 'Nalgonda', 'Adilabad', 'Suryapet', 'Miryalaguda', 'Jagtial', 'Wanaparthy', 'Vikarabad', 'Jangaon', 'Gadwal', 'Kamareddy', 'Palwancha', 'Kothagudem', 'Bodhan'],
        'Tripura': ['Agartala', 'Udaipur', 'Dharmanagar', 'Pratapgarh', 'Kailasahar', 'Belonia', 'Khowai', 'Teliamura', 'Ambassa', 'Bishalgarh', 'Sonamura', 'Melaghar', 'Mohanpur', 'Sabroom', 'Jirania', 'Santirbazar', 'Gakulnagar', 'Radhakishorepur', 'Matabari', 'Kamalpur'],
        'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Ghaziabad', 'Agra', 'Meerut', 'Varanasi', 'Allahabad', 'Bareilly', 'Aligarh', 'Moradabad', 'Saharanpur', 'Gorakhpur', 'Noida', 'Firozabad', 'Loni', 'Jhansi', 'Muzaffarnagar', 'Mathura', 'Shahjahanpur', 'Rampur'],
        'Uttarakhand': ['Dehradun', 'Haridwar', 'Roorkee', 'Haldwani', 'Rudrapur', 'Kashipur', 'Rishikesh', 'Pithoragarh', 'Pantnagar', 'Almora', 'Mussoorie', 'Tehri', 'Pauri', 'Nainital', 'Ranikhet', 'Bageshwar', 'Champawat', 'Lohaghat', 'Dwarahat', 'Bhimtal'],
        'West Bengal': ['Kolkata', 'Howrah', 'Durgapur', 'Asansol', 'Siliguri', 'Maheshtala', 'Rajpur Sonarpur', 'South Dum Dum', 'Bhatpara', 'Panihati', 'Kamarhati', 'Bardhaman', 'Kulti', 'Baharampur', 'Hugli-Chinsurah', 'Shantipur', 'Krishnanagar', 'Naihati', 'Uluberia', 'Jalpaiguri'],
        'Delhi': ['New Delhi', 'Delhi'],
        'Jammu and Kashmir': ['Srinagar', 'Jammu', 'Anantnag', 'Baramulla', 'Pulwama', 'Shopian', 'Kupwara', 'Bandipora', 'Ganderbal', 'Kulgam', 'Budgam', 'Ramban', 'Doda', 'Kishtwar', 'Udhampur', 'Reasi', 'Rajouri', 'Poonch', 'Kathua', 'Samba'],
        'Ladakh': ['Leh', 'Kargil'],
        'Puducherry': ['Puducherry', 'Karaikal', 'Mahe', 'Yanam'],
        'Dadra and Nagar Haveli and Daman and Diu': ['Daman', 'Diu', 'Silvassa'],
        'Lakshadweep': ['Kavaratti', 'Agatti', 'Amini', 'Kadmat', 'Kiltan', 'Chetlat', 'Bitra', 'Androth', 'Kalpeni', 'Minicoy'],
        'Andaman and Nicobar Islands': ['Port Blair', 'Havelock Island', 'Neil Island', 'Diglipur', 'Mayabunder', 'Rangat', 'Little Andaman', 'Car Nicobar', 'Nancowry', 'Campbell Bay'],
    }
    cities = cities_data.get(state, [])
    return JsonResponse({'cities': cities})

def refresh_captcha(request):
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    request.session['captcha'] = captcha_text
    return JsonResponse({'captcha': captcha_text})

def thank_you(request):
    return render(request, 'thank_you.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].strip().lower()
            password = form.cleaned_data['password'].strip()
            print(f"Login attempt: email='{email}', password='{password}'")
            # Try exact match first
            application = Application.objects.filter(email=email, password=password).first()
            if not application:
                # Try case-insensitive email match
                application = Application.objects.filter(email__iexact=email, password=password).first()
            print(f"Found application: {application}")
            if application:
                request.session['application_id'] = application.id
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def dashboard_view(request):
    application_id = request.session.get('application_id')
    if not application_id:
        return redirect('login')
    try:
        application = Application.objects.get(id=application_id)
    except Application.DoesNotExist:
        del request.session['application_id']
        return redirect('login')
    initials = ''.join([word[0].upper() for word in application.name.split()])
    if application.status == 'enrolled':
        apply_url = reverse('application_submitted')
    else:
        apply_url = reverse('details') + f'?app_id={application.id}'
    context = {
        'application': application,
        'initials': initials,
        'apply_url': apply_url
    }
    return render(request, 'dashboard.html', context)

def all_applications_view(request):
    application_id = request.session.get('application_id')
    if not application_id:
        return redirect('login')
    try:
        application = Application.objects.get(id=application_id)
        school_applications = [application]  # Assuming one application per user for now
        initials = ''.join([word[0].upper() for word in application.name.split()])
        context = {
            'application': application,
            'school_applications': school_applications,
            'initials': initials,
        }
        return render(request, 'all_applications.html', context)
    except Application.DoesNotExist:
        del request.session['application_id']
        return redirect('login')

def forgot_password_view(request):
    from .forms import ForgotPasswordForm
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                application = Application.objects.filter(email=email).first()
                if not application:
                    raise Application.DoesNotExist
                subject = "Your Password for Joy University Application"
                apply_url = request.build_absolute_uri(reverse('home'))
                message = f"""
<img src="{request.build_absolute_uri(static('images/mailimg.png'))}" alt="Welcome Image"><br>
<p>Now kick-start your academic journey with Joy University!</p>

<p><a href="{apply_url}">Apply Now</a></p>
<p>Step 1: Click on the above link.</p>
<p>Step 2: Access your application dashboard using your login ID & password
(these credentials were shared with you via email earlier at the beginning of the application process and are also mentioned below in this mail)</p>

<p>Username: {application.email}</p>
<p>Password: {application.password}</p>

<p>Best Wishes,</p>
<p>Team Admissions</p>
"""
                from django.core.mail import send_mail
                from django.conf import settings
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    html_message=message,
                    fail_silently=False,
                )
                messages.success(request, 'Password sent to your email.')
                return redirect('login')
            except Application.DoesNotExist:
                messages.error(request, 'Email not found.')
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {'form': form})

def otp_login_view(request):
    if request.method == 'POST':
        form = OTPLoginForm(request.POST)
        if form.is_valid():
            contact = form.cleaned_data['contact']
            try:
                # Check if contact is email or mobile
                if '@' in contact:
                    application = Application.objects.filter(email=contact).first()
                else:
                    # Assume it's mobile, but since mobile is stored with country code, need to handle
                    # For simplicity, assume contact is email for now, or add logic
                    application = Application.objects.filter(mobile=contact).first()
                if application:
                    # Generate OTP
                    otp = ''.join(random.choices(string.digits, k=6))
                    application.otp_code = otp
                    application.otp_expires_at = timezone.now() + timezone.timedelta(minutes=10)
                    application.save()
                    # Send OTP via email (for now, since mobile SMS not implemented)
                    subject = "Your OTP for Joy University Login"
                    message = f"Your OTP is {otp}. It expires in 10 minutes."
                    send_mail(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [application.email],
                        fail_silently=False,
                    )
                    request.session['otp_contact'] = contact
                    messages.success(request, 'OTP sent to your email.')
                    return redirect('otp_verify')
                else:
                    messages.error(request, 'Contact not found.')
            except Exception as e:
                messages.error(request, 'An error occurred. Please try again.')
    else:
        form = OTPLoginForm()
    return render(request, 'otp_login.html', {'form': form})

def otp_verify_view(request):
    contact = request.session.get('otp_contact')
    if not contact:
        return redirect('otp_login')
    if request.method == 'POST':
        form = OTPVerifyForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp_code']
            try:
                if '@' in contact:
                    application = Application.objects.filter(email=contact).first()
                else:
                    application = Application.objects.filter(mobile=contact).first()
                if application and application.otp_code == otp_code and application.otp_expires_at > timezone.now():
                    request.session['application_id'] = application.id
                    del request.session['otp_contact']
                    application.otp_code = None
                    application.otp_expires_at = None
                    application.save()
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid or expired OTP.')
            except Exception as e:
                messages.error(request, 'An error occurred. Please try again.')
    else:
        form = OTPVerifyForm()
    return render(request, 'otp_verify.html', {'form': form})

def all_applications(request):
    application_id = request.session.get('application_id')
    if not application_id:
        return redirect('login')
    try:
        application = Application.objects.get(id=application_id)
    except Application.DoesNotExist:
        del request.session['application_id']
        return redirect('login')

    # Get all applications for the user by email
    user_applications = Application.objects.filter(email=application.email)
    school_applications = []

    for app in user_applications:
        enrollment = None
        if app.status == 'enrolled':
            enrollment = Enrollment.objects.filter(application=app).first()
        school_applications.append({
            'application': app,
            'enrollment': enrollment,
            'title': app.school.title if app.school else 'School of Doctorate'
        })

    # Check if user has already enrolled in any school
    enrolled_application = user_applications.filter(status='enrolled').first()
    enrolled_school_name = enrolled_application.school.title if enrolled_application and enrolled_application.school else None

    initials = ''.join([word[0].upper() for word in application.name.split()])

    context = {
        'application': application,
        'school_applications': school_applications,
        'initials': initials,
        'enrolled_school_name': enrolled_school_name
    }
    return render(request, 'all_applications.html', context)


# Enrollment Views

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.units import mm
from io import BytesIO

def preview_view(request):
    # Assuming you have stored the latest form data in session or DB
    application_id = request.session.get('application_id')

    if not application_id:
        return redirect('details')

    application = Application.objects.get(id=application_id)
    enrollment = Enrollment.objects.filter(application=application).first()

    if not enrollment:
        messages.error(request, 'Enrollment details not found.')
        return redirect('details')

    # Set application number from application if not set
    if not enrollment.application_number:
        enrollment.application_number = enrollment.application.application_number
        enrollment.save()

    # Use current date if submitted_at is None
    display_date = enrollment.submitted_at if enrollment.submitted_at else timezone.now().date()

    # Render the HTML preview (styled like the PDF)
    return render(request, 'enrollment/preview.html', {'application': application, 'enrollment': enrollment, 'display_date': display_date})


def preview_pdf(request):
    import os
    from django.conf import settings
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib import colors
    from reportlab.lib.units import mm
    from io import BytesIO
    from django.utils import timezone

    app_id = request.session.get('application_id')
    if not app_id:
        return redirect('details')

    application = Application.objects.filter(id=app_id).first()
    enrollment = Enrollment.objects.filter(application=application).first()

    if not enrollment:
        messages.error(request, "Enrollment record not found.")
        return redirect("details")

    if not enrollment.application_number:
        enrollment.application_number = enrollment.application.application_number
        enrollment.save()

    display_date = enrollment.submitted_at or timezone.now().date()

    # PDF Layout
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=6*mm,
        rightMargin=6*mm,
        topMargin=6*mm,
        bottomMargin=6*mm
    )

    # Font styles
    NORMAL = ParagraphStyle("n", fontName="Helvetica", fontSize=10, leading=12)
    BOLD = ParagraphStyle("b", fontName="Helvetica-Bold", fontSize=10, leading=12)
    SECTION = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=12, leading=14)

    # Helper
    def bold(t): return Paragraph(f"<b>{t}</b>", BOLD)
    def val(t): return Paragraph(str(t if t else ""), NORMAL)

    # Get title + logo
    school_title = (
        enrollment.application.school.title
        if enrollment.application and enrollment.application.school
        else "School of Doctorate"
    )

    logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'joy_university.png')
    logo = Image(logo_path, width=24*mm, height=12*mm)

    # Title row (Logo LEFT + Title CENTER)
    title_row = Table(
        [
            [
                logo,
                Paragraph(f"<b>{school_title} Application Form</b>",
                          ParagraphStyle("title", fontName="Helvetica-Bold",
                                         alignment=1, fontSize=13)),
                ""
            ]
        ],
        colWidths=[26*mm, 130*mm, 15*mm]
    )

    # ===========================================
    # FINAL TABLE → ONLY 4 COLUMNS
    # ===========================================
    COLS = [32*mm, 50*mm, 32*mm, 50*mm]

    rows = []

    # Title Row (spans entire width)
    rows.append([title_row, "", "", ""])

    # Application Number
    rows.append([
        Paragraph(f"Application No: {enrollment.application_number}",
                  ParagraphStyle("an", alignment=2, fontSize=9)),
        "", "", ""
    ])

    # -------------------------------
    # COURSE DETAILS
    # -------------------------------
    rows.append([Paragraph("<b>Course Details</b>", SECTION), "", "", ""])
    rows.append([
        bold("Level of Program"), val(enrollment.program_level),
        bold("Course"), val(enrollment.course)
    ])
    rows.append([
        bold("Specialization"), val(enrollment.specialization),
        "", ""
    ])

    # -------------------------------
    # PERSONAL DETAILS
    # -------------------------------
    rows.append([Paragraph("<b>Personal Details</b>", SECTION), "", "", ""])

    rows.append([
        bold("Name of the Student"),
        val(f"{enrollment.first_name} {enrollment.last_name}"),
        "", ""
    ])

    rows.append([
        bold("Nationality"), val(enrollment.nationality),
        bold("Accommodation Status"), val(enrollment.accommodation_status)
    ])

    rows.append([
        bold("Mobile Number"), val("+91 " + str(application.mobile)),
        bold("Email ID"), val(enrollment.email)
    ])

    rows.append([
        bold("Date Of Birth"), val(enrollment.dob.strftime("%d/%m/%Y")),
        bold("Aadhaar Number"), val(enrollment.aadhaar)
    ])

    rows.append([
        bold("Gender"), val(enrollment.gender),
        bold("Category"), val(enrollment.category)
    ])

    rows.append([
        bold("Religion"), val(enrollment.religion),
        bold("How did you hear about us?"), val(enrollment.application.how_heard)
    ])

    # -------------------------------
    # GUARDIAN
    # -------------------------------
    rows.append([Paragraph("<b>Father’s / Guardian’s Details</b>", SECTION), "", "", ""])
    rows.append([
        bold("Name"), val(enrollment.parent_name),
        bold("Mobile Number"), val("+91 " + str(enrollment.parent_mobile))
    ])
    rows.append([
        bold("Email ID"), val(enrollment.parent_email),
        "", ""
    ])

    # -------------------------------
    # PASSPORT DETAILS
    # -------------------------------
    rows.append([Paragraph("<b>Passport Details</b>", SECTION), "", "", ""])
    rows.append([
        bold("Passport Number"), val(enrollment.passport_number),
        bold("Country Name"), val(enrollment.passport_country)
    ])
    rows.append([
        bold("Place Of Issue"), val(enrollment.passport_place),
        bold("Date Of Issue"), val(enrollment.passport_issue_date)
    ])
    rows.append([
        bold("Date Of Expiry"), val(enrollment.passport_expiry_date),
        "", ""
    ])

    # -------------------------------
    # ADDRESS
    # -------------------------------
    rows.append([Paragraph("<b>Address For Correspondence</b>", SECTION), "", "", ""])
    rows.append([
        bold("Country"), val(enrollment.country),
        bold("State"), val(enrollment.state)
    ])
    rows.append([
        bold("District"), val(enrollment.district),
        bold("City"), val(enrollment.city)
    ])
    rows.append([
        bold("Pincode"), val(enrollment.pincode),
        bold("Address"), val(f"{enrollment.address_line1} {enrollment.address_line2}")
    ])

    # -------------------------------
    # X Standard
    # -------------------------------
    rows.append([Paragraph("<b>X Standard / Matric Details</b>", SECTION), "", "", ""])
    rows.append([
        bold("School Name"), val(enrollment.x_school),
        bold("State"), val(enrollment.x_state)
    ])
    rows.append([
        bold("City"), val(enrollment.x_city),
        bold("Board"), val(enrollment.x_board)
    ])
    rows.append([
        bold("Percentage"), val(enrollment.x_percentage),
        bold("After Xth Qualification"), val(enrollment.x_after_qualification)
    ])

    # -------------------------------
    # Intermediate
    # -------------------------------
    rows.append([Paragraph("<b>Higher Secondary / 10+2 Details</b>", SECTION), "", "", ""])
    rows.append([
        bold("School Name"), val(enrollment.hs_school),
        bold("State"), val(enrollment.hs_state)
    ])
    rows.append([
        bold("City"), val(enrollment.hs_city),
        bold("Board"), val(enrollment.hs_board)
    ])
    rows.append([
        bold("Result Status"), val(enrollment.hs_result_status),
        bold("Percentage"), val(enrollment.hs_percentage)
    ])

    # -------------------------------
    # Diploma
    # -------------------------------
    rows.append([Paragraph("<b>Diploma Details</b>", SECTION), "", "", ""])
    rows.append([
        bold("Board / University Name"), val(enrollment.diploma_university),
        bold("Diploma Result Status"), val(enrollment.diploma_status)
    ])
    rows.append([
        bold("Diploma Percentage"), val(enrollment.diploma_percentage),
        "", ""
    ])

    # -------------------------------
    # DECLARATION
    # -------------------------------
    rows.append([Paragraph("<b>Declaration</b>", SECTION), "", "", ""])
    rows.append([
        Paragraph(
            "I certify that the information submitted by me in support of this application, "
            "is true to the best of my knowledge and belief. I undertake to abide by the "
            "disciplinary rules and regulations of the institute.",
            NORMAL
        ),
        "", "", ""
    ])
    rows.append([
        bold("Applicant Name"), val(f"{enrollment.first_name} {enrollment.last_name}"),
        bold("Parent Name"), val(enrollment.parent_name)
    ])
    rows.append([
        bold("Date"), val(display_date.strftime("%d/%m/%Y")),
        "", ""
    ])

    # Build final table
    table = Table(rows, colWidths=COLS)

    style = TableStyle([
        ('GRID', (0,0), (-1,-1), 0.7, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ])

    # Section headers → full span
    for i, row in enumerate(rows):
        if row[1] == row[2] == row[3] == "":
            style.add('SPAN', (0, i), (3, i))
            style.add('BACKGROUND', (0, i), (3, i), colors.skyblue)

    # Student name row → span
    for i, row in enumerate(rows):
        if row[2] == row[3] == "":
            style.add('SPAN', (1, i), (3, i))

    table.setStyle(style)

    # Output
    doc.build([table])
    buffer.seek(0)

    return HttpResponse(buffer, content_type="application/pdf")



def details(request):
    application_id = request.session.get('application_id')
    if not application_id:
        return redirect('login')
    try:
        application = Application.objects.get(id=application_id)
    except Application.DoesNotExist:
        del request.session['application_id']
        return redirect('login')

    # Check if enrollment already exists for this application
    existing_enrollment = Enrollment.objects.filter(application=application).first()

    if request.method == 'POST':
        form = EnrollmentDetailsForm(request.POST, instance=existing_enrollment)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.application = application
            # Clear parent_email if it matches the host email
            if enrollment.parent_email == django_settings.EMAIL_HOST_USER:
                enrollment.parent_email = None
            enrollment.save()
            messages.success(request, 'Details saved successfully.')
            return redirect('declaration')
    else:
        # Pre-fill form with application data or existing enrollment data
        if existing_enrollment:
            # Clear parent_email if it matches the host email before creating form
            if existing_enrollment.parent_email == django_settings.EMAIL_HOST_USER:
                existing_enrollment.parent_email = None
                existing_enrollment.save()
            form = EnrollmentDetailsForm(instance=existing_enrollment)
        else:
            name_parts = application.name.split(' ', 1)
            first_name = name_parts[0] if name_parts else ''
            last_name = name_parts[1] if len(name_parts) > 1 else ''
            initial_data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': application.email,
                'mobile': application.mobile,
                'course': application.course,
                'specialization': application.specialization,
                'country': 'India',  # Default to India
                'state': application.state,
                'city': application.city,  # Leave blank for manual entry
                'how_heard': application.how_heard,
            }
            form = EnrollmentDetailsForm(initial=initial_data)

    context = {
        'form': form,
        'application': application,
    }
    return render(request, 'enrollment/details.html', context)


def declaration(request):
    application_id = request.session.get('application_id')
    if not application_id:
        return redirect('login')
    try:
        application = Application.objects.get(id=application_id)
        enrollment = Enrollment.objects.filter(application=application).first()
        if not enrollment:
            messages.error(request, 'Enrollment details not found.')
            return redirect('details')
    except Application.DoesNotExist:
        del request.session['application_id']
        return redirect('login')

    if request.method == 'POST':
        enrollment.declaration_agreed = True
        enrollment.submitted_at = timezone.now()
        enrollment.application_number = enrollment.application.application_number
        enrollment.save()
        # Update application status to enrolled
        application.status = 'enrolled'
        application.save()
        messages.success(request, 'Application submitted successfully.')
        return redirect('application_submitted')

    # Get school name from application
    school_name = application.school.title if application.school else 'Computational Intelligence'

    # Pre-fill data for form
    applicant_name = f"{enrollment.first_name} {enrollment.last_name}"
    parent_name = enrollment.parent_name
    current_date = timezone.now().date()

    form = DeclarationForm(initial={
        'applicant_name': applicant_name,
        'parent_name': parent_name,
        'declaration_date': current_date,
    })

    context = {
        'enrollment': enrollment,
        'application': application,
        'school_name': school_name,
        'form': form,
        'progress_percentage': 86,
        'step_number': 3,
    }
    return render(request, 'enrollment/declaration.html', context)


def application_submitted(request):
    application_id = request.session.get('application_id')
    if not application_id:
        return redirect('login')
    try:
        application = Application.objects.get(id=application_id)
        enrollment = Enrollment.objects.filter(application=application).first()
        if not enrollment:
            messages.error(request, 'Enrollment details not found.')
            return redirect('details')
    except Application.DoesNotExist:
        del request.session['application_id']
        return redirect('login')

    context = {
        'enrollment': enrollment,
        'application': application,
    }
    return render(request, 'enrollment/application_submitted.html', context)


def logout_view(request):
    if 'application_id' in request.session:
        del request.session['application_id']
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')





