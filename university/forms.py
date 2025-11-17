from django import forms
from .models import ContactMessage, Application, Enrollment, School

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'email-input', 'placeholder': 'Enter your email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'password-input', 'placeholder': 'Enter your password'}))

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'email-input', 'placeholder': 'Enter your registered email'}))

class ApplicationForm(forms.ModelForm):
    COUNTRY_CODES = [
        ('+91', 'India (+91)'),
        ('+1', 'USA (+1)'),
        ('+44', 'UK (+44)'),
        ('+61', 'Australia (+61)'),
        ('+86', 'China (+86)'),
        ('+81', 'Japan (+81)'),
        ('+49', 'Germany (+49)'),
        ('+33', 'France (+33)'),
        ('+39', 'Italy (+39)'),
        ('+7', 'Russia (+7)'),
        ('+55', 'Brazil (+55)'),
        ('+27', 'South Africa (+27)'),
        ('+971', 'UAE (+971)'),
        ('+65', 'Singapore (+65)'),
        ('+60', 'Malaysia (+60)'),
        ('+82', 'South Korea (+82)'),
        ('+66', 'Thailand (+66)'),
        ('+63', 'Philippines (+63)'),
        ('+62', 'Indonesia (+62)'),
        ('+84', 'Vietnam (+84)'),
        ('+20', 'Egypt (+20)'),
        ('+234', 'Nigeria (+234)'),
        ('+254', 'Kenya (+254)'),
        ('+91', 'Sri Lanka (+94)'),
        ('+977', 'Nepal (+977)'),
        ('+880', 'Bangladesh (+880)'),
        ('+92', 'Pakistan (+92)'),
        ('+98', 'Iran (+98)'),
        ('+964', 'Iraq (+964)'),
        ('+962', 'Jordan (+962)'),
        ('+966', 'Saudi Arabia (+966)'),
        ('+90', 'Turkey (+90)'),
        ('+30', 'Greece (+30)'),
        ('+31', 'Netherlands (+31)'),
        ('+32', 'Belgium (+32)'),
        ('+34', 'Spain (+34)'),
        ('+35', 'Portugal (+35)'),
        ('+36', 'Hungary (+36)'),
        ('+40', 'Romania (+40)'),
        ('+41', 'Switzerland (+41)'),
        ('+43', 'Austria (+43)'),
        ('+45', 'Denmark (+45)'),
        ('+46', 'Sweden (+46)'),
        ('+47', 'Norway (+47)'),
        ('+48', 'Poland (+48)'),
        ('+52', 'Mexico (+52)'),
        ('+53', 'Cuba (+53)'),
        ('+54', 'Argentina (+54)'),
        ('+56', 'Chile (+56)'),
        ('+57', 'Colombia (+57)'),
        ('+58', 'Venezuela (+58)'),
        ('+64', 'New Zealand (+64)'),
        ('+91', 'Bhutan (+975)'),
        ('+91', 'Maldives (+960)'),
    ]

    country_code = forms.ChoiceField(choices=COUNTRY_CODES, initial='+91', label='Country Code')
    school = forms.CharField(
        label='Select School Applying for *',
        widget=forms.Select(),
        required=True
    )
    state = forms.CharField(
        label='Select State *',
        widget=forms.Select(),
        required=True
    )
    city = forms.CharField(
        label='Select City *',
        widget=forms.Select(),
        required=True
    )
    course = forms.CharField(
        label='Select Course *',
        widget=forms.Select(),
        required=False
    )
    specialization = forms.CharField(
        label='Select Specialization *',
        widget=forms.Select(),
        required=False
    )

    class Meta:
        model = Application
        fields = ['name', 'email', 'country_code', 'mobile', 'state', 'city', 'course', 'specialization', 'captcha', 'authorization']
        exclude = ['school']
        labels = {
            'name': 'Enter Name *',
            'email': 'Enter Candidate\'s Email Address *',
            'country_code': 'Country Code',
            'mobile': 'Enter Candidate\'s Mobile Number *',
            'state': 'Select State *',
            'city': 'Select City *',
            'school': 'Select School Applying for *',
            'course': 'Select Course *',
            'specialization': 'Select Specialization *',
            'captcha': 'Enter Captcha',
            'authorization': 'I authorize Joy University and its representatives to contact me via Email, SMS, WhatsApp, or Call for updates and notifications, even if I am on DND/NDNC *',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name *'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Candidate\'s Email Address *'}),
            'country_code': forms.Select(attrs={'class': 'country-code-select'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Enter Candidate\'s Mobile Number *'}),
            'state': forms.Select(attrs={'placeholder': 'Select State *'}),
            'city': forms.Select(attrs={'placeholder': 'Select City *'}),
            'school': forms.Select(attrs={'placeholder': 'Select School Applying for *'}),
            'course': forms.Select(attrs={'placeholder': 'Select Course *'}),
            'specialization': forms.Select(attrs={'placeholder': 'Select Specialization *'}),
            'captcha': forms.TextInput(attrs={'placeholder': 'Enter Captcha'}),
            'authorization': forms.CheckboxInput(attrs={'required': False}),
        }

class OTPLoginForm(forms.Form):
    contact = forms.CharField(label='Mobile Number or Email', widget=forms.TextInput(attrs={'class': 'contact-input', 'placeholder': 'Enter registered mobile number or email'}))

class OTPVerifyForm(forms.Form):
    otp_code = forms.CharField(label='OTP Code', max_length=6, widget=forms.TextInput(attrs={'class': 'otp-input', 'placeholder': 'Enter 6-digit OTP'}))


class DeclarationForm(forms.Form):
    applicant_name = forms.CharField(max_length=100, label="Applicant's Name *", widget=forms.TextInput(attrs={'readonly': True}))
    parent_name = forms.CharField(max_length=120, label="Parent's Name *", widget=forms.TextInput(attrs={'readonly': True}))
    declaration_date = forms.DateField(label="Date *", widget=forms.DateInput(attrs={'type': 'date', 'readonly': True}))

class EnrollmentDetailsForm(forms.ModelForm):
    NATIONALITY_CHOICES = [
        ('Indian', 'Indian'),
        ('Foreigner', 'Foreigner'),
    ]
    PROGRAM_LEVEL_CHOICES = [
        ('UG', 'UG'),
        ('PG', 'PG'),
    ]
    RELIGION_CHOICES = [
        ('Hindu', 'Hindu'),
        ('Muslim', 'Muslim'),
        ('Christian', 'Christian'),
    ]
    CATEGORY_CHOICES = [
        ('General/OC', 'General/OC'),
        ('BC', 'BC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
        ('Others', 'Others'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    COUNTRY_CHOICES = [
        ('', 'Select Country'),
        ('Afghanistan', 'Afghanistan'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cabo Verde', 'Cabo Verde'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Costa Rica', 'Costa Rica'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('East Timor', 'East Timor'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Eswatini', 'Eswatini'),
        ('Ethiopia', 'Ethiopia'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Greece', 'Greece'),
        ('Grenada', 'Grenada'),
        ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea North', 'Korea North'),
        ('Korea South', 'Korea South'),
        ('Kosovo', 'Kosovo'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mexico', 'Mexico'),
        ('Micronesia', 'Micronesia'),
        ('Moldova', 'Moldova'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('North Macedonia', 'North Macedonia'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Romania', 'Romania'),
        ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Sudan', 'South Sudan'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Vatican City', 'Vatican City'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
    ]

    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES, widget=forms.Select())
    program_level = forms.ChoiceField(choices=PROGRAM_LEVEL_CHOICES, widget=forms.Select())
    religion = forms.ChoiceField(choices=RELIGION_CHOICES, widget=forms.Select())
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select())
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select())
    country = forms.CharField(max_length=60, widget=forms.Select(choices=COUNTRY_CHOICES))

    class Meta:
        model = Enrollment
        fields = [
            'nationality', 'program_level', 'course', 'specialization', 'accommodation_status',
            'first_name', 'last_name', 'email', 'mobile', 'dob', 'gender', 'aadhaar', 'religion', 'category',
            'country', 'state', 'district', 'city', 'address_line1', 'address_line2', 'pincode',
            'parent_name', 'parent_mobile', 'parent_email',
            'x_school', 'x_board', 'x_state', 'x_city', 'x_percentage', 'x_after_qualification',
            'hs_school', 'hs_state', 'hs_city', 'hs_board', 'hs_percentage', 'hs_result_status',
            'diploma_university', 'diploma_status', 'diploma_percentage',
            'has_consultant_code', 'consultant_code',
            'passport_number', 'passport_country', 'passport_place', 'passport_issue_date', 'passport_expiry_date',
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'x_percentage': forms.NumberInput(attrs={'step': '0.01'}),
            'hs_percentage': forms.NumberInput(attrs={'step': '0.01'}),
            'diploma_percentage': forms.NumberInput(attrs={'step': '0.01'}),
            'has_consultant_code': forms.CheckboxInput(),
            'aadhaar': forms.TextInput(attrs={'maxlength': '12', 'pattern': r'\d{12}', 'title': 'Aadhaar must be 12 digits'}),
            'passport_issue_date': forms.DateInput(attrs={'type': 'date'}),
            'passport_expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }



