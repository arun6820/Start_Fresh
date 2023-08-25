$(document).ready(function() {


    

    function updateJobResults() {
        var salary_from = $('#from').val();
        var salary_to = $('#to').val();
        var date_filter = $('select[name="date_filter"]').val();
        var employers = $('input[name="employer"]:checked').map(function() {
            return this.id;
        }).get();

        $.ajax({
            type: 'POST',
            url: '/filter_jobs',
            data: {
                salary_from: salary_from,
                salary_to: salary_to,
                date_filter: date_filter,
                employers: employers
            },
            success: function(data) {
                console.log("sucess");
                console.log(data);
                var jobResultsContainer = $('#job-results');
                var jobCards = jobResultsContainer.find('.card');
                jobCards.remove();
                for (var i = 0; i < data.length; i++) {
                    var job = data[i];

                    var jobCard = $('<a href="' + '/job-details?jobId=' + job.jobId + '" class="card-link"></a>');
                    var cardContent = $('<div class="card"></div>');
                
                    cardContent.append('<h2>' + job.jobTitle + '</h2>');
                    cardContent.append('<p class="date">Date: ' + job.date + '</p>');
                    cardContent.append('<p class="salary">Salary: ' + job.currency + ' ' + job.minimumSalary + ' - ' + job.currency + ' ' + job.maximumSalary + '</p>');
                    cardContent.append('<p class="location">Location: ' + job.locationName + '</p>');
                
                    jobCard.append(cardContent);
                    jobResultsContainer.append(jobCard);
                }

            }
        });
    }

    $('#from, #to, select[name="date_filter"], input[name="employer"]').on('change', function() {
        updateJobResults();
    });
});
