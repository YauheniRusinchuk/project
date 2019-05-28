$(function(){

    $('.btn_login').on('click', (e)=>{
        e.preventDefault();
        $('.login_container').slideToggle();
    })

    $('.register_form').on('submit', (e)=>{
        e.preventDefault();
        console.log("SUBMIT")
        $.ajax({

            url: $(this).attr('action'),
            type: 'POST',
            data: {
                username    : $('.username').val(),
                email       : $('.email_register').val(),
                password    : $('.password_register').val(),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(res) {
                console.log("GOOD");
            },
            error: function(err) {
                console.log("ERROR");
            }
        })
    })

})
