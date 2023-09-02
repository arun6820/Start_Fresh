
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get data from input fields
        const looking = document.getElementById("looking").value;
        const where = document.getElementById("where").value;
        const salaryFrom = document.getElementById("salary_from").value;
        const salaryTo = document.getElementById("salary_to").value;
        const jobTypes = Array.from(document.querySelectorAll('input[name="jobtype"]:checked')).map(checkbox => checkbox.value);
        const otherTypes = Array.from(document.querySelectorAll('input[name="others"]:checked')).map(checkbox => checkbox.value);
        console.log(jobTypes);

        window.location.href = `/advanced-search_page?looking=${looking}&where=${where}&salaryFrom=${salaryFrom}&salaryTo=${salaryTo}&jobTypes=${JSON.stringify(jobTypes)}&otherTypes=${JSON.stringify(otherTypes)}`;

        // Create an object with the gathered data
        const searchData = {
            looking: looking,
            where: where,
            salary_from: salaryFrom,
            salary_to: salaryTo,
            jobtype: jobTypes,
            others: otherTypes
        };

        console.log(searchData);

    });
});
