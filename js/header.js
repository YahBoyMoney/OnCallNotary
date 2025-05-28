// Initialize header functionality when DOM is fully loaded
function initHeader() {
    // Elements
    const header = document.querySelector('.header');
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');
    const overlay = document.querySelector('.mobile-menu-overlay');
    
    // Close all dropdowns
    function closeAllDropdowns() {
        document.querySelectorAll('.has-dropdown').forEach(dropdown => {
            dropdown.classList.remove('active');
        });
    }
    
    // Toggle mobile menu
    function toggleMobileMenu() {
        const isActive = mobileMenuToggle.classList.toggle('active');
        mainNav.classList.toggle('active', isActive);
        
        if (overlay) {
            overlay.classList.toggle('active', isActive);
        }
        
        // Prevent scrolling when menu is open
        document.body.classList.toggle('menu-open', isActive);
        
        // Close all dropdowns when closing mobile menu
        if (!isActive) {
            closeAllDropdowns();
        }
    }
    
    // Scroll event for header
    window.addEventListener('scroll', function() {
        header.classList.toggle('scrolled', window.scrollY > 50);
    });
    
    // Mobile menu toggle
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', toggleMobileMenu);
    }
    
    // Handle dropdown toggles on mobile
    document.querySelectorAll('.has-dropdown > a').forEach(dropdownToggle => {
        dropdownToggle.addEventListener('click', function(e) {
            if (window.innerWidth <= 992) {
                e.preventDefault();
                const parent = this.parentElement;
                const isActive = parent.classList.contains('active');
                
                // Close all other dropdowns
                document.querySelectorAll('.has-dropdown').forEach(d => {
                    if (d !== parent) d.classList.remove('active');
                });
                
                // Toggle current dropdown
                parent.classList.toggle('active', !isActive);
            }
        });
    });
    
    // Close menu when clicking on overlay
    if (overlay) {
        overlay.addEventListener('click', function() {
            mobileMenuToggle.classList.remove('active');
            mainNav.classList.remove('active');
            this.classList.remove('active');
            document.body.classList.remove('menu-open');
            closeAllDropdowns();
        });
    }
    
    // Close menu when clicking on a link (for mobile)
    document.querySelectorAll('.main-nav a:not(.has-dropdown > a)').forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth <= 992) {
                toggleMobileMenu();
                closeAllDropdowns();
            }
        });
    });
    
    // Close dropdowns when clicking outside (for desktop)
    document.addEventListener('click', function(e) {
        if (window.innerWidth > 992) {
            const isClickInside = header.contains(e.target);
            if (!isClickInside) {
                closeAllDropdowns();
            }
        }
    });
    
    // Handle hover for desktop dropdowns
    if (window.innerWidth > 992) {
        document.querySelectorAll('.has-dropdown').forEach(dropdown => {
            dropdown.addEventListener('mouseenter', function() {
                closeAllDropdowns();
                this.classList.add('active');
            });
            
            dropdown.addEventListener('mouseleave', function() {
                this.classList.remove('active');
            });
        });
    }
    
    // Resize event
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            if (window.innerWidth > 992) {
                mobileMenuToggle.classList.remove('active');
                mainNav.classList.remove('active');
                if (overlay) overlay.classList.remove('active');
                document.body.classList.remove('menu-open');
                closeAllDropdowns();
            }
        }, 250);
    });
    
    // Close dropdowns when pressing Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeAllDropdowns();
        }
    });
}

// Initialize with a small delay to ensure all elements are loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeader);
} else {
    // DOMContentLoaded has already fired, initialize immediately
    setTimeout(initHeader, 100);
}
