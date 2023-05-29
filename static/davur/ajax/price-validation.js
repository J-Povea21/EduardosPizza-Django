// We use the jQuery library to make an AJAX request to the create-size view
// when the user submits the form. The AJAX request sends the form data to the
// server and receives a response. If the size was created successfully, the
// user is redirected to the home page. If the price is invalid, an error
// message is displayed to the user.

$(document).ready(function() {
    $('.needs-price-validation-form').on('submit', function(event) {
      event.preventDefault();  // Prevent the default form submission

      // Get the form data
      var formData = $(this).serialize();

      // Send an AJAX request to the create-size view
      $.ajax({
        url: $(this).attr('action'),
        method: 'POST',
        data: formData,
        dataType: 'json',
        success: function(response) {
          // Handle the response from the server
          if (response.success) {
            // If the size was created successfully, redirect to the home page
            window.location.href = response.redirect_to;
          } else {
            // If the price is invalid, display an error message to the user
            $('#error-message').text(response.errors);
          }
        },
        error: function(xhr, status, error) {
          // Handle any errors that occur during the AJAX request
          console.log(error);
          $('#error-message').text('An error occurred. Please try again.');
        }
      });
    });
  });
