const menuIcon = document.querySelector('.menu-icon');
const headerLinks = document.querySelector('.header-links');
const navBar = () => {
    menuIcon.addEventListener('click', () => {
        headerLinks.style.animation = 'rotate 800ms both alternate';
        menuIcon.classList.toggle('icon-opacity');
        headerLinks.classList.toggle('nav-active');

    });
};
navBar();
