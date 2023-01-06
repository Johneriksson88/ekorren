// Create date for copyright footer

$("#copyright").text(new Date().getFullYear());

// Remove messages after 5 seconds

setTimeout(function () {
    if ($('.alert').length > 0) {
        $('.alert').slideUp('100');
    }
}, 5000)




$(document).ready(function () {

    // Toggle Edit customer information in user panel

    $("#user-info-edit").hide();
    $("#toggle-form").click(function ($e) {
        $e.preventDefault();
        $("#user-info-edit").toggle();
        $("#user-info").toggle();
    });

    $("#update-info-back").click(function ($e) {
        $e.preventDefault();
        $("#user-info").toggle();
        $("#user-info-edit").toggle();
    })
    
    // Put placeholders in and style UserCreationForm since i use the django model

    var form_fields = document.getElementsByTagName('input')
    form_fields[1].placeholder = 'Username..';
    form_fields[2].placeholder = 'Enter password...';
    form_fields[3].placeholder = 'Re-enter Password...';

    for (var field in form_fields) {
      form_fields[field].className += ' form-control'
    }

    
    
});


/* $(document).ready(function () {

    $("#user-info-edit").hide();
    $("#toggle-form").click(function ($e) {
        $e.preventDefault();
        $("#user-info-edit").toggle();
        $("#user-info").toggle();
        $('#update-form').on('click', function () {
            $("#update-customer-form").valid();
        });
    });
}); */

// Modal confirmation of order

$(document).ready(function () {
    $('#order-modal-btn').on("click", function () {
        $('#order-modal').modal("show");
        var storageUnit = $("#id_storage_unit option:selected").text();
        var startDate = $("#id_start_date").val();
        $('#order-modal-body').html(
            "<b>Storage unit: </b>" + storageUnit + "<br><b>Start date:</b> " + startDate
        )
    });

    $('.close-modal').on("click", function () {
        $('#order-modal').modal("hide");
    })
});

