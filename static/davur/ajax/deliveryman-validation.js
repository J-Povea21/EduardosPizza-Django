  $(document).ready(function() {
      $('.deliveryman-form').submit(function(event) {
        event.preventDefault(); // Prevent the default form submission

        var form = $(this);
        var formData = form.serialize(); // Serialize the form data

        // Send the AJAX request to check if cedula is valid
        $.ajax({
          url: form.attr('action'),
          type: form.attr('method'),
          data: formData,
          success: function(response) {
            // Check if coupon code is available
            if (response.exists) {
              // Show an error message in the modal
              $('#error-message').text(response.errors);
            } else {
              // Submit the form if coupon code is valid
              window.location.href = 'deliverymen';
            }
          },
          error: function(xhr, status, error) {
            // Handle error if the AJAX request fails
            console.error(xhr.responseText);
          }
        });
      });
    });