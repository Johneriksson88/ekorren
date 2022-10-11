const toggleButton = document.getElementsByClassName("toggle-btn")[0]
const navBarLinks = document.getElementsByClassName("navbar-links")[0]


// Create date for copyright footer

$("#copyright").text(new Date().getFullYear());


toggleButton.addEventListener("click", () => {
    navBarLinks.classList.toggle("active")
})