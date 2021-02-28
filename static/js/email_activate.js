$(document).ready(function() {
    $('form').on('submit' , function(event){
        $.ajax({
            data : {
                email_activation = $('#email_activation').val(),
            },
            type: 'POST',
            url: '/Register',
        });
        event.preventDefault();
    });
});