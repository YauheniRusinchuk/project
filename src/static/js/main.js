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
                $('.login_container').slideDown();
            },
            error: function(err) {
                $('.email_register').css('border', '1px solid red');
            }
        })
    })

})
