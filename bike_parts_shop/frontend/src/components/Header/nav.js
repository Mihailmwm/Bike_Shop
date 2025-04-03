
document.addEventListener("DOMContentLoaded", function () {
    let lastScrollTop = 0; 
    const navbar = document.querySelector('.navbar'); 

    if (navbar) {
        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset || document.documentElement.scrollTop; 

            if (currentScroll > lastScrollTop && currentScroll > 50) {
                navbar.classList.add('hidden'); 
            } else {
                navbar.classList.remove('hidden'); 
            }

            lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
        });
    } else {
        console.error("Элемент .navbar не найден! Проверь HTML и порядок загрузки скрипта.");
    }
});


