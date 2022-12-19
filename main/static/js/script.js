// Create date for copyright footer

$("#copyright").text(new Date().getFullYear());

// Remove messages after 5 seconds

setTimeout(function () {
    if ($('.alert').length > 0) {
        $('.alert').slideUp('100');
    }
}, 5000)


// Toggle Edit customer information in user panel

$(document).ready(function () {

    $("#user-info-edit").hide();
    $("#toggle-form").click(function ($e) {
        $e.preventDefault();
        $("#user-info-edit").toggle();
        $("#user-info").toggle();
    });
});
