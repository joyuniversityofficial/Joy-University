// Joy University Site JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Hero Slider
    const heroSlides = document.querySelectorAll('.hero-slide');
    const heroIndicators = document.querySelectorAll('.carousel-indicator');
    let currentSlide = 0;

    function showSlide(index) {
        heroSlides.forEach(slide => slide.classList.remove('active'));
        heroIndicators.forEach(indicator => indicator.classList.remove('active'));

        heroSlides[index].classList.add('active');
        heroIndicators[index].classList.add('active');
        currentSlide = index;
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % heroSlides.length;
        showSlide(currentSlide);
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + heroSlides.length) % heroSlides.length;
        showSlide(currentSlide);
    }

    // Auto slide
    setInterval(nextSlide, 5000);

    // Manual controls
    document.querySelector('.carousel-control.next')?.addEventListener('click', nextSlide);
    document.querySelector('.carousel-control.prev')?.addEventListener('click', prevSlide);

    heroIndicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => showSlide(index));
    });

    // News Carousel
    const newsTrack = document.querySelector('.news-track');
    const newsCards = document.querySelectorAll('.news-card');
    let newsCurrentIndex = 0;

    function updateNewsCarousel() {
        if (newsTrack) {
            const cardWidth = newsCards[0]?.offsetWidth + 20 || 320;
            newsTrack.style.transform = `translateX(-${newsCurrentIndex * cardWidth}px)`;
        }
    }

    document.querySelector('.news-next')?.addEventListener('click', () => {
        if (newsCurrentIndex < newsCards.length - 3) {
            newsCurrentIndex++;
            updateNewsCarousel();
        }
    });

    document.querySelector('.news-prev')?.addEventListener('click', () => {
        if (newsCurrentIndex > 0) {
            newsCurrentIndex--;
            updateNewsCarousel();
        }
    });

    // Testimonial Slider
    const testimonialSlides = document.querySelectorAll('.testimonial-slide');
    const testimonialIndicators = document.querySelectorAll('.testimonial-indicator');
    let testimonialCurrent = 0;

    function showTestimonial(index) {
        testimonialSlides.forEach(slide => slide.classList.remove('active'));
        testimonialIndicators.forEach(indicator => indicator.classList.remove('active'));

        testimonialSlides[index].classList.add('active');
        testimonialIndicators[index].classList.add('active');
        testimonialCurrent = index;
    }

    function nextTestimonial() {
        testimonialCurrent = (testimonialCurrent + 1) % testimonialSlides.length;
        showTestimonial(testimonialCurrent);
    }

    // Auto testimonial change
    setInterval(nextTestimonial, 6000);

    testimonialIndicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => showTestimonial(index));
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Mobile menu toggle
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');

    menuToggle?.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!menuToggle.contains(e.target) && !navMenu.contains(e.target)) {
            navMenu.classList.remove('active');
        }
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.style.borderColor = '#dc3545';
                    isValid = false;
                } else {
                    field.style.borderColor = '#28a745';
                }
            });

            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });

    // Animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });

    // Lazy loading images
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });

    // Back to top button
    const backToTopBtn = document.querySelector('.back-to-top');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTopBtn.style.display = 'block';
            } else {
                backToTopBtn.style.display = 'none';
            }
        });

        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Swipe functionality for IQAC navigation
    const iqacNav = document.querySelector('.iqac-nav');
    if (iqacNav && window.innerWidth <= 900) { // Only on mobile/tablet
        let startX, startY, endX, endY;
        let isSwiping = false;

        iqacNav.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
            startY = e.touches[0].clientY;
            isSwiping = true;
        });

        iqacNav.addEventListener('touchmove', (e) => {
            if (!isSwiping) return;
            endX = e.touches[0].clientX;
            endY = e.touches[0].clientY;
        });

        iqacNav.addEventListener('touchend', (e) => {
            if (!isSwiping) return;
            isSwiping = false;

            const deltaX = startX - endX;
            const deltaY = startY - endY;

            // Check if horizontal swipe is dominant
            if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > 50) {
                const scrollAmount = iqacNav.offsetWidth * 0.8; // Scroll by 80% of container width

                if (deltaX > 0) {
                    // Swipe left - scroll right
                    iqacNav.scrollBy({ left: scrollAmount, behavior: 'smooth' });
                } else {
                    // Swipe right - scroll left
                    iqacNav.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
                }
            }
        });
    }

    // School detail tabs functionality
    const tabLinks = document.querySelectorAll('.nav-pills-custom .nav-link');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            // Remove active class from all links and panes
            tabLinks.forEach(l => l.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('show', 'active'));

            // Add active class to clicked link
            this.classList.add('active');

            // Show corresponding tab pane
            const targetId = this.getAttribute('href');
            const targetPane = document.querySelector(targetId);
            if (targetPane) {
                targetPane.classList.add('show', 'active');
            }
        });
    });

    // Scroll buttons for nav pills
    const scrollLeftBtn = document.querySelector('.scroll-button.left');
    const scrollRightBtn = document.querySelector('.scroll-button.right');
    const navContainer = document.querySelector('.nav-container');

    if (scrollLeftBtn && scrollRightBtn && navContainer) {
        scrollLeftBtn.addEventListener('click', () => {
            navContainer.scrollBy({ left: -200, behavior: 'smooth' });
        });

        scrollRightBtn.addEventListener('click', () => {
            navContainer.scrollBy({ left: 200, behavior: 'smooth' });
        });
    }

    // Accordion functionality for programmes offered
    const accordionHeaders = document.querySelectorAll('.accordion-item-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const item = header.parentElement;
            const descriptionWrapper = item.querySelector('.accordion-item-description-wrapper');
            const icon = header.querySelector('.accordion-item-header-icon');

            // Toggle open class
            item.classList.toggle('open');

            // Toggle description visibility
            if (item.classList.contains('open')) {
                descriptionWrapper.style.maxHeight = descriptionWrapper.scrollHeight + 'px';
                if (icon) icon.style.transform = 'rotate(180deg)';
            } else {
                descriptionWrapper.style.maxHeight = '0';
                if (icon) icon.style.transform = 'rotate(0deg)';
            }
        });
    });
});
