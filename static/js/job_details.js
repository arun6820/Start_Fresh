$(document).ready(function() {

    var applyButton = document.getElementById("apply-button");
    var applyUrl = applyButton.getAttribute("data-job-url"); 

    applyButton.addEventListener("click", function() {
        window.location.href = applyUrl;
    });
});