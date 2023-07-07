$(document).ready(function() {
		$('#signUp-form').submit(function(event) {
			event.preventDefault();
			var form = $(this);
			var url = form.attr('action');
			var data = {
				email: $('#email').val(),
				phone_number: $('#phoneNumber').val(),
				password: $('#pwd').val()
			};
			$.ajax({
				type: 'POST',
				url: '/api/signup/',
				data: data,
				dataType: 'json',
				success: function(response) {
					$('#message').html('<p class="text-success">User registered successfully!</p>');
				},
				error: function(xhr, status, error) {
					$('#message').html('<p class="text-danger">' + xhr.responseJSON.email[0] + '</p>');
				}
			});
		});
	});