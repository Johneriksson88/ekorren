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
        $('#update-form').on('click', function () {
            $("#update-customer-form").valid();
        });
    });
});

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



$(document).ready(function () {

    // On button click, get value
    // of input control Show alert
    // message box

});

// Hide help text from UserCreationForm

/* $('.help-block').hide();
 */