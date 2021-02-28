$(document).ready(function() {
    $('form').on('submit' , function(event){
        $.ajax({
            data : {
                email: $('#email').val(),
                email_check: $('#email_check').val(),
                password: $('#password').val(),
                password_check: $('#password_check').val(),
                last_name: $('#last_name').val(),
                first_name: $('#first_name').val(),
                gender: $('#gender').val(),
                // email_activation = $('#email_activation').val(),
            },
            type: 'POST',
            url: '/Register'
        })
        event.preventDefault();
    });

    



});