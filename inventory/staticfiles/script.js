document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".faq-question").forEach(button => {
        button.addEventListener("click", function() {
            this.nextElementSibling.classList.toggle("show");
            if (this.nextElementSibling.style.display === "block") {
                this.nextElementSibling.style.display = "none";
            } else {
                this.nextElementSibling.style.display = "block";
            }
        });
    });
});