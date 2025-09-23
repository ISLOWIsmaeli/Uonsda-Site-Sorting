// copyright.js
// Dynamically insert the current year into any element with class 'copyright-year'
document.addEventListener('DOMContentLoaded', function() {
    var yearElements = document.getElementsByClassName('copyright-year');
    var year = new Date().getFullYear();
    for (var i = 0; i < yearElements.length; i++) {
        yearElements[i].textContent = year;
    }
});
