
$('#post-form').submit(function(e){
    e.preventDefault()
    console.log("form submitted")
    
    $.ajax({
        url:'posts',
        method: 'post',
        data: $(this).serialize(),
        success: function(serverResponse){
            // console.log("received this from server: ", serverResponse)
            $('.posts').html(serverResponse)
        }
    })
    $(this).trigger('reset')
});
