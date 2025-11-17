from bs4 import BeautifulSoup
import os

def scrape_courses_and_specializations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Assuming the courses are in a specific section, e.g., under 'programmes-offered'
    programmes_section = soup.find('section', id='programmes-offered')
    if not programmes_section:
        return {}, {}

    courses = {}
    specializations = {}

    # Extract all h2 and their following ul
    h2_elements = programmes_section.find_all('h2')
    for h2 in h2_elements:
        ul = h2.find_next('ul')
        if ul:
            course_list = [li.get_text(strip=True) for li in ul.find_all('li') if 'Apply Now' not in li.get_text()]
            if course_list:
                courses[h2.get_text(strip=True)] = course_list
                for course in course_list:
                    specializations[course] = []  # Assuming no specializations for now

    return courses, specializations

def scrape_all_schools(directory):
    all_courses = {}
    all_specializations = {}
    for file in os.listdir(directory):
        if file.startswith('school_') and file.endswith('.html'):
            file_path = os.path.join(directory, file)
            school_name = file.replace('school_', '').replace('.html', '').replace('_', ' ').title()
            courses, specializations = scrape_courses_and_specializations(file_path)
            if courses:
                all_courses[school_name] = courses
                all_specializations.update(specializations)
    return all_courses, all_specializations

if __name__ == "__main__":
    directory = "templates"
    all_courses, all_specializations = scrape_all_schools(directory)
    print("All Courses:", all_courses)
    print("All Specializations:", all_specializations)
