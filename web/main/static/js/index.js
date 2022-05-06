/*
=============
Navigation
=============
 */
const menu = document.querySelector(".menu");
const navOpen = document.querySelector(".hamburger");
const navClose = document.querySelector(".close");
const navBar = document.querySelector(".navbar");


navOpen.addEventListener("click", () => {
 
    //menu.classList.add("show");
    menu.style="left:0;";
    document.body.classList.add("show");
    //navBar.classList.add("show");
  
});

navClose.addEventListener("click", () => {
    menu.style="left:-100%;";
    document.body.classList.remove("show");
    navBar.classList.remove("show");
  
});