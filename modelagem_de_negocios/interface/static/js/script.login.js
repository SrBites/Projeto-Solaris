$(document).ready(function(){
    $(".cliente").hide();
    $(".empresa").hide();
    if ($( '.cliente' ).is(":hidden") && $('.empresa').is(":hidden")) {
        if($(window).width() <= 1600 && $(window).height() <= 900){
            $("#log").css("margin-bottom", "200px");
        }
        if($(window).width() <= 1366 && $(window).height() <= 768){
            $("#log").css("margin-bottom", "50px");
        }
        if($(window).width() <= 1920 && $(window).height() <= 1080){
            $("#log").css("margin-bottom", "500px");
        }
    }
    $("#logincliente").click(function(){
        if ($('.empresa').is(":hidden")) {
            $(".cliente").show();
            $("#log").css("margin-bottom", "50px");
            $(".footer").css("bottom", "0");
            $(".footer").css("width", "100%");
            if($(window).width() <= 1920 && $(window).height() <= 1080){
                $(".cliente").css("margin-bottom", "100px");
            }
        } else {
            $(".empresa").hide();
            $(".cliente").show();
            $("#log").css("margin-bottom", "50px");
            $(".footer").css("bottom", "0");
            $(".footer").css("width", "100%");
            if($(window).width() <= 1920 && $(window).height() <= 1080){
                $(".cliente").css("margin-bottom", "100px");
            }

        }
    });
    $("#loginempresa").click(function(){
        if ($('.cliente').is(":hidden")) {
            $(".empresa").show();
            $("#log").css("margin-bottom", "50px");
            $(".footer").css("bottom", "0");
            $(".footer").css("width", "100%");
            if($(window).width() <= 1920 && $(window).height() <= 1080){
                $(".empresa").css("margin-bottom", "100px");
            }
        } else {
            $(".cliente").hide();
            $(".empresa").show();
            $("#log").css("margin-bottom", "50px");
            $(".footer").css("bottom", "0");
            $(".footer").css("width", "100%");
            if($(window).width() <= 1920 && $(window).height() <= 1080){
                $(".empresa").css("margin-bottom", "100px");
            }
        }
    });
});