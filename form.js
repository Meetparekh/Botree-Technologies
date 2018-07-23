$(document).ready(function(){
    $('.form-control').click(function(){
        $(this).css('background-color','#eee')
    })


    //disable button

    $("button[type=submit]").attr("disabled","disabled")

    $ ("input").change(function(){

        //validate here

        var validate=true
        var el=$('#emailinput').val()
        var pl=$('#pswinput').val()

        if(el==0 || pl==0) validate=false

        // if form is validate then enable button

        if(validate)$('button[type=submit]').removeAttr("disabled")

        // Trigger change the function once to check if form is validate on page load

        $('input:first').trigger("change")

    })
});

