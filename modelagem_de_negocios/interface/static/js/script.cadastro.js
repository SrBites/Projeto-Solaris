$(document).ready(function(){
    $(".cliente").hide();
    $(".empresa").hide();
    if ($( '.cliente' ).is(":hidden") && $('.empresa').is(":hidden")) {
        if($(window).width() <= 1600 && $(window).height() <= 900){
            $("#cad").css("margin-bottom", "200px");
        }
        if($(window).width() <= 1366 && $(window).height() <= 768){
            $("#cad").css("margin-bottom", "50px");
        }
        if($(window).width() <= 1920 && $(window).height() <= 1080){
            $("#cad").css("margin-bottom", "500px");
        }
    }
    $("#cadastrocliente").click(function(){
        if ($('.empresa').is(":hidden")) {
            $(".cliente").show();
            $("#cad").css("margin-bottom", "50px");
            $(".footer").css("bottom", "0");
            $(".footer").css("width", "100%");
            if($(window).width() <= 1920 && $(window).height() <= 1080){
                $(".cliente").css("margin-bottom", "200px");
            }
        } else {
            $(".empresa").hide();
            $(".cliente").show();
            $("#cad").css("margin-bottom", "50px");
            $(".footer").css("bottom", "0");
            $(".footer").css("width", "100%");

        }
    });
    $("#cadastroempresa").click(function(){
        if ($('.cliente').is(":hidden")) {
            $(".empresa").show();
            $("#cad").css("margin-bottom", "50px");
            $(".footer").css("bottom", "0");
            $(".footer").css("width", "100%");
            if($(window).width() <= 1920 && $(window).height() <= 1080){
                $("#cad").css("margin-bottom", "1px");
            }
        } else {
            $(".cliente").hide();
            $(".empresa").show();
            $("#cad").css("margin-bottom", "50px");
            $(".footer").css("bottom", "0");
            $(".footer").css("width", "100%");
            if($(window).width() <= 1920 && $(window).height() <= 1080){
                $("#cad").css("margin-bottom", "1px");
            }
        }
    });
});