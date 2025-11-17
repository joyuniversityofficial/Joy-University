from django.contrib import admin
from .models import School, Update, Approval, Event, Faculty, SchoolDetail, StudentClub, ExecutiveCouncil, GoverningCouncil, AcademicCouncil, Infrastructure, InfrastructureImage, Library, LibraryImage, Hostel, HostelImage, Transportation, TransportationImage, Sports, SportsImage, Facilities, FacilitiesImage, PressMedia, Application

class InfrastructureImageInline(admin.TabularInline):
    model = InfrastructureImage
    extra = 1

class LibraryImageInline(admin.TabularInline):
    model = LibraryImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    search_fields = ['title', 'description']
    list_filter = ('date',)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(SchoolDetail)
class SchoolDetailAdmin(admin.ModelAdmin):
    list_display = ('school',)
    search_fields = ('school__title',)

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)

@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ('alt', 'img_url')
    search_fields = ('alt',)

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

@admin.register(StudentClub)
class StudentClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty_advisor')
    search_fields = ('name', 'faculty_advisor')

@admin.register(ExecutiveCouncil)
class ExecutiveCouncilAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

@admin.register(AcademicCouncil)
class AcademicCouncilAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

@admin.register(GoverningCouncil)
class GoverningCouncilAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    inlines = [InfrastructureImageInline]

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    inlines = [LibraryImageInline]

class HostelImageInline(admin.TabularInline):
    model = HostelImage
    extra = 1

class TransportationImageInline(admin.TabularInline):
    model = TransportationImage
    extra = 1

class SportsImageInline(admin.TabularInline):
    model = SportsImage
    extra = 1

class FacilitiesImageInline(admin.TabularInline):
    model = FacilitiesImage
    extra = 1

@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    inlines = [HostelImageInline]

@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    inlines = [TransportationImageInline]

@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    inlines = [SportsImageInline]

@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    inlines = [FacilitiesImageInline]

@admin.register(PressMedia)
class PressMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'school', 'application_number', 'status', 'created_at')
    list_filter = ('status',)
    readonly_fields = ('application_number',)

from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("application_number", "first_name", "last_name", "program_level", "course", "specialization", "submitted_at")
    search_fields = ("application_number", "first_name", "last_name", "email", "mobile")
    list_filter = ("program_level", "accommodation_status", "hs_result_status", "category")


