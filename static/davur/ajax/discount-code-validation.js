// In this file we define the validation of the discount and the coupon code

$(document).ready(function() {
    $('.coupon-form').on('submit', function(event) {
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
          // Here we validate if the coupon code exists and if the discount is valid
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
