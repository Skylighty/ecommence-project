const navSilde = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    // Toggle Navigation

    // when we click on burger we want nav to get class nav-active
    burger.addEventListener('click', () => {
        // Toggle now
        nav.classList.toggle('nav-active');

        //Animate the links
        navLinks.forEach((link, index) => {
            if (link.style.animation){
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            }
        });
        burger.classList.toggle('toggle');
    });
    
}

navSilde();