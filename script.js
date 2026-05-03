document.addEventListener('DOMContentLoaded', () => {
    const navItems = document.querySelectorAll('.nav-item');
    const tabContents = document.querySelectorAll('.tab-content');

    // Navigation Tab Switching Logic
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active class from all nav items and hide all content
            navItems.forEach(nav => nav.classList.remove('active'));
            tabContents.forEach(tab => {
                tab.classList.remove('active');
            });

            // Add active class to clicked nav item
            item.classList.add('active');

            // Show target content
            const targetId = item.getAttribute('data-target');
            const targetContent = document.getElementById(targetId);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });

    // Simple interaction for baby movement counter
    const recordMovementBtns = document.querySelectorAll('.btn-primary');
    recordMovementBtns.forEach(btn => {
        if(btn.innerHTML.includes('Catat Gerakan')) {
            btn.addEventListener('click', () => {
                const counterDisplay = btn.previousElementSibling.querySelector('h1');
                let count = parseInt(counterDisplay.innerText);
                counterDisplay.innerText = count + 1;
                
                // Add a small animation effect
                counterDisplay.style.transform = 'scale(1.2)';
                setTimeout(() => {
                    counterDisplay.style.transform = 'scale(1)';
                }, 200);
            });
        }
    });

    // Symptom logger interaction
    const symptomItems = document.querySelectorAll('.symptom-item');
    symptomItems.forEach(item => {
        item.addEventListener('click', () => {
            item.classList.toggle('active');
            
            // Toggle check badge
            let checkBadge = item.querySelector('.check-badge');
            if (item.classList.contains('active')) {
                if (!checkBadge) {
                    checkBadge = document.createElement('div');
                    checkBadge.className = 'check-badge';
                    checkBadge.innerHTML = '<i class="fa-solid fa-check"></i>';
                    item.appendChild(checkBadge);
                }
            } else {
                if (checkBadge) {
                    checkBadge.remove();
                }
            }
        });
    });
});
