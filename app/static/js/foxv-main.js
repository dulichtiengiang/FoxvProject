$(document).ready(function() {
/////////////////////////////////////////////
////////// HEADER ///////////////////////////
/////////////////////////////////////////////

const btnAccount = document.querySelector('.foxv-header-tools__tools-item.-account');
const btnClose = document.querySelector('.foxv-modal__close');
const sidePanel = document.querySelector('.foxv-modal__sidepanel');
const backDrop = document.querySelector('.foxv-modal__backdrop');
const body = document.querySelector('body');

btnAccount.addEventListener('click', function() {
    backDrop.classList.add('active');
    sidePanel.classList.add('active');
    body.classList.add('o-hidden');
});
btnClose.addEventListener('click', function(){
    sidePanel.classList.remove('active');
    backDrop.classList.remove('active');
    body.classList.remove('o-hidden');
});
/////////////////////////////////////////////
////////// TAB SHOW /////////////////////////
/////////////////////////////////////////////
    $(".nav-tabs a").click(function(){
        $(this).tab('show');
    });
    $('.nav-tabs a').on('shown.bs.tab', function(event){
        var x = $(event.target).text();         // active tab
        var y = $(event.relatedTarget).text();  // previous tab
        $(".act span").text(x);
        $(".prev span").text(y);
    });

// for Moblie
// $('footer div').css({height': variable + 'px'}
    var slide_Width = $('.slider-container').width();
    var slide_Height = slide_Width/2.35;
    $('.slider-container').css({'height': slide_Height});

    var autoLoad = setInterval(function() {
        dot_Active = dot_Current + 1;
        controlDot();
        controlSlide();
    },3000);
    var dot_Current = $('.foxv-slick-dots .dot.active').index() + 1;
    var dot_Active = 1;
    //var dot_Current = $('.foxv-slick-dots .dot:nth-child('+()+')');
    var slide_Current;
    var slide_Active;
    var modeAction;
    function controlDot() {
        if (dot_Active > dot_Current) {
            $('.foxv-slick-dots .dot').removeClass('active');
            if (dot_Active < 5) {
                $('.foxv-slick-dots .dot:nth-child('+(dot_Active)+')').addClass('active');
            } else {
                $('.foxv-slick-dots .dot:first-child').addClass('active');
            }
        } else if (dot_Active < dot_Current) { //dot_Active < dot_Current
            $('.foxv-slick-dots .dot').removeClass('active');
            if (dot_Active > 0) {
                $('.foxv-slick-dots .dot:nth-child('+(dot_Active)+')').addClass('active');
                //dot_Current = dot_Active;
            } else {
                $('.foxv-slick-dots .dot:last-child').addClass('active');
            }
        }
    }
    function controlSlide() {
                slide_Current   = $('.slide-block .slide:nth-child('+(dot_Current)+')');
                slide_Active    = $('.slide-block .slide:nth-child('+(dot_Active)+')');
        if (dot_Active > dot_Current) {
            if (dot_Active < 5) { // click Dot = 1 -> 4
                slide_Current.addClass('disappear-left').one('webkitAnimationEnd', function(){ //after
                    $('.disappear-left').removeClass('disappear-left').removeClass('active');
                });
                slide_Active.addClass('active').addClass('appear-left').one('webkitAnimationEnd', function(){
                    $('.appear-left').removeClass('appear-left');
                });
                dot_Current = dot_Active;
            } else { // click Dot = 5
                slide_Current.addClass('disappear-left').one('webkitAnimationEnd',function(){
                    $('.disappear-left').removeClass('disappear-left').removeClass('active');
                });
                $('.slide-block .slide:first-child').addClass('active').addClass('appear-left').one('webkitAnimationEnd',function(){
                    $('.appear-left').removeClass('appear-left');
                });
                dot_Current = 1;
            }
        // PREV
        } else if (dot_Active < dot_Current) {
            if (dot_Active > 0) { // click Dot = 1 -> 4
                slide_Current.addClass('disappear-right').one('webkitAnimationEnd', function(){ //after
                    $('.disappear-right').removeClass('disappear-right').removeClass('active');
                });
                slide_Active.addClass('active').addClass('appear-right').one('webkitAnimationEnd', function(){
                    $('.appear-right').removeClass('appear-right');
                });
                dot_Current = dot_Active;
            } else { // click Dot = 0
                slide_Current.addClass('disappear-right').one('webkitAnimationEnd',function(){
                    $('.disappear-right').removeClass('disappear-right').removeClass('active');
                });
                $('.slide-block .slide:last-child').addClass('active').addClass('appear-right').one('webkitAnimationEnd',function(){
                    $('.appear-right').removeClass('appear-right');
                });
                dot_Current = 4;
            }
        }
    }
    // handling Button
    $('#btn-next').on('click', function(event) {
        clearInterval(autoLoad);
        dot_Active = dot_Current + 1;
        controlDot();
        controlSlide();

    });
    $('#btn-prev').on('click', function(event) {
        clearInterval(autoLoad);
        dot_Active = dot_Current - 1;
        controlDot();
        controlSlide();
    });
    $('.foxv-slick-dots li').on('click', function() {
        clearInterval(autoLoad);
        dot_Active=$(this).index()+1;
        controlDot();
        controlSlide();
    });

    // handling Dot
    // handling Slide
});


