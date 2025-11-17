from django.core.management.base import BaseCommand
from university.models import Faculty

class Command(BaseCommand):
    help = 'Populate Faculty model with initial data'

    def handle(self, *args, **options):
        faculty_data = [
            {
                "name": "Prof. Dr. Bini Marin V",
                "qualifications": "Ph.D. - Business Administration, Mother Teresa Women's University, Kodaikanal",
                "designation": "Associate Dean - Academics, Associate Dean - School of Entrepreneurship & Management",
                "description": """An accomplished academician with 23 years of experience in field of Business Management. Her key academic roles includes Associate Professor and Faculty Head for the Department of Business Management in Scott Christian College (Autonomous), Nagercoil. Dr. Marin holds MBA from MS University, Tirunelveli , an MPhil from Alagappa University, Karaikudi and Doctorate in Business Administration from Mother Teresa Women's University. Kodaikanal. She has also cleared UGC-NET in Business Administration, underscoring her academic credibility. Her teaching portfolio spans subjects such as Human Resource Management, Organisational Behaviour, Business Analytics and HR Analytics.

Dr. Marin's research interests lie in Contemporary HR Practices including e-HRM, Hybrid Work Culture, Green HRM, Employee Branding and Data Driven Business Intelligence. She has guided Six PhD Scholars to successful completion in the area of Business Administration and continues to mentor in Doctoral level. She has a strong research profile, with several publications indexed in Scopus and other reputed journals.

Dr. Marin is known for combining academic rigour with practical insights and she continues to contribute meaningfully to the academic community through teaching. research and mentorship."""
            },
            {
                "name": "Prof. Dr. Chithra D Gracia",
                "qualifications": "Ph.D - NIT, Tiruchirapalli",
                "designation": "Professor & Dean - School of Computational Intelligence",
                "description": """Prof. Dr. Chithra D Gracia is working as an Assistant Professor in the Department of Computing & Information Systems under the School of Computational Intelligence, Joy University, Kanyakumari, Tamil Nadu, India. She has her Bachelor's Degree (B.E) in Computer Science and Engineering from Manonmanian Sundaranar University, Tirunelveli, Master's Degree (M.E) in Computer Science and Engineering from Anna University, Chennai and Ph.D. in Computer Science and Engineering from National Institute of Technology, Tiruchirapalli.

She has worked as faculty in Engineering Colleges and University in Tamil Nadu and has handled classes in National Institute of Technology, Tiruchirapalli. Prior to joining Joy University, she has 12 and 6 years of experience in teaching and research respectively. She is the only recipient of HTRA fellowship (2011 to 2016) in the department of Computer Science and Engineering for pursuing Ph.D at National Institute of Technology Tiruchirapalli from Ministry of Human Resource and Development (MHRD), Government of India.

She has presented her research papers in leading international and national conferences in leading institutions in India.  She has published more than 20 research papers in SCI and SCOPUS indexed International Journals, Conferences and Book chapters of repute in the field of Data Science. She has delivered many invited lectures on Machine Learning, Recommender Systems. She has been a professional facilitator of students and her teaching experience includes experiments on Learner centric teaching and flipped classroom. During her tenure, she was a nominated member in various committees assisting the administration in matters of importance. She is a reviewer of the reputed International journal, IEEE Systems. Her research areas include Machine Learning, Web services, Cloud computing, Fog computing and Edge Computing. She is a Life Member of Indian Society for Technical Education (MISTE)."""
            },
            {
                "name": "Prof. Dr. V. Balasubramaniam",
                "qualifications": "Ph.D. - JNTU, Hyderabad",
                "designation": "Professor & Dean - School of Pharmacy",
                "description": """Prof. Dr. V. Balasubramaniam has obtained his M. Pharm at The Tamil Nadu Dr. MGR Medical University (JSS College of Pharmacy) with the specialization of Pharmaceutical Biotechnology.

Prof. V. Balasubramaniam has 25 years of versatile experience in the various fields of Pharmacy with 20 years of teaching experience. He has been recommended as faculty by the Staff Selection Committee of Osmania University, Hyderabad. He is approved as Research Supervisor, Examiner & Evaluator for M.Pharm by the Osmania University, Hyderabad, Palamuru University, Mahabubnagar and Jawaharlal Nehru Technological University, Hyderabad and Kakatiya University, Warangal.

His area of research is Novel Vaccine Delivery Systems. He has published 20 research articles in peer reviewed reputed international journals and presented 40 research papers in National & International Conferences and has guided 25 research projects. He is a life member of APTI (The Association of Pharmaceutical Teachers of India) since 2008. He served as Editorial Advisory Board Member, International Journal of Pharmaceutical & Industrial Research and Associate Editor for International Journal of Innovative Pharmaceutical Sciences and Research."""
            },
            {
                "name": "Prof. Dr. Johnsy Rani",
                "qualifications": "Ph.D - The TN Dr.M.G.R Medical University, Chennai",
                "designation": "Professor & Associate Dean - School of Nursing",
                "description": """Prof. Dr. Johnsy Rani is currently serving as a Professor in the School of Nursing at Joy University, Tirunelveli, Tamil Nadu. She has her Doctoral degree in Community Health Nursing from Apollo College of Nursing, Chennai under The Tamilnadu Dr. MGR Medical University, Chennai in the year 2019. She is presently a Postdoctoral Researcher at Srinivas University, Mangalore, Karnataka. She is a Research co-guide under Meenakshi Academy of Higher Education and Research, Chennai, Srinivas University, Mangalore, and Shri Jagdishprasad Jhabarmal Tiberwala University, Rajasthan. 

She has a teaching experience of more than 13 years. She has achieved the Best Teacher Award thrice. She is a Life Member of the Christian Medical Association of India (CMAI), the Clinical Nursing Research Society (CNRS), and the Trained Nurses Association of India (TNAI). She has been a trainer in International projects funded by SAWSO, Norway, and NORAD. She has published about 16 research articles in reputed national and international journals and one book chapter under Jaypee Publications. She has done about 13 invited presentations. She is the editor of the International Journal of Community Health Nursing and the International Journal of Nursing Science Practice and Research.   

She has international work experience as Assistant Professor in Male', Maldives where she has been involved in Program, curriculum, module, and content development. She has worked as Nodal Officer for the Mentorship program under Mission Niramaya, Uttar Pradesh, and worked for the Quality ranking of nursing colleges by QCI under Mission Niramaya, Uttar Pradesh."""
            },
            {
                "name": "Prof. Dr. M. S. Sundaram",
                "qualifications": "Ph.D. - VISTAS, Chennai",
                "designation": "Professor & Associate Dean - Physiotherapy, School of Life and Health Sciences",
                "description": """He is graduated with the degree of PhD in Physiotherapy from VISTAS , Chennai in the year of 2017. He served as Senior Professor cum Research supervisor in the same institution.He is holding 28 years of Academic experience with 12 years of research experience in VISTAS , Chennai. Under his able guidance 4 scholars were awarded with PhD degree and four scholars yet to receive.

He also guided more than thirty Post Graduate students in their dessirtation. He has published more than fifty articles in International & National journals."""
            },
            {
                "name": "Prof. Bennet Paul Giftson.D",
                "qualifications": "MA, ML - Department of Legal Studies, University of Madras, Chennai.",
                "designation": "Associate Professor & Associate Dean - School of Law",
                "description": """Bennet Paul Giftson.D currently serving as Associate Professor cum Associate Dean at Joy University, near Kanyakumari in Tirunelveli District. With over 15 years of teaching experience in the field of law, Previously Worked as Assistant Professor at SRM Institute of Science & Technology with a proven track record in curriculum innovation and student mentorship. Expert in syllabus development and class room management, fostering academic growth and engagement. Successfully organized workshops, Seminars and Tamil Moot Court competition and relevant programmes to enhance the practical skills with mother Language and the learning outcomes, while advocating for student success through effective problem - solving and carrer counselling."""
            },
            {
                "name": "Prof. Dr. M. Senthilkumar",
                "qualifications": "Ph.D. - Crystal Growth Centre, Anna University, Chennai",
                "designation": "Associate Professor & Associate Dean - Physics, School of Arts and Natural Sciences",
                "description": """Dr. M. Senthilkumar is an Associate Professor in Physics in the School of Arts and Natural Sciences at Joy University, located near Kanyakumari, Tirunelveli District, Tamil Nadu, India. He holds a Bachelor of Science degree in Physics from Sri Vasavi College, Erode (affiliated with Bharathiar University, Tamil Nadu) and a Master of Science degree in Physics from PSG College of Arts and Science, Coimbatore (affiliated with Bharathiar University, Tamil Nadu).

Dr. Senthilkumar earned his Ph.D. from the Crystal Growth Centre, Anna University, Chennai, Tamil Nadu, India.  He has 15 years of teaching experience and 21 years of research experience. His research expertise lies in High-Temperature Crystal Growth (Nonlinear Optics) for frequency conversion and laser applications, and the synthesis and fabrication of nano-bio-nanomaterials and biopolymer scaffolds for tissue engineering, drug delivery, and wound healing applications.

Dr. Senthilkumar's career highlights include junior and senior research fellowships on a major Department of Science and Technology (DST) project focused on developing oxide-based nonlinear optical crystals. He also received a direct senior research fellowship award from the Council of Scientific and Industrial Research (CSIR), Government of India. He has authored over 40 research and review articles published in peer-reviewed journals, including those indexed in Science Citation Index (SCI), Science Citation Index Expanded (SCIE), Scopus, Web of Science, and the University Grants Commission (UGC) CARE List. He has supervised four Ph.D. students in Physics to completion and currently supervises five doctoral candidates. He holds one Indian patent in the field of nano-biomaterials for medical applications and has contributed a book chapter. He has supervised ten postgraduate research projects and one Master of Philosophy (M.Phil.) project. He also mentored a visiting researcher from Togo under the DST-CV Raman Fellowship program through the Federation of Indian Chambers of Commerce and Industry (FICCI). He has presented his research at numerous international and national conferences, workshops, and seminars.  He serves as a peer reviewer for several journals indexed in AIP, Scopus, SCIE, and Web of Science."""
            },
            {
                "name": "Prof. Dr. M. Haris",
                "qualifications": "Ph.D.-Crystal Growth Centre, Anna University, Chennai",
                "designation": "Associate Professor - Physics, School of Arts and Natural Sciences",
                "description": """Professor Dr.M.Haris is currently an Associate Professor at the School of Arts and Natural Sciences at Joy University, located in Kanyakumari, Tamil Nadu, India. He holds a Bachelor's degree in Physics from Manonmaniam Sundaranar University through S.T.Hindu College in Nagercoil, Tamil Nadu, and a Master's degree in Physics and Master of Philosophy degree in Physics from Annamalai University in Chidambaram, Tamil Nadu.

He holds a Ph.D. degree through Crystal Growth Centre, Anna University in Chennai, Tamil Nadu, India. He has more than 15 years of teaching experience and 26 years of Research experience at various academic institutions, including Scientist 'D' in Centre for Nanoscience and Nanotechnology, Sathyabama Institute of Science and Technology, Chennai, India and Associate Professor of Physics at Karunya Institute of Technology and Sciences, Coimbatore, India. His areas of focus in research include Semiconductor Crystal Growth, Nanomaterials and Thin Films for Gas sensing applications.

Prof. Dr.M.Haris has achieved significant milestones in his career, including Project Fellow in an UGC project, Japanese Government Scholarship (Monbukagakusho) supported by Ministry of Human Resource Development, New Delhi, India and Japanese Government, Japan for carrying out Research work in Research Insitute of Electronics, Shizuoka University, Hamamatsu, Japan. He served as a Post-Doctoral Fellow in Laboratory for Materials Processing, POSTECH, South Korea and Centre for Condensed Matter Sciences, National Taiwan University, Taipen, Taiwan. He has authored over 60 research articles in reputable journals, including SCI, SCIE, Scopus, and UGC Care List journals. In his supervision 7 students have completed their Ph.D in Physics. He has supervised more than 15 research projects for PG students as part of their curriculum and has guided several Foreign students from Mongolia, Nigeria, Togo, Morocco and Germany through Department of Science and Technology (DST-RTF-DCS), CICS, DST-CV Raman Fellowship programs."""
            },
            {
                "name": "Prof. Dr. Ayappasamy. K",
                "qualifications": "Ph.D (Wireless Communication). - Pondicherry Central University",
                "designation": "Associate Professor - School of Computational Intelligence",
                "description": """Dr. Ayappasamy K. is an Associate Professor in Computing and Information Systems at the School of Computational Intelligence, Joy University, Kanyakumari, Tamil Nadu, India. He earned his B.Tech. and M.Tech. Degrees in Electronics and Communication Engineering (ECE) from Pondicherry Engineering College (PEC) affiliated with Pondicherry central university, and completed his Ph.D. in  the field of 5G wireless communication at Pondicherry Central University, Puducherry, India.

Before his current position, Dr. Ayappasamy worked as a Research Engineer, where he conducted research on heart-based phonocardiogram (PCG) signals using machine learning and deep learning models at the School of Electronic Systems and Automation, Digital University Kerala (IIITM Kerala) in Thiruvananthapuram, Kerala, India. He also served as an Assistant Professor in the Department of ECE at Christ College of Technology in Puducherry, India. In 2021, he was honored with the Dr. A. P. J. Abdul Kalam Teacher Award by the education minister of Puducherry.

Dr. Ayappasamy is a professional member of IEEE and he is the SDLP (sustainable development platform) speaker of the IEEE Kerala section. He has published his research in various journals, book chapters, and lecture notes including IEEE, IET, Springer, CRC Press, and other Scopus-indexed forums. His research interests encompass signal processing in 5G wireless communication, 2D multi-carrier modulations, bio-signal processing with machine learning and deep learning models, and the Internet of Things (IoT)."""
            },
            {
                "name": "Prof. Dr. Sanjith S",
                "qualifications": "Ph.D. - Noorul Islam University",
                "designation": "Associate Professor - School of Computational Intelligence",
                "description": """Dr. Sanjith is a seasoned academician and researcher with over 16 years of experience in teaching, research, and technology management. Currently serving as Associate Professor under the School of Computational Intelligence, Joy University, he has previously held key roles at Karunya Institute of Technology and Sciences and St. Alphonsa College of Arts and Science. He holds a Ph.D. in Computer Science and Engineering and has published 37+ research papers in SCI, Scopus, and Web of Science indexed journals. His research interests span Cybersecurity, Digital Forensics, Artificial Intelligence, Networking, and Image Processing. He has contributed to 4 book chapters and holds 2 published patents in areas such as quantum cryptography and AI-driven anomaly detection.
 

Recognized for academic excellence, Dr. Sanjith is a recipient of the Outstanding Ph.D. Award and has earned listings in the World Book of Records, India Book of Records, and Asia Book of Records. He serves as a reviewer for leading journals, including Artificial Intelligence Review and IET Image Processing, and holds memberships in the Indian Society for Remote Sensing and Indian Academic Researchers Association.

Beyond research, he plays an active role in curriculum development, mentoring NPTEL learners, coordinating curriculum design, and contributing to innovation and entrepreneurship initiatives. He also served as Assistant Project Director for the NIUSAT satellite mission.Outside academia, Dr. Sanjith is a passionate environmentalist and antiquities enthusiast, committed to preserving nature through planting trees and collecting cultural artifacts."""
            },
            {
                "name": "Prof. Dr. Kala S Nathan",
                "qualifications": "Ph.D. - Vels University , Chennai",
                "designation": "Associate Professor - School Of Computational Intelligence",
                "description": """Dr. Kala S. Nathan holds a Ph.D. in Computer Science from Vels Institute of Science & Technology and an M.Phil. in Computer Science from Alagappa University. Her academic journey reflects a deep commitment to learning, teaching, and mentoring, forming the foundation of her distinguished career in higher education.
With over 17 years of experience in the field of Computer Science, Dr. Kala is a highly accomplished academician and visionary educator. Renowned for her dynamic leadership and unwavering dedication to academic excellence, she has played a pivotal role in shaping the research and academic environment within her institution. Her career is characterized by a strong emphasis on curriculum innovation, strategic academic planning, and student-centered learning methodologies.
 

Dr. Kala served as the Head of the Department of Computer Science & Applications for more than a decade, during which she led transformational initiatives that resulted in increased student enrollment, enhanced academic performance, and significant departmental growth. Her leadership style is collaborative and inspiring, consistently promoting interdisciplinary engagement and continuous quality improvement in academic standards.
She is especially passionate about supporting the academic growth of slow learners, designing tailored learning strategies, and fostering inclusive and empathetic classroom environments that enable every student to thrive.
A prolific contributor to the academic community, Dr. Kala has authored six academic books, reviewed two scholarly publications, and presented numerous research papers in reputed journals and international conferences. Her research interests include Artificial Intelligence, Image Processing, and IoT Security-fields in which she remains actively engaged through ongoing scholarly work.
In the area of innovation, she has multiple patents, including two Indian Design Patents-one focused on an AI and Image Processing-based Plant Immunity Tracking Device, and another on a Sign Language to Speech Converter Device. Additionally, she has a Utility Patent for a deep learning-based approach to IoT security aimed at detecting and preventing cyber threats.
Dr. Kala S. Nathan is widely respected not only for her technical expertise but also for her integrity, motivational leadership, and student-centric approach to education. She continues to make meaningful contributions to academia through her dedication to research, innovation, and the holistic development of future-ready graduates."""
            },
            {
                "name": "Prof. Dr. A. Alphonse John Kenneth",
                "qualifications": "Ph.D. - Manonmaniam Sundaranar University",
                "designation": "Associate Professor - School of Computational Intelligence",
                "description": """I completed my Ph.D Computer Science in MS University, Tirunelveli. I worked as vice-principal in Unicohs University, Lusaka, Zambia."""
            },
            {
                "name": "Prof. Dr. Ramswaroop Saini",
                "qualifications": "Ph.D - IIT, Madras",
                "designation": "Assistant Professor & Assistant Dean - School of Life and Health Sciences",
                "description": """Prof. Dr. Ramswaroop Saini is currently working as an Assistant Professor in the School of Life and Health Sciences, Joy University, Kanyakumari, Tamilnadu, India. He received his Bachelor's and Master's Degree from the University of Rajasthan in the field of Biotechnology. He completed his Doctoral degree from the Indian Institute of Technology Madras (IITM) in the field of Plant Genetics and Developmental Biology. He qualified GATE, CSIR-UGC-NET and CSIR-UGC-NET-JRF and availed the fellowship during doctoral research. He visited the United State of America (USA) to attend "the 28th International Conference on Arabidopsis Research (ICAR) 2017" held on 19 to 23rd June 2017 in St. Louis Missouri, USA.

Prior to joining Joy University, he has total 10 + years of experience in research and Academics (Kalinga University Raipur, Chhattisgarh). He has been involved in establishing the set up of Green House, Vermicompost unit and Mushroom cultivation facilities on the premises of Kalinga University Raipur. He has experience in conducting Hands-on training programs, Workshops and summer internships in the field of molecular biology, Microbial and Biochemical Techniques.
He has published 7 research papers and 1 book chapter (Elsevier) in reputed International and National journals with a good impact factor. During Doctoral research he examined the role of various Biotic and Abiotic factors such as parental age, temperature and nitric oxide on Meiotic Recombination (MR) rates in model plant Arabidopsis thaliana.  His research interests include Plant Genetics, Developmental Biology, Plant Molecular Biology, Stress Biology, Meiotic Recombination, Plant Growth hormones and Nitric oxide Signaling.
Faculty Testimonial of Prof. Dr. Ramswaroop Saini. Ph.D - IIT, Madras"""
            },
            {
                "name": "Prof. Dr. Pooja Krishna J",
                "qualifications": "Ph.D - Kerala Agricultural University, Thrissur",
                "designation": "Assistant Professor & Assistant Dean - School of Agricultural Sciences",
                "description": """Dr. Pooja Krishna J obtained her Ph.D. in Agriculture from Kerala Agricultural University, Thrissur, specializing in Agricultural Extension Education. She has successfully qualified for the UGC NET in Adult Education/Andragogy and the ASRB ICAR-NET in Agricultural Extension.

Dr. Pooja has conducted numerous expert sessions and On-the-Job Training (OJT) classes for vocational higher secondary education students. Her scholarly contributions include authoring numerous research papers, book chapters, abstracts, and articles in various international journals. She has also served as a reviewer for esteemed journals and books, such as the Asian Journal of Agricultural Extension, Economics and Sociology, International Journal of Plant and Soil Science, Journal of Experimental Agriculture International, and BP International.

Her areas of interest and specialization include climate change and resilience, peri-urban and urban agriculture, and subaltern and gender studies. Dr. Pooja has actively participated in and organized various international and national seminars. She has been recognized for her outstanding research, receiving the Best Research Paper Presentation award at the International Seminar on Sustainable Urban Agricultural Systems and Community Resilient Cities 2024, and the Third Best Research Paper award at the Biozion International Biotechnology Conclave 2023."""
            },
            {
                "name": "Prof. Dr. K. S. Ramya",
                "qualifications": "MBBS., F.Diab",
                "designation": "Assistant Professor - School of Life and Health Sciences",
                "description": """Prof. Dr. Ramya KS is currently serving as an Assistant Professor in the  Department of Allied Health Science under the School of Life and Health Sciences at Joy University, Kanyakumari, Tamil Nadu. She completed her Bachelor of Medicine & Bachelor of Surgery from Rajah Muthiah Medical College, Chidambaram and fellowship in clinical diabetology from Ramachandran Diabetic Hospital, Chennai.

She has worked as a General Physician, Consultant Diabetologist in Chennai and in Nagercoil. Some of the services provided by the doctor - Emergency Care, Counselling, Diabetic Management. Her other interests are travelling and cooking."""
            },
            {
                "name": "Prof. Dr. C. Rajesh Kumar",
                "qualifications": "B.S Psychology, MBBS - AMASOM, Philippines",
                "designation": "Assistant Professor- School of Life and Health Sciences",
                "description": """Prof. Dr. Rajesh Kumar. C is currently serving as an Assistant Professor in Department of Allied health Sciences under the school of Life and Health Sciences at Joy University, Kanyakumari, Tamilnadu. He completed his Bachelor of science in Psychology from AMA university- Philippines, and Doctor of Medicine from AMA School of Medicine - Philippines. 

He Has worked as a General Physician in Valliyoor - Tirunelveli. He did his 2-year medical internship in Government  medical college and hospital - Ooty, Nilgiris. Services provided by the doctor - First Aid management and emergency Health care. His other interests Bike traveling and exploring."""
            },
            {
                "name": "Prof. Dr. F. Dinusha Masil",
                "qualifications": "Ph.D - Business Administration - Manonmaniam Sundaranar University, Tirunelveli",
                "designation": "Assistant Professor - School of Law",
                "description": """Prof. Dr. F. Dinusha Masil currently holds the esteemed position of Assistant Professor in the School of Law at Joy University, Kanyakumari, Tamil Nadu, India. She embarked on her educational journey progressing to achieve an extensive academic portfolio that includes qualifications such as B.A. BL. from the Government Law College, Tirunelveli, an MBA from Alagappa University, Karaikudi, M.A in Criminology and Police Science, M.Sc. in Psychology, and two LLM degrees from esteemed universities. The pinnacle of her academic achievements is her Ph.D. in Business Administration-Commerce (Interdisciplinary) which she was awarded by Manonmaniam Sundaranar University, Tirunelveli in 2022.

Before joining Joy University, she practiced as an Advocate in the District Court of Kanniyakumari District, enriching her professional experience in the field of law from March 2010 to May 2015. She furthered her academic career by serving as an Assistant Professor in Thulasi College of Law for Women, Vallanadu, Thoothukudi District before her current tenure.

Throughout her academic career, she has shown keen interest in pertinent societal issues. This is reflected in her research projects which revolve around the protection of women from domestic violence, corporate laws concerning the Board of Directors' role in company management, and the imperative topic of stress management for women in the informal sector. She has also made significant academic contributions by publishing six research articles in various esteemed journals. Her work has found a place in the UGC CARE list journal and other UGC-approved journals with significant impact factors. She has also authored chapters in books with ISBN, amplifying her research on stress management techniques and the correlation between working conditions and workplace stress."""
            },
            {
                "name": "Prof. Achsha Shiny.A",
                "qualifications": "M.Sc - Pediatric Nursing, MBA - Manonmaniam Sundaranar University, Tirunelveli",
                "designation": "Assistant Professor - School of Nursing",
                "description": """Prof. Achsha Shiny is currently a professor at the School of Nursing, Joy University, Tirunelveli, Tamil Nadu. She received her UG & PG in Nursing from Dr.MGR medical university, Chennai. She specializes in child-health nursing. Her academic project on a quasi-experimental study to evaluate the efficacy of using ice cubes before intramuscular injection for pain reduction using a numerical pain rating scale in children aged 8 to 12 years is still recommended by many university students. She has been a member of TNAI and an active participant in SNA activities.

She received the best academic achievement award and best student award during her course of study in nursing. With her passion for managing students and management studies. She earned her MBA in Human Resources from Manonmaniam Sundaranar University, Tirunelveli. She has hosted/presented papers and publications at many international conferences. She is pursuing her Ph.D in management studies at Madurai Kamaraj University.

She is currently conducting her doctoral research on job stress, coping strategies, and their effects on teachers' job performance. Recently, she published a dissertation on "Dynamic Management Practices in the Digitalized Era" which is used by many MBA students and other researchers. She has more than 11 years of teaching and training experience in the field of nursing. Dedicated, resourceful, and goal-driven, professional educator with a vision and commitment to the academic growth and development of every student."""
            },
            {
                "name": "Prof. Dr. Mukesh Kumar",
                "qualifications": "Ph.D. - IIT Guwahati, M.Tech - NIT Bhopal",
                "designation": "Assistant Professor - Mechanical Engineering, School of Engineering & Technology",
                "description": """Dr. Mukesh Kumar is currently working as an Assistant Professor in the Department of Mechanical Engineering under the School of Computational Intelligence at Joy University, Kanyakumari, Tamil Nadu, India. He completed his Master's degree in Mechanical Engineering from NIT Bhopal, Madhya Pradesh and Ph.D. in Design and Manufacturing from the Department of Mechanical Engineering in Indian Institute of Technology Guwahati, Assam.

He published his research work in reputed journals and conferences, including six SCI-indexed journals, six international conferences, and one book chapter. His research interests include Wearable device, Energy harvesting, Sensors, Nanocomposite, and Electrospinning. He achieved a good score in GATE four times and received a fellowship during his master's and doctoral research.

He started his teaching career as an Assistant Professor at the E-max Group of Institutions, Ambala, and worked there for almost three years after completing his M.Tech. After earning Ph.D., he worked on two different SERB projects at the Indian Institute of Technology Guwahati, Assam, for one year. He actively participated in numerous workshops and conferences, coordinated various academic events and activities, and served as a reviewer for SCI-indexed journals. In addition to his academic pursuits, he enjoys extracurricular activities such as playing cricket, badminton, running, and yoga."""
            },
            {
                "name": "Prof. Dr. K. Anilet Anandhy",
                "qualifications": "Ph.D - Child Health Nursing",
                "designation": "Assistant Professor - School of Nursing",
                "description": """Dr.K. Anilet Anandhy has a total of 13 years of experience in teaching. Published more than 9 research articles and presented 2 papers. Membership in CMAI,ADE,TNAI,NTAI.

Held various positions in the field of nursing"""
            },
            {
                "name": "Prof. Dr. Kavitha Williams W",
                "qualifications": "Ph. D - VIT, Vellore",
                "designation": "Assistant Professor - School of Arts & Natural Sciences",
                "description": """Dr. Kavitha Williams W is an accomplished Assistant Professor in the School of Arts and Natural Sciences at Joy University, Kanyakumari, Tamil Nadu, India. Dr. Kavitha Williams holds a Bachelor of Science in Mathematics and a Master of Science in Mathematics from Thiruvalluvar University, Katpadi, Vellore. She also completed her Ph. D. from VIT Vellore in 2024, with her thesis titled "A study on the existence and controllability results for fractional evolution equations and inclusions.

Dr. Kavitha Williams research focuses on fractional calculus, particularly on existence and controllability results, second-order fractional systems, fractional differential equations and inclusions, Atangana-Baleanu fractional systems, and stochastic differential equations of fractional evolution equations and inclusions. She has published nine research papers in SCI/SCIE-indexed journals."""
            },
            {
                "name": "Prof. Dr. P. Deepavathi",
                "qualifications": "Ph.D - National Institute of Technology, Tiruchirappalli",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Mrs. P. Deepavathi has completed her Ph.D in the Department of Computer Science and Engineering, National Institute of Technology, Tiruchirappalli, Tamil Nadu. She obtained her B. Tech degree from Arulmigu Kalasalingam College of Engineering and M. Tech degree from Kalasalingam University in the Department of Information Technology, Krishnan Koil, Tamilnadu, India.

Her areas of interest include Computer Networks, network Security, Operating Systems, Mobile Communication, and Internet of Things."""
            },
            {
                "name": "Prof. Dr. Mohammed Shuaib PA",
                "qualifications": "Ph.D - University of Calicut",
                "designation": "Assistant professor - School of Arts and Natural Sciences",
                "description": """Dr. Mohammed Shuaib currently working as an Assistant Professor in the School of Arts and Natural Sciences at Joy University, Kanyakumari, Tamil Nadu. He completed his Bachelor in English Literature from Kannur University, Kerala, and earned his MA and M.Phil. in Comparative Literature from University of Calicut, Kerala, and qualified for the UGC National Eligibility Test for Lectureship along with Junior Research Fellowship. He has his PhD in Comparative Literature from University of Calicut. Currently he is pursuing his second Master's degree from Aligarh Muslim University.

Dr. Shuaib has presented his research papers at national and international conferences hosted by leading universities in India. He has published two research papers in international journals and has participated in numerous seminars, workshops and colloquiums. During his PhD tenure he served as a Teaching Assistant at University Department. Previously he worked at Jaipur National University, Jaipur, Rajasthan as an Assistant Professor. He also work as a freelance editor and translator."""
            },
            {
                "name": "Prof. Dr. Anitha T",
                "qualifications": "Ph.D - Gandhigram University, Dindigul",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Prof. Dr. Anitha T is working as an Assistant Professor in the Department of Computing & Information Systems
under the School of Computational Intelligence, Joy University, Kanyakumari, Tamil Nadu, India. She has her Bachelor's Degree (BCA) in Computer Application from Madurai Kamaraj University, Madurai, Master's Degree (MCA) in Computer Application from The Gandhigram University, Dindigul, Master of Philosophy (M.Phil) in Computer Science from Madurai Kamaraj University and Ph.D. in Computer Science from The Gandhigram University, Dindigul.

She has worked as a faculty member at Arts College in Tamil Nadu. Prior to joining Joy University, she has 2 and 4 years of experience in teaching and research, respectively.

She has presented her research papers in leading international and national conferences in leading institutions in India. She has published more than 20 research papers in ESCI and SCOPUS indexed International Journals, Conferences and Book chapters of repute in the field of Medical Image Processing. During her tenure, she was a nominated member in various committees assisting the administration in matters of importance. She is a reviewer of the reputed SCI, International journals. Her research areas include Brain Tumor Analysis, Medical Image Processing, Deep Learning, Machine Learning, Image Retrieval, Data Preprocessing and Parallel Computing."""
            },
            {
                "name": "Prof. Dr. R. Pungavi",
                "qualifications": "Ph.D - Annamalai University, Chidambaram",
                "designation": "Assistant professor - School of Agricultural Sciences",
                "description": """Dr. R. Pungavi received Bachelor's Degree from Tamil Nadu Agricultural University and Master's Degree from the Pondicherry University in the field of Agricultural Entomology (Plant Protection). Also completed Doctoral degree from Department of Entomology, Faculty of Agriculture, Annamalai University, Chidambaram with specialization in Chemical Ecology on Extrafloral nectaries mediated interactions with usefulness in Pest Management and Biological control. Qualified ASRB-ICAR-NET-2021. Worked as Field Assistant under the project funded by Sulphur Mills Limited and received fellowship during my doctoral research.

Coming to teaching experience, worked as Teaching Assistant by Assisting Entomology practical classes for the Under Graduate students at Annamalai University during my Doctoral Programme. Acted as Guest Teaching Faculty for agriculture staff at Amalorpavam Senior Secondary School, Pondicherry during the period between 2022-2024.

Published 09 research articles in peer reviewed reputed national and international journals with NAAS along with Scopus/WOS/SCI indexed, also published a book as well as 14 book chapters with ISBN number. Participated and presented more than ten research papers in National and International conference. And published more than 10 interesting contents about agriculture through popular articles in several Agricultural e-magazine.

Research interests include insect rearing, pest management using biological controls, arthropod- plant interactions and field evaluation studies using biorationals and insecticide molecules."""
            },
            {
                "name": "Prof. Dr. Mohammed Shafeer K P",
                "qualifications": "Ph.D - Thiruvalluvar University, Vellore",
                "designation": "Assistant Professor - School of Arts and Natural Sciences",
                "description": """Dr. MOHAMMED SHAFEER K P, currently working as Assistant Professor in the School of Arts and Natural Sciences at Joy University, Kanyakumari,Tamilnadu has 9 years of experience in teaching. He completed his Masters and M Phil in English Literature from Annamalai University, Tamilnadu and has his PhD from Thiruvalluvar University, Vellore. He qualified UGC-National Eligibility Test for Lectureship in June 2012.

He has presented papers in 145 international, and 25 national seminars/conferences; published 36 articles in ISSN journals and 31 chapters in ISBN books and has participated in 155 international, 189 national and 56 state level seminars/conferences; Attended 217 national/ international workshops; 60 national/ international FDPs and 33 lectures/training programmes/ symposia.

He has finished 7 NPTEL courses including a gold medal in the 12 Week Course Short Fiction in Indian Literature conducted by IIT Madras in November 2023. His area of interest include Regional Studies, Postcolonialism and Cultural Studies"""
            },
            {
                "name": "Prof. Dr. Ramu Samineni",
                "qualifications": "Ph.D - Vignan University, Guntur, Andhra Pradesh",
                "designation": "Assistant Professor - School of Pharmacy",
                "description": """Professor Ramu Samineni is currently an assistant professor at the School of Pharmacy at Joy University, located in Kanyakumari, Tamil Nadu, and India. He holds a Bachelor's degree from Annamalai University in Chidambaram, Tamil Nadu, and a Master's degree from SRM University in Chennai, Tamil Nadu. Additionally, he completed a Doctoral degree from Vignan University in Guntur, Andhra Pradesh, India. Prior to joining Joy University, He has more than 12 years of teaching experience at various academic institutions, including Sandip University, Nashik, Vignan University, Guntur, and Mohan Babu University, Tirupati in India.

His areas of focus in research include novel drug delivery systems, cocrystals, floating microspheres, solid lipid nanoparticles, and mouth-disintegrating tablets. He specializes in subjects such as Pharmaceutics, Novel drug delivery systems, Bio pharmaceutics and Pharmacokinetics, Pharmaceutical technology, and Computer-aided drug delivery systems.

Prof. Samineni has achieved significant milestones in his career, including securing one CSIR National Symposium and one workshop project, as well as being granted 3 Indian patents and publishing 9 Indian patents. He has also authored over 45 research and review articles in reputable journals, including SCI, SCIE, Scopus, and UGC Care List journals. Additionally, he holds lifetime professional memberships in various regulatory bodies such as APTI, the Indian Pharmaceutical Association, and the Andhra Pradesh Pharmacy Council. Throughout his professional journey, He has received several awards, including the best researcher award from Insc. Scholars in the academic year 2021-2022, the Best Paper Publication award from Vignan University in the academic year 2022-2023, and the Best Researcher award from TFRF for the academic year 2023-2024. He has supervised more than 20 research projects for both UG and PG students as part of their curriculum and has actively participated in and presented research papers at both national and international conferences.

In addition to his academic and research achievements, Prof. Samineni has extensive experience in handling various pilot-scale equipment for the manufacturing of different dosage forms. He has also organized various conferences, workshops, seminars, add-on courses, and pharmacist day celebrations at the national and international level."""
            },
            {
                "name": "Prof. Dr. Arun Balaji P",
                "qualifications": "Ph.D - VIT University, Chennai",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Dr. Arun Balaji P is an Assistant Professor in the Department of Computing & Information Systems under the School of Computational Intelligence at Joy University, Kanyakumari, Tamil Nadu, India. He holds a Ph.D. in Mechanical / Mechatronics Engineering from VIT University, Chennai. After completing his doctorate, he served as a Postdoctoral Fellow at the Amrita School of Artificial Intelligence, Bangalore, where he worked on multidisciplinary projects involving machine learning and hydraulic systems.

Dr. Arun has a strong academic background, holding an MBA in Human Resource Management from Pondicherry University and a Master's degree in Aircraft Maintenance Engineering from Hindustan University. He has over 7 years of university teaching and research experience at SRM University, VIT University and Hindustan University, along with 3 years of industrial experience. He has contributed to multidisciplinary project funded by the Royal Academy (UK). His expertise spans machine learning, deep learning, 3D modeling and mechanical design, with notable work in fault diagnosis, condition monitoring and automation.

Technically proficient in MATLAB, LabVIEW, SolidWorks and AutoCAD. He specializes in 3D modeling and design for advanced manufacturing. His research is well-recognized, with over 12 publications in SCI journals, including 6 research papers in SCOPUS-indexed journals, covering areas such as deep learning, computer vision, robotics and advanced manufacturing, with a focus on condition monitoring / fault diagnosis.

Throughout his career, Dr. Arun has been actively involved in teaching, mentorship and curriculum development. He has also served in various administrative roles and is a reviewer for Elsevier journals. His current research interests include automation, fault diagnosis, computer vision, condition monitoring and robotic systems."""
            },
            {
                "name": "Prof Dr. P. K. Manoj Kumar",
                "qualifications": "Ph. D - Sri Sathya University of Technology and Medical Sciences",
                "designation": "Assistant Professor -School of Computational Intelligence, ICT Coordinator, IQAC - Member Secretary and Coordinator",
                "description": """Dr. P. K. Manoj Kumar, currently working as Assistant Professor in the School of Computational Sciences at Joy University, Kanyakumari,Tamilnadu has 17 years of experience in teaching. He completed his Masters and M Phil in Computer Science from Vivekanda College, Tamil Nadu and Ph. D from Sri Sathya University of Technology and Medical Sciences. He acted as a senate member of Bharathiar University during 2016-2019. He organized international conferences at Malaysia, Thailand and Indonesia.

He has presented papers in international and national seminars/conferences; published articles in the reputed peer reviewed journals. He has authored for five books and four book chapters. Till now seven patents has published and two patents are granted. He has prepared e-contents for his courses. Received Best HoD award and Best seed Money project award in his career. He has completed many online courses through NPTEL, Coursera and other MOOCs platform. He motivates the students in real time application projects and acted as a mentor for TNSCST student project"""
            },
            {
                "name": "Prof. Dr. Sreya.B",
                "qualifications": "Ph.D - Human Resources from SRM University",
                "designation": "Assistant Professor - School of Entrepreneurship and Management",
                "description": """Dr. Sreya B. is currently serving as an Assistant Professor in the School of Entrepreneurship and Management at Joy University, Kanyakumari, Tamil Nadu. She holds a Ph.D. in Human Resources from SRM University, Andhra Pradesh (2021-2024), where she pursued her research as a full-time scholar. She also holds an M. Com in International Business (University Rank Holder) from PSG College of Arts and Science and an MBA in Human Resources from Bharathiar University. Dr. Sreya has presented her research at eight international conferences, including renowned institutions such as IIM Visakhapatnam, IIT Delhi, IIM Bodh Gaya, and IIT Dhanbad. Her research contributions span across critical areas such as employee engagement, work-life balance, job satisfaction, performance management, and the dynamics of remote working. 

She has published 15 research papers, including five in Q1 Scopus and Web of Science indexed journals such as Frontiers in Sociology and Frontiers in Public Health, as well as in IEEE Xplore®. Her recent work addresses emerging and impactful themes in Human Resource Management, particularly the integration of Artificial Intelligence (AI) for recruitment, predictive HR analytics, and ethical automation practices.

In the area of innovation, Dr. Sreya holds a total of seven patents: five utility patents published in the Patent Official Journal, focusing on the application of AI, augmented reality (AR), and virtual reality (VR) in workplace design and employee monitoring systems, along with one granted international design patent (UK) and one granted Indian design patent, for which she has also received official certificates of grant. With her interdisciplinary research and innovative contributions, Dr. Sreya continues to bridge academic knowledge and technological advancements, offering forward-looking insights into the future of human resource practices in a digitally transforming world."""
            },
            {
                "name": "Prof. Dr. M. N. Mohamed Sadiq",
                "qualifications": "Ph.D. - International Business (Bharathiar University)",
                "designation": "Assistant Professor - School of Entrepreneurship & Management",
                "description": """Dr. Mohamed Sadiq is currently serving as an Assistant Professor in the School of Entrepreneurship & Management at Joy University, Kanyakumari, Tamil Nadu. He holds a Ph.D. in International Business and his doctoral research focused on "Maritime Logistics and Less than Container Load (LCL) Consolidation in Multimodal Supply Chain Management - An Empirical Analysis."

He also earned a Master's degree in International Business and an MBA in Human Resource Management from Bharathiar University, Coimbatore and M.Sc. in Psychology from Tamil Nadu Open University, Chennai. He secured a university rank in both Master's degree in International Business and M.Sc. Psychology. He began his professional journey as an Assistant Professor at Sasurie College of Arts and Science, Tiruppur, where he taught in the Department of Business Administration and Commerce - Professional Accounting. He completed research internships with the Land Ports Authority of India, the Chennai Port Authority and the DP World. These internships provided him with valuable industry insights and practical experience in logistics and supply chain management.

He has been honoured with several accolades, including the "Academic Achiever Award 2020" by Sasurie Arts & Science College, the "Best Research Scholar Award 2023" by the Indian Academic Researchers Association, the "Best Presentation Award" at an International Level Case Study Presentation, the "Best Research Paper Award 2023" issued by Novel Research Academy and presented his research at the National and International conferences. His numerous research publications further underscore his academic rigor and contributions to the field."""
            },
            {
                "name": "Prof. Dr. Salman Ismail Hassan",
                "qualifications": "Ph.D. - International Business (PSG CAS, Bharathiar University)",
                "designation": "Assistant Professor - School of Entrepreneurship & Management",
                "description": """Prof. Dr. Salman Ismail Hassan is a dedicated academician, researcher and social innovator specializing in International Marketing, Logistics and Supply Chain Management. With a strong foundation in international business, he is deeply committed to advancing research, fostering industry-academic collaborations and mentoring students to excel in global business practices. His expertise extends to NAAC accreditation processes (Criteria 3 & 5), ISO documentation and institutional quality enhancement initiatives, contributing significantly to academic governance and institutional development.

Having earned his Ph.D. in International Business from Bharathiar University, his research focuses on International Marketing and Supply Chain Management, reflecting a profound understanding of global trade dynamics. His academic journey includes an M.Com. in International Business from PSG College of Arts & Science and a BBM in Business Management from Chinmaya College of Arts & Science. Recognized for academic excellence, he was awarded the Institutional Research Fellowship during his doctoral studies.

Beyond academia, he brings rich industry experience, having worked as a Supply Chain Analyst at Jayam Impex Pvt. Ltd., Coimbatore, where he specialized in documentation and customer relations. His internship at Cochin Port Trust (Traffic Department) provided invaluable exposure to EXIM cargo operations, enhancing his expertise in maritime logistics. His research engagements have also explored logistics effectiveness at Sahana Logistics Pvt. Ltd., Bengaluru, offering a well-rounded perspective on supply chain management and operational efficiencies.

His contributions to academia are extensive. He served as a Research Assistant on an ICSSR-funded project at PSG College of Arts & Science, engaging in significant research initiatives that contributed to policy discussions and industry best practices. His research has been showcased at top-tier institutions including IIFT Kolkata, IIM Bangalore, IIM Shillong, IIM Sambalpur, and ISID New Delhi, demonstrating his ability to address critical challenges in international business. With publications in SCOPUS, UGC CARE, and other refereed journals, his work has made a meaningful impact on academic literature.

A passionate academic leader, Prof. Dr. Salman actively participates in academic forums, quality assurance processes, and institutional development activities. His expertise in NAAC accreditation (Criteria 3 & 5) and ISO documentation has enabled him to contribute to curriculum enhancement, research promotion and institutional quality assurance. Additionally, he has served as a resource person and guest speaker at several academic events, sharing his knowledge with students and fellow researchers. His leadership extends to editorial roles-he was the Creative Director of The Godwit: An IB Newsletter (2022-2024) at PSG College of Arts & Science, contributing to academic publications and outreach.

In addition to his academic and research pursuits, Prof. Dr. Salman is a committed social activist. As the Founder of Manitham Ondre, a social foundation, he has successfully organized thirteen major initiatives, including gender equality programs, awareness campaigns and community-driven events. His dedication to social impact is further demonstrated through his volunteer work with the Thiyana Foundation, contributing to the United Nations' Zero Hunger Challenge 2030 initiative. His efforts in social engagement and academia have earned him several accolades, including the Best Paper Award at a national conference organized by Government Arts College, Coimbatore.

His academic excellence is further highlighted by his sixth rank in BBM at Mahatma Gandhi University. His achievements extend beyond academics-he is a state gold medalist in fencing and has represented his university in various sporting events. His leadership capabilities were evident early on when he served as a University Union Councillor at Mahatma Gandhi University, Kerala (2017-18), showcasing his ability to lead and inspire.

With a strong passion for mentoring students, enhancing academic quality and driving institutional excellence, Prof. Dr. Salman Ismail Hassan continues to make significant contributions to the fields of International Business and Supply Chain Management. His unique blend of academic expertise, industry experience, and institutional leadership positions him as a dynamic educator, researcher, and change-maker, dedicated to shaping the future of business education and industry practices."""
            },
            {
                "name": "Prof. Dr. N. Jayanthi",
                "qualifications": "Ph.D - M.S. University, Tirunelveli",
                "designation": "Assistant Professor - Tamil, School of Arts & Natural Sciences",
                "description": """Dr.N.Jayanthi is currently serving as an Assistant Professor in Tamil in the school of Art and Natural Science at Joy University,near Kanyakumari, Tirunelveli, Tamil Nadu. she has her Bachelor of Arts, Master of Arts, Master of philosophy and Doctor of Philosophy from MS University Tirunelveli, Tamilnadu and her Bachelor of Education in Tamil from Tamilnadu teachers education University at Chennai. Additionally a certified course in DTP at ICES, Cochin. 

Dr.N.Jayanthi has a teaching experience of more than 5 years reputed organisation in South Tamilnadu. she has published more than 10 research articles in UGC recognised articles. she has participated in many seminars conferences and presented papers."""
            },
            {
                "name": "Prof. Dr. Mary Christobel R",
                "qualifications": "Ph.D - M.S. University, Tirunelveli",
                "designation": "Assistant Professor - English, School of Arts & Natural Sciences",
                "description": """Committed always to the task of imparting in-depth knowledge and values to the students, Dr. Christobel has worked exceptionally well teaching in various States of India as well as in Spain. Being passionate about mentoring the students to excellence in academics and overall human development, she is currently working at Joy University, Tirunelveli, as an Assistant Professor in the School of Arts and Natural Sciences.

Academic Biography: She has done her Junior College at Vivek Vidyalaya, Goregaon, Mumbai. She has obtained her UG and PG degrees from Madurai Kamaraj University, B.Ed. from Jolarpettai, MPhil from Holy Cross college, Nagercoil, securing the first rank and her Doctoral Degree from Manonmaniam Sundaranar University. She has done Fine Arts at Ken School of Arts, Bangalore. She has a Diploma in Professional Informatics and Internet from Consejería de Educación, Las Palmas de Gran Canaria, Spain.

Research interest: Her research publications focus on the origin and diffusion of Mythology and Religion, psychological factors beneath mythological traditions, mythology and feminism, etc. Her area of interest is mainly Literary theory and criticism, and Shakespearean Studies. Her research interests revolve around posthumanism and its ethical imperatives, and she has conducted seminars cum workshops on Posthumanism for college students. She has guided MPhil., M.A., & B.A. Projects by helping the students develop critical and analytical thinking skills in their approach to various literary texts."""
            },
            {
                "name": "Prof. Dr. S. Prabha",
                "qualifications": "Ph.D - Dept. of Medical Physics, Anna University",
                "designation": "Assistant Professor - Physics, School of Arts & Natural Sciences",
                "description": """Dr. S. Prabha is currently working as an Assistant Professor at the School of Arts and Natural Sciences at Joy University. She holds a Bachelor's degree in Physics and a Master's degree in Physics from Manonmaniam Sundaranar University. She got several awards during her academics and notably she is a university first rank holder in her M.Sc. from Manonmaniam Sundaranar University She completed her Doctoral degree from Department of Medical Physics, Anna University.

Before joining to Joy University, she served as a Research Associate in Laser & Plasma Technology Division, Bhabha Atomic Research Centre, Mumbai and as Assistant Professor in the Department of Physics at Auxilium College.
Her areas of focus in research include Biomaterials, Optical Biosensors, Implants and Nanomaterials. She has authored over 15 research articles in peer reviewed reputed international journals and one book chapter in springer publication. She has participated and presented research papers in various National, International conferences and seminars."""
            },
            {
                "name": "Prof. Dr. V. Adlin Asha",
                "qualifications": "Ph.D - Manonmaniam Sundaranar University",
                "designation": "Assistant Professor - School of Arts & Natural Sciences",
                "description": """She is currently working as an Assistant Professor in the School of Arts and Natural Science, Joy University, Kanyakumari, Tamilnadu, India. She has completed her Bachelor of education and Master of Philosophy from Manonmaniam Sundaranar University Tirunelveli. She has over 14 years of teaching experience in various Engineering Colleges in South Tamilnadu.

She has received the best academic achievement award during her service. She has presented her research papers in leading International and National conferences. She has submitted her thesis in Ph.D titled, 'Studies on the physico-chemical parameters of the seawater of selected fishing harbours of kanyakumari district' in Manonmaniam Sundaranar University Tirunelveli. Her work has shortlisted and published in the SCOPUS, WOS with significant impact factors."""
            },
            {
                "name": "Prof. Dr. C. Preethi",
                "qualifications": "Ph.D - Manonmaniam Sundaranar University",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Dr. C. Preethi is currently serving as an Assistant Professor in the Department of Computing & Information Systems under the School of Computational Intelligence at Joy University, Kanyakumari, Tamil Nadu. She earned her M.E. and B.E. degrees in Computer Science and Engineering from Infant Jesus College of Engineering, affiliated with Anna University, Chennai and Ph.D in Computer Science from Manonmaniam Sundaranar University, Tirunelveli. 

She has gained valuable teaching experience during her tenure at SCAD College of Engineering and Technology and Sri Sarada College for Women. She has published several research papers in SCOPUS, SCI, and Web of Science indexed journals. She also presented her work at numerous national and international conferences, focusing on advanced imaging techniques, AI-based diagnostic tools, and virtual reality applications in healthcare. Her research areas include Medical Image Processing, Virtual Reality, Augmented Reality, Artificial Intelligence and Machine Learning."""
            },
            {
                "name": "Prof. Dr. A. Jagajeeth Paul",
                "qualifications": "Ph.D - Bharathiar University",
                "designation": "Assistant Professor - History, School of Arts & Natural Sciences",
                "description": """Prof. Dr. Jagajeeth Paul is currently serving as an Assistant Professor in the School of Arts and Natural Sciences and in the Department of Humanities and Social Sciences at Joy University, Tirunelveli District, Tamil Nadu. He has a Master's degree in History from Scott Christian College, Nagercoil and doctoral degree from Monomaniam Sundaranar University, Tirunelveli.

Dr. Jagajeeth Paul has published two research papers in ISBN journal, titled Progress of Women's Education in Travancore since 1800 and A Study of Higher Education in Travancore under Sri Moolam Thirunal Maharaja. He served as Assistant Professor of History in Bethany Navajeeevan College of Education, Vencode for seven years. He was appointed as an examiner by TNTEU to conduct practical examination for B.Ed. students in Maruthu Pandiyar College of Education, Thanjavur in April 2022. He has engaged in paper valuation camp conducted by TNTEU, Chennai held at Sri Sharadha College of Education for women, Tirunelveli in in in 2023. He has also attended faculty development program envisioning National Education Policy of 2020 in the year 2023 at Bishop Agniswamy College of Education Muttom."""
            },
            {
                "name": "Prof. Dr. Chockalingam A",
                "qualifications": "Ph.D. - Manonmaniam Sundaranar University, Tirunelveli",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Prof. Chockalingam A is an Assistant Professor in the Department of Computing & Information Systems under the School of Computational Intelligence at Joy University, Kanyakumari, Tamil Nadu, India. He holds a Bachelor's Degree (B.Tech.) and a Master's Degree (M.Tech.) in Information and Communication Technologies, along with a Ph.D. (Thesis Submitted) from Manonmaniam Sundaranar University, Tirunelveli.

 

Prior to joining Joy University, he served as a faculty member at the Manonmaniam Sundaranar University, Tirunelveli, accumulating over four years of teaching and research experience.

He has presented research papers at national and international conferences and has published in SCI and SCOPUS-indexed international journals, conferences, and book chapters in the field of Computer Science. His expertise has led him to serve as a reviewer for reputed international journals, ensuring high-quality scholarly contributions in the field.

During his academic tenure, he has been actively involved in various academic and administrative committees, contributing to curriculum development and institutional governance. His research interests include Machine Learning, Deep Learning, Natural Language Processing (NLP) and Computer Vision."""
            },
            {
                "name": "Prof. Dr. N. Micheal Mathava Visakan",
                "qualifications": "Ph.D - Vellore Institute of Technology, Vellore",
                "designation": "Assistant Professor - School of Arts & Natural Sciences",
                "description": """Dr. N. Micheal Mathava Visakan is an Assistant Professor of Mathematics in the School of Arts and Natural Sciences at Joy University. He completed his B.Sc. in Mathematics at St. Xavier's College, Tirunelveli, followed by an M.Sc. and M.Phil. in Mathematics at St. Joseph's College, Trichy. He earned his Ph.D. in Mathematics from Vellore Institute of Technology (VIT), Vellore, in August 2024.

His research primarily focuses on queueing theory, with expertise in stochastic modeling of retrial queues, optimization techniques in queueing systems, and cost function optimization in service environments. His doctoral thesis, titled Metaheuristic Cost Optimization of a Single Server Retrial Queue with Working Vacation, investigates optimization methodologies in queueing models. He has published eight research articles in Web of Science, SCIE, and SCOPUS-indexed journals.

He has also gained international academic experience. He served as an Assistant Lecturer in Mathematics at DMI St. Eugene University, Lusaka, Zambia, from November 2017 to September 2019. Additionally, he worked as a Research Assistant at Chang Gung University, Taiwan, from September to November 2024."""
            },
            {
                "name": "Prof. Dr. P. S. Stem Edilber",
                "qualifications": "Ph.D - Bharathidasan University",
                "designation": "Assistant Professor - School of Arts & Natural Sciences",
                "description": """Dr. P.S. Stem Edilber is an Assitant Professor of Mathematics in the school of Arts and Natural Science Joy University. He  completed his B.Sc., M.Sc., and M.Phil. in Mathematics at St. Xavier's College in Palayamkottai. He earned his Ph.D. in Mathematics from H.H. The Rajah's College, Pudukkottai, under Bharathidasan University.

His research primarily focuses on stochastic processes, with a particular emphasis on their applications. His doctoral thesis, titled "Application of Stochastic Processes for Dengue Fever," reflects his interest in this area. He has authored seven research publications, all of which are indexed in prestigious journals like SCI, Scopus, and Web of Science.

Between 2019 and 2021, he served as an Assistant Professor at Sigma College of Architecture, where he also taught NATA classes. From 2021 to 2025, he worked as the Department Head and Assistant Professor at St. Alphonsa College of Arts and Science. In addition to his academic roles, he composed several songs in his capacity as a Music Director."""
            },
            {
                "name": "Prof. Dr. Jerish J R",
                "qualifications": "Ph.D. Genetics & Plant Breeding - Tamil Nadu Agricultural University, Coimbatore",
                "designation": "Assistant Professor - School of Agricultural Sciences",
                "description": """Dr. Jerish J R had obtained his Ph.D. in Genetics and Plant Breeding from Tamil Nadu Agricultural University, Coimbatore. During his doctoral degree programme he was served as Research fellow and received fellowship from GOI-BRNS-Groundnut Scheme of BARC (Bhabha Atomic Research Centre) operated at Department of Genetics and Plant Breeding, V.O.C. Agricultural College and Research Institute, Killikulam for two years and after that he worked as SRF (Senior Research Fellow) and associated few UG courses for six months under the same scheme.

He had completed his M.Sc. (Agriculture) with a gold medal in "Quantitative Genetics" subject and B.Sc. (Agriculture) with distinction from Faculty of Agriculture, Annamalai University, Chidambaram. He also obtained PGDSSA (Post Graduate Diploma in Software Based Statistical Analysis) from Faculty of Science, Annamalai University and HDCP (Honours Diploma in Computer Programme) from Computer Software College, Tirunelveli.

He had published 4 Research Article in international journal of NAAS more than six and 3 articles in National Journal. He had also written 4 Book Chapters (Agri Gate), attended 7 trainings, 3 international and 6 national conferences and also 2 national webinars. He also served as an Organizing committee member in GOI-DST-SERB sponsored training programme and in APHISA-2025 held at V.O.C. AC & RI Killikulam.

His area of interest includes Statistical Genetics, Reverse Genetics, Groundnut Breeding, Improvement of Oil seeds, Cereals & Millets Breeding and Mutation Breeding. Finally, his hobbies include playing violin, chess, basketball and badminton."""
            },
            {
                "name": "Prof. Dr. Nishi S Das",
                "qualifications": "Ph.D. - Noorul Islam College for Higher Education, Thuckalay",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Dr. Nishi S Das is currently an Assistant Professor in the School of Computational Intelligence at Joy University, Tirunelveli. She previously served as an Associate Professor and Research Dean in the Department of Electrical and Electronics Engineering at Baselios Mathews II College of Engineering, Kollam, Kerala, India. She received her PhD in Medical Image Processing from Noorul Islam College of Higher Education. In recognition of her scholarly contributions, she was honoured with the "Research Excellence Award" by InSc in 2020.

Dr. Das has published extensively in reputable national and international journals and has presented numerous academic and research-based papers at conferences across the globe. Her research interests include Medical Image Processing, Digital Electronics, Communication Systems, Information Theory, and Coding."""
            },
            {
                "name": "Prof. Nandhakumar.R",
                "qualifications": "Ph.D (Thesis submitted) - Vellore Institute of Technology, Vellore",
                "designation": "Assistant Professor - School of Engineering",
                "description": """I have submitted my Ph.D. thesis in the area of Additive Manufacturing at VIT University, Vellore. My research focuses on the optimization of process parameters to enhance performance and precision in additive manufacturing systems. I am currently working as an Assistant Professor in the School of Engineering and Technology at Joy University.

My academic interests include additive manufacturing, advanced materials, optimization techniques, and intelligent manufacturing systems."""
            },
            {
                "name": "Prof. Dr. D. Vanitha",
                "qualifications": "Ph. D (Commerce) - Bharathiar University & Coimbatore",
                "designation": "Assistant Professor - School of Entrepreneurship & Management",
                "description": """Dr. D. Vanitha is currently serving as an Assistant Professor at the School of Entrepreneurship and Management, Joy University, Kanyakumari, Tamil Nadu. She brings over 17 years of teaching experience to her role. She holds a Master's degree in International Business, along with an M.Phil. and a Ph.D. in Commerce from Bharathiar University, Coimbatore.
 

Dr. Vanitha has actively participated in numerous national and international seminars and conferences, presenting scholarly papers. She has published several research articles in reputed peer-reviewed journals and contributed to five book chapters. She has also published several patents and developed E-Content for her courses.
Her dedication to academic excellence has earned her the Best Faculty Award. Committed to continuous learning, she has completed multiple online certification courses through NPTEL, Coursera, and other MOOCs platforms.
Dr. Vanitha is passionate about guiding students in industry-oriented projects and provides support for their emotional well-being. Her holistic approach to education encourages both academic and personal growth in her students."""
            },
            {
                "name": "Prof. Sahaya Rishoba",
                "qualifications": "MBBS - Beihua University, China",
                "designation": "Assistant Professor - School of Life & Health Sciences",
                "description": """I have completed my Bachelor of Medicine, Bachelor of Surgery at beihua university jilin,china.I served as a Medical Officer in various reputable healthcare institutions from 2019 to 2025 at Nagercoil.Proficient in diagnosing, treating, and managing a wide range of acute and chronic medical conditions across diverse patient populations. Demonstrated expertise in outpatient and inpatient care, emergency response, preventive medicine, and patient education.

Adept at working in multidisciplinary teams, maintaining detailed medical records, and ensuring adherence to clinical protocols and ethical standards."""
            },
            {
                "name": "Prof. Dr. R. L. Babisha Julit",
                "qualifications": "Ph. D. - Manonmaniam sundaranar University, Thirunelveli",
                "designation": "Assistant Professor - School of Arts & Natural Sciences",
                "description": """Dr. R. L. Babisha Julit is an Assistant Professor in the Department of Mathematics at JOY University. She earned her Ph.D. in Mathematics from Manonmaniam Sundaranar University, Thirunelveli, with research conducted at G. V. N. College, Kovilpatti. Her postgraduate and M.Phil. studies were completed at St. Xavier's College, Palayamkottai, and her undergraduate degree was from Holy Cross College, Nagercoil. Her research focuses on Neutrosophic Topological Spaces, with areas of expertise in Topology, Fuzzy Set Theory and it's generalizations, and Analysis.

With 3 years of experience in teaching and research, Dr. Babisha Julit has published numerous papers in reputable journals and conferences."""
            },
            {
                "name": "Prof. Dr. Jenila. J",
                "qualifications": "Ph.D. - Clinical Pathology, Bundelkhand University, Jhansi",
                "designation": "Assistant professor - School of Life & Health Sciences",
                "description": """I have completed my bachelor's and master's degree from the Vivek institute of laboratory medicine under Dr M. G. R  University. I obtained my doctoral degree in clinical pathology from the University of Bundelkhand, Jhansi.

I also have one year of experience in research and academia ( KMMC Medical college, Mutton)"""
            },
            {
                "name": "Prof. Dr. I Sofiya",
                "qualifications": "Ph.D. - Manonmaniam Sundaranar University",
                "designation": "Assistant professor - School of Computational Intelligence",
                "description": """I am an academic professional specializing in Object-Oriented Programming, Java, and Data Structures. I have teaching and mentoring experience in these core areas of computer science, with a focus on helping students build strong problem-solving and programming skills. My academic interests include software development methodologies, algorithm optimization, and applications of programming concepts in real-world problem solving.

I am committed to fostering an engaging learning environment, guiding students in projects, and contributing to the overall academic growth of the institution."""
            },
            {
                "name": "Prof. Dr. Aswathy.C",
                "qualifications": "Ph.D. - Manonmaniam Sundaranar University",
                "designation": "Assistant Professor - School of Life & Health Sciences",
                "description": """I am Dr. Aswathy Chelladurai, a researcher and educator with a Ph.D. in Nanoscience. My work focuses on Chemistry, Nanotechnology, and their applications in pharmaceuticals, biomedical sciences, and environmental sustainability. I have published research on nanocomposites, green synthesis of nanoparticles, and their biomedical potential.

Teaching is my passion, and I strive to simplify complex scientific concepts through real-world examples that inspire curiosity and active learning. Alongside academics, I am involved in scientific outreach, career guidance, and community engagement. My goal is to mentor students to think innovatively and apply science for meaningful societal impact"""
            },
            {
                "name": "Prof. Dr. J.N.Cheerlin Mishma",
                "qualifications": "Ph.D. - Manonmaniam Sundaranar University",
                "designation": "Assistant Professor - School of Arts & Natural Sciences",
                "description": """Prof. Dr. J.N. Cheerlin Mishma is currently serving as an Assistant Professor in the School of Arts and Natural Sciences and in the Department of Applied Physics at Joy University, Tirunelveli District, Tamil Nadu. Dr. J.N. Cheerlin Mishma is an accomplished researcher and academic specializing in Computational Physics, Quantum Chemistry, and Molecular Modelling, with extensive expertise in Density Functional Theory (DFT), Molecular Docking, and Spectroscopic Characterization. With a remarkable academic foundation comprising a Ph.D. in Physics with an Outstanding grade from Manonmaniam Sundaranar University in the field of Physics (Spectroscopy).

Her prolific research contributions include 28 Scopus-indexed publications, 21 conference papers, and collaborations with internationally recognized scientists across diverse domains such as drug discovery, nanomaterials, corrosion inhibition, and bioactive molecular design. She has collaborated internationally with distinguished researchers from institutions across India, Saudi Arabia, Turkey, and Mexico, advancing the frontiers of computational and molecular sciences.

She has been the recipient of multiple prestigious honours, including the International Most Prominent Researcher of the Year Award in Physics (ISTRA, 2024), Best Theoretical Research Award (International Research Excellence Awards, 2025), Women Achiever Award (M.S. University, 2024), Best Young Researcher Award (2022) and Inspiring Education Hero Award (Southern India Conclave, Kochi). Her works have appeared in reputed journals like the Journal of Molecular Liquids, Journal of Molecular Structure, Computational and Theoretical Chemistry, and Spectroscopy Letters.

Dr. Cheerlin Mishma's scholarly influence is reflected in her Google Scholar citation count of 166, h-index of 8, and i10-index of 6, underscoring her growing impact in theoretical and computational research.
Beyond her research excellence, Dr. Cheerlin Mishma has demonstrated strong academic versatility with multiple postgraduate diplomas in Advanced Scientific Interfacing, Human Resource Management, and Computer Applications. She is proficient in advanced computational tools such as GAUSSIAN 09/16, GaussView, ChemCraft, Discovery Studio, Mercury, AutoDock, and Origin.

Her professional journey reflects a commitment to scientific innovation, interdisciplinary collaboration, and mentoring excellence, making her a dynamic contributor to both academia and research."""
            },
            {
                "name": "Prof. Dr. E. Janani",
                "qualifications": "Ph.D - VIT University",
                "designation": "Assistant Professor - School of Arts & Natural Sciences",
                "description": """I have completed my Ph.D from VIT University, Vellore. My research interests are focused on Graph Theory, particularly in Topological Indices of chemical molecular graphs and networks."""
            },
            {
                "name": "Prof. Dr. Melbha Starlin Chellathurai",
                "qualifications": "Ph.D. - Universiti Malaya, Malaysia",
                "designation": "Assistant Professor - School of Pharmacy",
                "description": """Passionate educator and researcher with more than 10 years of experience in pharmaceutical technology. Expertise in curriculum development, hybrid teaching methodologies and researched on novel drug delivery systems like microneedles and nanoparticles. Recognised for innovative teaching and research contributions with awards. Published and presented papers in Q1 journals and in international conferences.

Supervised final year undergraduate student projects and the products were exhibited in international expos."""
            },
            {
                "name": "Prof. Dr. Gopi Kannan",
                "qualifications": "Ph.D - Manonmaniam Sundaranar University",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Specialist in Deep Learning"""
            },
            {
                "name": "Prof. Rahul",
                "qualifications": "M.Tech - NIT Jalandhar",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Prof. Dr. Rahul is currently serving as an Assistant Professor in the School of computational intelligence at Joy University, Kanyakumari, Tamil Nadu. He has completed his schooling from Birla School Pilani. He has his Bachelor's degree in Electronics and Communication from Kurukshetra University, Kurukshetra and Master's degree in Control and Instrumentation from National Institute of Technology Jalandhar.

Prof. Rahul has qualified GATE Exam (Electronics and Communication) 4 times. He has worked as a coordinator for many workshops and conferences and he has also attended more than ten conferences and workshops. His areas of interest in research are Wireless Sensor Network, Optimization techniques using AI, Soft computing, Reinforcement Learning. His other interests are travelling, Badminton, Cricket, cooking etc."""
            },
            {
                "name": "Prof. R. K.Varrsha",
                "qualifications": "LLM - Tamil Nadu Dr. Ambedkar Law University",
                "designation": "Assistant Professor - School of Law",
                "description": """Mrs. R.K.Varrsha, B.A.LL.B, LLM, Ph.D working as an Assistant Professor of Law, School of Law, Joy University. She has completed her LLM in Criminal Law and Criminal Justice Administration and her Dissertation research was on the topic "Animal Cruelty: Effectiveness of Law in its Prevention in India" from Tamilnadu Dr. Ambedkar Law University, School of Excellence in 2021

She has completed her Bachelor Degree [B.A.,LL.B] (2014-2019) at Vaikunta Baliga College of Law, Udupi, Karnataka and Master of Laws [LLM] (2019-2021) at Tamilnadu Dr. Ambedkar Law University, School of Excellence. Also, she enrolled as an Advocate in the Bar Council of Tamil Nadu & Puducherry and cleared the All-India Bar Examination in 2019. She has practiced at Madras High court and Lower courts for a period of 1 year in Civil, Criminal, Labour, Debt Recovery Tribunals, Family matters. She has worked as an Assistant Professor of Law from 2021 in UGC recognized deemed University Law college and has a total experience of 2.6 years in this field. In her previous endeavours, she has been a coordinator of admissions, sports, legal aid, State Human Rights Commission internships, Culturals, NAAC. She has also conducted and participated in various Conferences and Workshops.

She has secured overall 2nd rank in Karnataka State Law University for the year 2014-2019. She has participated at National level Throw ball held at Guwahati, Assam in the year 2013-2014 and also represented Karnataka State Law University at South-Zone Inter-University Volleyball in the year 2018 and 2019. She has also represented participated and volunteered in various National Moot Court Competitions at various colleges. Her specialization in teaching is Criminal Laws."""
            },
            {
                "name": "Prof. M. Surendar",
                "qualifications": "LLM - Tamil Nadu Dr. Ambedkar Law University",
                "designation": "Assistant Professor - School of Law",
                "description": """Mr. M. SURENDAR, is currently serving as Assistant Professor of Law at School of Law Joy University, Kanyakumari, Tamil Nadu , He has his Bachelors degree in Mechanical Engineering from Anna University, and in his own interest and efforts, he has completed LL.B(Hons) (UG) and Masters degree in Business Law (LL.M) from Tamilnadu Dr. Ambedkar Government Law University, Chennai, Tamilnadu and he also holds a Diploma in Police Administration from Madras University, Chennai, Tamilnadu.

Before joining Joy University he worked as Legal Compliance Specialist / Corporate Advisor for leading Healthcare industries, Educational sectors and Manufacturing companies in India, after completing his PG in Law he has emerged as an Academician and served as Assistant Professor of Law at School of Law VTU University Chennai, Tamilnadu. Throughout his career as an Academician he has conducted various programs like International Faculty Development Program, National Moot Court Competition, National Workshop and other Law school competitions. He has been a NAAC and BCI coordinator.

He was awarded as Best Speaker - Male Advocate with a prize amount of Rs. 5000/- and a Trophy in National Moot court competition held at Mumbai in March 2018. He was awarded with a Gold Medal for reaching Semi final in a National Trial Advocacy Competition held at Chennai in August 2018. He was awarded with Runners up Trophy in National Client Counseling Competition held at Mumbai in March 2019 during his Studies. He has successfully completed his PG dissertation on A Crtitical Analysis of Life Insurance and its business in India. His areas of interest include Cyber Laws, Constitutional Law, IPR, Commercial Contract laws etc.,"""
            },
            {
                "name": "Prof. Rajesh Bharathi",
                "qualifications": "M.A . M.L., - University of Madras",
                "designation": "Assistant Professor - School of Law",
                "description": """Passionate about teaching, mentoring, and fostering critical thinking in students. Demonstrates a deep commitment to academic excellence, legal research, and institutional service. Actively involved in National Service Scheme (NSS) programs, promoting social awareness, civic engagement, and community service among students. A strong advocate for student wellness and development, with a hands-on role in organizing and mentoring student sports activities, inter-college competitions, and fitness initiatives.

Regularly engages in voluntary programs focusing on legal literacy, gender sensitization, and rural outreach.Successfully organized and led an All-India Educational Tour, providing students with exposure to India's legal, constitutional, and cultural landmarks."""
            },
            {
                "name": "Prof. Nikhil Harikumar P",
                "qualifications": "LL.M - IIT Kharagpur, West Bengal",
                "designation": "Assistant Professor - School of Law",
                "description": """Mr. Nikhil Harikumar P is currently serving as an Assistant Professor of Law at the School of Law, Joy University. He holds a Master's degree (LL.M.) in Intellectual Property Laws from the esteemed Rajiv Gandhi School of Intellectual Property Law, IIT Kharagpur, graduating with distinction. Prior to that, he completed his integrated Bachelor's degree in Law and Business Administration (B.B.A. LL.B.) from Government Law College, Kozhikode.

His primary research interests include Intellectual Property Management, IP Jurisprudence, and the intersection of Law and Religion."""
            },
            {
                "name": "Prof. Sruthy Murugan Usha",
                "qualifications": "LL.M(Intellectual Property Rights) - Saveetha School of Law, SIMATS, CHENNAI",
                "designation": "Assistant Professor - School of Law",
                "description": """Sruthy Murugan Usha is currently serving as Assistant Professor at the School of law, Joy University. She is a dedicated and passionate academician with 2.6 years of teaching experience in the field of law. She holds a Postgraduate degree (LL.M) in Intellectual Property Rights from Saveetha School of Law, SIMATS and a Bachelor's degree in Law (B.A. LL.B) from Ramaiah College of Law, affiliated to Karnataka State Law University, Hubli. She is a university rank holder in 2018 and is currently pursuing her Ph.D. in Law from Saveetha School of Law, SIMATS, having enrolled in the year 2023.

 

She was enrolled as an Advocate in the Bar Council of Tamil Nadu & Puducherry in 2020 and has consistently contributed to both academic and professional spheres. She has expertise in Trademark registration and Filing. During her academic journey, she actively participated in numerous national and international seminars and conferences, reflecting her commitment to continuous learning and professional development.

Apart from her teaching responsibilities, she has played a pivotal role in organizing several seminars including national seminars, workshops, international conferences, expert lectures, industrial visits, legal awareness initiatives, and community outreach programs across Chennai and Kanchipuram districts. Her efforts have also significantly contributed to promoting women empowerment through legal education and social awareness campaigns. With a strong foundation in law, a passion for intellectual property rights, and a commitment to social justice, she continues to inspire and empower the next generation."""
            },
            {
                "name": "Prof. Solomen Jasmine Rajakumar",
                "qualifications": "M.L.(Property LAW), SET (Law) Qualified School of Excellence In Law - Tamil Nadu Dr. Ambedkar Law University, Chennai",
                "designation": "Assistant Professor - School of Law",
                "description": """Solomen Jasmine Rajakumar is a committed legal academician and practitioner with over a decade of multifaceted experience spanning litigation, corporate legal services, legal research, and higher education. She is an alumna of the School of Excellence in Law, TNDALU, Chennai, where she earned her integrated B.A.,B.L. (Hons.) degree. She later specialized with a Master's in Property Law from the Tamil Nadu Dr. Ambedkar Government Law College, Chennai. Her M.L. dissertation had extensive research on the concept of "Passing off in Trademarks" in Intellectual Property Rights. She successfully cleared the State level Eligibility Test (SET) in Law, conducted by Mother Teresa Women's University in 2017, further establishing her academic credentials.

Her legal journey began under the mentorship of Senior Advocate Mr. S. Prabakaran at the Madras High Court, gaining extensive courtroom experience across diverse legal domains. She was enrolled as an Advocate on September 2012 and successfully qualified in the All India Bar Examination conducted on June 2013.

Jasmine has worked in both litigation and corporate environments, including her role as Legal Assistant at Apollo Hospitals Enterprise Ltd., Chennai, where she handled medico-legal documentation, legal notices and consumer court proceedings involving medical negligence. Her experience extends to Merrill Technology Pvt. Ltd., where she served as a Legal Associate in the LPO division, contributing to international legal documentation and compliance.

She further expanded her corporate legal expertise through her work with a Company Secretary, assisting in statutory compliance, board resolutions, and annual filings with the Ministry of Corporate Affairs. At Zenith Lex and Co., a reputed banking law firm in Chennai, she was involved in preparing vetting reports, ROC reports, and title opinions for loan documentation, which were reviewed and sent to various financial institutions. Additionally, her role as a Legal Analyst at Asia Legal Dimensions involved reading and analyzing case laws to draft legal headnotes and summaries for judicial reference.

In the academic space, Jasmine has served as Lecturer at School of Excellence in Law, TNDALU, Chennai and Dr. Ambedkar Government Law College, Chengalpattu, where she taught various core legal subjects and mentored aspiring legal professionals. She also contributed to judicial research as a Law Clerk to Hon'ble Justices Jyothimani and Jaichandren at the Madras High Court, assisting with precedent analysis and legal referencing.

Her research interests is evident as she has presented a paper titled "Intellectual Property Rights and Passing Off" at an international conference hosted in collaboration with Siyah Kuala University, Indonesia, at Sathyabama Institute of Science and Technology, Chennai. The work was later published in LegalFoxes Law Times Journal (ISSN: 2582-6034). During her academic years, she actively participated in national-level competitions, notably representing her institution in the National Moot Court Competition conducted by Raja Lakhamgouda Law College, Belgaum, Karnataka.

With a holistic legal background that bridges practice, research, and education, Prof. Jasmine brings a distinctive blend of academic rigor and real-world insight, committed to empowering future generations of legal professionals through excellence in legal education."""
            },
            {
                "name": "Prof. Mrs. Feba Varghese",
                "qualifications": "M.Sc. ASRB NET - Kerala Agricultural University",
                "designation": "Assistant Professor - School of Agricultural Sciences",
                "description": """Feba Varghese is an enthusiastic in Horticulture and she has 4 years of expertise in the field of Horticulture. She worked as farm officer, Agri forestry graduate and Assistant Professor in various government institutions in Kerala. She was part of the organising committee of various international seminars in KAU. Under the training service scheme of KAU she has organized several trainings for farmers of Thiruvananthapuram district. She played a crucial role in coordinating afforestation activities in the mined out and refilled areas of Kerala Minerals and Metals Limited, A govt of Kerala Undertaking, Chavara, Kerala. She has worked as Assistant Professor at College of Agriculture, Vellayani, Kerala for One year also.

She has 4 journal articles and one popular article in her credit. She did postgraduation in Horticulture from Kerala Agricultural University and has cleared ASRB NET in Vegetable Science. As part of her post graduation research work she has experience in hybridisation in vegetable crops. Also she is certificate holder in Word processing and data entry course by Keltron. Her Graduation is in Horticulture from DBSKKV, Dapoli, Maharashtra. Her schooling and higher education is from Kerala itself."""
            },
            {
                "name": "Prof. Sreelakshmi P",
                "qualifications": "MSc. Soil Science & Agricultural Chemistry - Kerala Agricultural University, Thrissur",
                "designation": "Assistant Professor - School of Agricultural Sciences",
                "description": """Currently pursuing PhD from Kerala Agricultural University. Qualified for ICAR ASRB NET and Gold medalist in UG. Worked as Agricultural Officer in Govt of Kerala and also worked as course teacher for diploma students in KAU and conducted different On -Job-Training (OJT) classes for vocational higher secondary students. Has published numerous articles in International journals, book chapters, worked as co-editor and attended different national and international conferences and also awarded for the best oral presentation in International conference on Natural farming Innovation jointly organized by ICAR and Cambridge international agricultural organizations and in National seminar on soil and water symbiosis for sustainable agriculture conducted by KAU.

Recently awarded as "Young Soil Scientist " on the occasion of Global Agricultural Conference organized by Agrimeet foundation Bharat, UGC MMTTC Jodhpur and Southern Federal University, Russia. Also has participated and awarded in various inter university and National level cultural programs conducted by AgriUnifest (under ICAR) Area of interest is Soil pedology, Soil fertility and nutrient management with novel aspects on remote sensing and GIS techniques."""
            },
            {
                "name": "Prof. R. S. Haritha Shree",
                "qualifications": "Qualified UGC NET English, M.A. English -Thiagarajar College Madurai",
                "designation": "Assistant Professor - School of Arts and Natural Science",
                "description": """R.S. Haritha Shree is an Assistant Professor of English at the School of Arts and Natural Science, Joy University. She holds a Master's degree in English from Thiagarajar College, Madurai. Her dissertation, "Jazzing the Jim Crow," explores the intricate relationship between African American Literature and Art Therapy Psychology.

Ms.Haritha has successfully qualified the UGC National Eligibility Test (NET) for Assistant Professor in December 2023. She also possesses a Diploma in Human Rights, further enriching her academic profile.Beyond her academic pursuits, Ms.Haritha has had a distinguished career in the National Cadet Corps (NCC), achieving the rank of Lieutenant Colonel and earning an 'A' Certificate.

Her research interests primarily focus on Hermeneutics, with a particular emphasis on Contemporary Theory and Language. She has actively contributed to the academic community by participating in various national seminars and presenting research papers like , "Dystopian Bend in Adiga's 'Between the Assassinations'. Currently, her research is centered on Cognitive Linguistics and Language."""
            },
            {
                "name": "Prof. Sowdhanya.M.R",
                "qualifications": "MBA, MSc(N) - Rajiv Gandhi University of health sciences, Bangalore",
                "designation": "Assistant professor - School of Nursing",
                "description": """Mrs.Sowdhanya.M.R currently going to serve in joy university as assistant professor.I have completed MSc nursing in shanthi dhama college of nursing under Rajiv Gandhi University of health sciences, Bangalore and my MBA in Alagappa university,karaikudi.i worked as IVF OT nurse in dara al bara medical centre,kuwait for 5 years and 2 years as a assistant professor after my PG in Maa shahzadi devi memorial nursing college, uttarpradesh.As Dedicated Assistant Professor with 4 years of experience in nursing education, curriculum development, and clinical instruction. Proven ability to design and deliver engaging courses, foster student learning outcomes,

and mentor aspiring nurses. Committed to preparing students for successful careers in diverse healthcare settings"""
            },
            {
                "name": "Prof. An Belin Felicsona",
                "qualifications": "M.E., - Sathyabama University& Chennai",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Prof. An Belin Felicsona is currently serving as an Assistant Professor in the Department of Computing and Information Systems under the School of Computational Intelligence at Joy University, Kanyakumari, Tamil Nadu, India. She holds a Master of Engineering (M.E.) in Applied Electronics from Sathyabama University, Chennai, and a Bachelor of Engineering (B.E.) in Electronics and Communication Engineering from Rajalakshmi Engineering College, Chennai.
 

Currently, she is pursuing her Ph.D. in Information Technology and Mobile Network Communication at the Universidade da Coruña, Spain (enrolled in 2024), focusing on the design and numerical simulation of Time-Modulated Antenna Arrays (TMAAs) using various pulse waveforms. Her research aims to enhance beam steering, harmonic suppression, and radiation efficiency in wireless, radar, and satellite communication systems.
She has served as a Teaching and Research Assistant at Shiv Nadar University, Greater Noida, where she contributed to academic support, student guidance, and RF research activities. With extensive teaching and research experience in multiple reputed institutions, she has developed strong expertise in antenna design, RF and microwave circuit simulation, and industry-standard tools such as Keysight ADS, Pathwave System Design, and CST Microwave Studio.
She has been honored with prestigious recognitions, including support from the European Union's Communication Technologies, Coding and Processing for Next Generation Classical Quantum Networks (MADDIE) Project, and the SNU Doctoral Fellowship sponsored by the HCL Technologies Foundation."""
            },
            {
                "name": "Prof. Fernando Sahaya Mary Albeena",
                "qualifications": "M.E., - RIT Nagercoil, Anna University of Chennai",
                "designation": "Assistant Professor - School of Computational Intelligence",
                "description": """Prof. Albeena is currently working as an Assistant Professor in the Department of the School of Computational Intelligence at Joy University, Kanyakumari, Tamil Nadu, India. She holds a Bachelor's degree in Information Technology from CSI College of Engineering, affiliated with Anna University, Chennai, and a Master's degree (M.E.) in Computer Science and Engineering from RIT, also under Anna University, Chennai.
 

Before joining Joy University, she served as a Professor at a college affiliated with Mumbai University. She brings over 7 years of teaching experience and 6 month of industry experience as a Software Developer.

She has actively presented papers at leading academic institutions and has contributed to a Tamil Nadu Government project. Additionally, she has completed a certification course from Microsoft in .NET and App Development.

Her areas of interest include Blockchain Technology and Machine Learning."""
            },
            {
                "name": "Prof. Haripriya M",
                "qualifications": "MSc. Counseling psychology (UGC NET Qualified) - St. Joseph's University, Bengaluru",
                "designation": "Assistant Professor - School of Arts & Natural Sciences",
                "description": """Haripriya M is an Assistant Professor of Psychology at the School of Arts and Natural Sciences, Joy University. She is a committed academician and counseling professional with a Master's degree in Counseling Psychology. Her master's dissertation, "A Comparative Study between Personality Traits and Sleep Hygiene Association among College Students with Respect to Class Starting Time", reflects her keen interest in student well-being and the role of psychological and behavioral factors in academic performance.

She has qualified the UGC-NET, demonstrating her strong foundation in research and higher education. In addition, she is certified in Cognitive Behavioral Therapy (CBT), which strengthens her ability to bring evidence-based practices into both counseling and teaching.

Ms. Haripriya's research interests span the psychological well-being of students, positive psychology, and the intersection of policy-making with mental health. Drawing upon her professional counseling experience, she incorporates real-world case insights into classroom discussions, enabling students to connect psychological concepts with lived experiences."""
            },
            {
                "name": "Prof. P. Sandhiya",
                "qualifications": "M.Optom - Saveetha University, Chennai",
                "designation": "Assistant Professor - School of Life & Health Sciences",
                "description": """Ms. Sandhiya palani completed M. Optom at saveetha university. I am interested to teach in both clinical and academic aspects includes contact lens specialist, vision therapist, low vision rehabilitation and community eye care services."""
            },
            {
                "name": "Prof . T. Vijitha",
                "qualifications": "M.Sc - Dr.M.G.R.Medical University, Nehru Nursing college, Vallioor",
                "designation": "Assistant Professor - School of Nursing",
                "description": """As a graduate with an M.Sc. in Medical-Surgical Nursing is an advanced practice nurse specializing in the care of adult patients with complex health issues. It combines extensive clinical expertise with advanced knowledge in nursing theory, research, and leadership.
 

And I have an ideal for roles such as a Clinical Nurse Specialist, Nurse Educator, or Nursing Manager, where advanced clinical knowledge and leadership are essential to improving healthcare delivery and patient outcomes."""
            },
            {
                "name": "Prof. Narashimma Jainthan L",
                "qualifications": "L.L.M (Taxation Law) - Tamilnadu Dr Ambedkar Law University (School of Excellence In Law)",
                "designation": "Assistant Professor - School of Law",
                "description": """I, L. Narashimma Jainthan, am a passionate law educator with a strong academic background and a commitment to advancing legal scholarship and student learning. Currently, I serve as a Guest Lecturer at the School of Excellence in Law, Tamil Nadu Dr. Ambedkar Law University, where I have been teaching since November 2021. I handle a wide range of subjects, including Taxation Law, Environmental Law, Human Rights in Constitutional Law, Corporate Securitisation, Land Laws, and Research Methodology, catering to both undergraduate and postgraduate students.

I hold an LL.M. in Taxation Law from the School of Excellence in Law, Chennai, and an LL.B. from the Government Law College, Tirunelveli. Additionally, I pursued an M.A. in Criminology and Criminal Justice Administration through Tamil Nadu Open University, reflecting my interdisciplinary interests. My academic journey began with a B.Sc. in Chemistry, which provided me with an analytical approach to problem-solving.

Beyond teaching, I actively contribute to academia through research and publications. I have presented and published several papers at national and international conferences on topics such as international taxation, foreign direct investment, medical tourism, environmental sustainability, human rights, and prisoners' rights. My postgraduate dissertation focused on tax avoidance through treaty shopping, an area of growing global significance.

I have also served as a resource person for National Human Rights Commission-sponsored training programs, engaging with students on the importance of human rights awareness. Additionally, I have participated in faculty development programs, workshops, and seminars that enhanced my pedagogical and research skills.

With strong communication skills, research aptitude, and a dedication to student growth, I strive to make legal education practical, dynamic, and socially relevant. My long-term aspiration is to contribute meaningfully as a faculty member, combining my academic knowledge, research insights, and teaching experience to inspire future legal professionals."""
            },
            {
                "name": "Prof. John Singh Russel E",
                "qualifications": "M.Pharm - The TamilNadu Dr MGR Medical University",
                "designation": "Assistant Professor - School of Pharmacy",
                "description": """A highly dedicated result oriented Pharmacist with 20+ yrs in industry and 3.5 yrs in teaching Pharmacy graduates. Had worked in various Pharmaceutical industries in India as well as abroad. 
Had undertaken greenfield projects for new Manufacturing units and successful completion of the same.

Had been into Operations and Facility management (Head)."""
            },
            {
                "name": "Prof. Gopinath",
                "qualifications": "M.Sc Anesthesia Technology - SRM Medical University",
                "designation": "Assistant Professor - School of Life & Health Sciences",
                "description": """Highly accomplished and dedicated Anesthesia Technology Educator and Operating Theatre Technologist with 5 years of integrated academic and extensive hands-on clinical experience. Proven expertise in developing and delivering high-quality, standards-aligned curriculum in anesthesia principles, pharmacology, and perioperative care, fostering dynamic, student-centered learning environments. Clinically proficient across specialties, including Laparoscopic, OBG, and Pediatric surgeries, with advanced skills in surgical scrubbing, anesthesia support and monitoring, and sterile processing (CSSD).

Actively engaged in curriculum development, research, and academic leadership, dedicated to mentoring future professionals while upholding the highest standards of patient safety and technical excellence. (BLS/ACLS Certified)"""
            }
        ]

        for faculty in faculty_data:
            obj, created = Faculty.objects.get_or_create(
                name=faculty["name"],
                defaults={
                    "qualifications": faculty["qualifications"],
                    "designation": faculty["designation"],
                    "description": faculty["description"],
                    "photo": "faculty_photos/default.jpg",  # Set default photo
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added faculty: {faculty["name"]}'))
            else:
                self.stdout.write(f'Faculty already exists: {faculty["name"]}')

