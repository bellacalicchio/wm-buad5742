/**
 * Raymond A. Mason School of Business - AI Proficiency Course
 * Basic JavaScript for interactive elements
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log('AI Proficiency Course website loaded successfully.');

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add visual feedback to download buttons
    const downloadBtns = document.querySelectorAll('.btn-secondary');
    downloadBtns.forEach(btn => {
        if (btn.innerText.includes('Download')) {
            btn.addEventListener('click', () => {
                console.log('Download initiated for:', btn.innerText);
                // In a real app, this would trigger the actual file download
            });
        }
    });
});
