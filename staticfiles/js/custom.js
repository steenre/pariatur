jQuery( document ).ready(function( $ ) {

	"use strict";

        // Page loading animation

        // $(window).on('load',function() {
        $("#preloader").animate({
            'opacity': '0'
        }, 600, function(){
            setTimeout(function(){
                $("#preloader").css("visibility", "hidden").fadeOut();
            }, 300);
        });
        // });

        $(".django-messages").animate(3000, function(){
            setTimeout(function(){
                $('.django-messages').css('tranform', 'translate(0,-150%)').fadeOut()
            }, 4000);
        });

        $("#tools-btn").click(
            function(){
                // $("#tools-btn").css('background', 'red')
                $(".dash-sidebar").toggleClass("on");
            }
        )

        $('.nav-btn').click(
            function(){
                $('.nav-btn').toggleClass('active')
                $('nav').toggleClass('active')  
            }
        )
        // $(window).scroll(function() {
        //   var scroll = $(window).scrollTop();
        //   var box = $('.header-text').height();
        //   var header = $('header').height();

        //   if (scroll >= box - header) {
        //     $("header").addClass("background-header");
        //   } else {
        //     $("header").removeClass("background-header");
        //   }
        // });

});