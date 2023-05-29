// Here we're going to check if the coupon code is valid or not
// If it's valid, we're going to update the total price
// If it's not valid, we're going to show an error message

// We're going to use jQuery to make an AJAX request to the server

$(document).ready(function () {
    var $couponForm = $('#id-code');
    $couponForm.on('change', function () {
        var $form = $(this);
        var $formData = $form.serialize();
        var $endpoint = $form.attr('action');
        var $method = $form.attr('method');

        $.ajax({
            method: $method,
            url: $endpoint,
            data: $formData,
            success: function (response) {
                if(response.valid){

                }
            }),
            error: handleFormError
        })
    }
}