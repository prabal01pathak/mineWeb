const menuIcon = document.querySelector('.menu-icon');
const headerLinks = document.querySelector('.header-links');

menuIcon.addEventListener('click', () => {
    headerLinks.classList.toggle('nav-active');
    menuIcon.classList.toggle('icon-opacity');

});