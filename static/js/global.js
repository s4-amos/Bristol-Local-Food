// ===== GLOBAL JAVASCRIPT =====
// Handles dark mode toggle, hamburger menu, and theme persistence.

// Dark mode toggle elements
const themeToggle = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const htmlElement = document.documentElement;

// Hamburger menu elements
const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');

// ----- Hamburger menu toggle -----
if (hamburger) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// ----- Dark mode -----
// Check for saved theme in localStorage
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    htmlElement.setAttribute('data-theme', savedTheme);
    updateIcon(savedTheme);
} else {
    // Default to light theme
    htmlElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    updateIcon('light');
}

// Update the sun/moon icon based on current theme
function updateIcon(theme) {
    if (themeIcon) {
        themeIcon.textContent = theme === 'dark' ? '🌙' : '☀️';
    }
}

// Toggle theme on button click
if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateIcon(newTheme);
    });
}

// Close mobile menu when a link is clicked
if (navLinks) {
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
        });
    });
}