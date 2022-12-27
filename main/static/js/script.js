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
        $('#update-form').on('click', function() {
            $("#update-customer-form").valid();
        });
    });
});


// Hide help text from UserCreationForm

/* $('.help-block').hide();
 */
// Validation for multiform

/* $(document).ready(function() {
    $("#basic-form").validate({
        errorClass: "error fail-alert",
        validClass: "valid success-alert",
        rules: {
            personnr: {
                 required: '#id_orgnr:blank'
            },
            orgnr: {
                 required: '#id_personnr:blank'
            }
       },

       messages: {
            personnr: {
            required: "Enter a valid swedish person number"
            },
            orgnr: {
                required: "Enter a valid swedish organisation number"
            }
        }
})
    }); */