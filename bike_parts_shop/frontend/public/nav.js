let lastScrollTop = 0; // Переменная для хранения предыдущей позиции скролла
const navbar = document.querySelector('.navbar'); // Находим navbar

// Событие скролла
window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset || document.documentElement.scrollTop; // Текущая позиция скролла

    if (currentScroll > lastScrollTop && currentScroll > 50) {
        // Скролл вниз
        navbar.classList.add('hidden'); // Добавляем класс для скрытия
    } else {
        // Скролл вверх
        navbar.classList.remove('hidden'); // Убираем класс для показа
    }

    // Обновляем последнюю позицию скролла
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});
//burger
document.querySelector('.burger').addEventListener('click', function () {
    this.classList.toggle('active');

    document.querySelector('.menu-list').classList.toggle('open');

})