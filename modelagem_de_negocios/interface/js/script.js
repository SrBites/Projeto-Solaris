$(document).ready(function(){
    $(".cliente").hide();
    $(".empresa").hide();
    if ($( '.cliente' ).is(":hidden") && $('.empresa').is(":hidden")) {
        document.getElementById("footer").style.marginTop = "200px";
    } else {
        document.getElementById("footer").style.marginTop = "0";
    }
    $("#cadastrocliente").click(function(){
        if ($('.empresa').is(":hidden")) {
            $(".cliente").show();
        } else {
            $(".empresa").hide();
            $(".cliente").show();
        }
    });
    $("#cadastroempresa").click(function(){
        if ($('.cliente').is(":hidden")) {
            $(".empresa").show();
        } else {
            $(".cliente").hide();
            $(".empresa").show();
        }
    });
});