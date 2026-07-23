// Sticky Navbar

window.addEventListener("scroll",function(){

    let navbar=document.querySelector(".custom-navbar");

    if(window.scrollY>40){

        navbar.classList.add("scrolled");

    }else{

        navbar.classList.remove("scrolled");

    }

});
const dropdowns=document.querySelectorAll(".mega-dropdown");

dropdowns.forEach(function(item){

    item.addEventListener("mouseenter",function(){

        let menu=this.querySelector(".dropdown-menu");

        menu.classList.add("show");

    });

    item.addEventListener("mouseleave",function(){

        let menu=this.querySelector(".dropdown-menu");

        menu.classList.remove("show");

    });

});