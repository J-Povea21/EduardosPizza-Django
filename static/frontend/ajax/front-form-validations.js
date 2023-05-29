$(document).ready(function() {
    //Function to validate the form fields
    $('#front-form').submit(function (event) {
        event.preventDefault(); // Prevent the default form submission
       var form = $(this);
       var formData = form.serialize(); // Serialize the form data

       //Send the AJAX request to check if all fields are valid
         $.ajax({
              url: form.attr('action'),
             type: form.attr('method'),
             data: formData,
                success: function(response) {
                // Check if all fields are valid
                if (response.are_invalid) {
                    $('#error-title').text('¡Ups! Parece que hay algunos errores en el formulario:');
                    $('#error-message').html(response.errors.join('<br>'));
                }else{
                    window.location.href = response.redirect_to;
                }
              },
             error: function(response) {
                  $('#error-title').text('¡Ups! Parece que hay un error en el servidor');
                  $('#error-message').text('Por favor, inténtalo de nuevo más tarde');
                }
         });
    });

    //Clean form submission errors when user close the modal
    $('#confirmOrderModal').on('hidden.bs.modal', function () {
        $('#error-title').text('');
        $('#error-message').html('');
    });

});