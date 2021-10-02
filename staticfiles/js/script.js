function navSlide() {
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".nav-links");
    const navLinks = document.querySelectorAll(".nav-links li");

    burger.addEventListener("click", () => {
        //Toggle Nav
        nav.classList.toggle("nav-active");

        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ""
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            }
        });
        //Burger Animation
        burger.classList.toggle("toggle");
    });

}
navSlide();
const navBar = document.querySelector('nav');
window.addEventListener("scroll", () => {
    let value = window.scrollY;
    if (value !== 0) {
        navBar.classList.add('bgColor');
    } else {
        navBar.classList.remove('bgColor');
    }
});

function checkMe(){
    var checkit = document.getElementById("checkbox");
    var signIn = document.getElementById("buttons");
    if(checkit.checked==true){
        signIn.style.display="flex";
    }
    else{
        signIn.style.display ="none";
    }
}