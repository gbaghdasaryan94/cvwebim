
 $(window).load(function () {


$('.header-content a[href*="#"]').on('click', function(e) {
  e.preventDefault()

  $('html, body').animate(
    {
      scrollTop: $($(this).attr('href')).offset().top,
    },
    900,
    'swing'
  )
})

$('.footer a[href*="#"]').on('click', function(e) {
  e.preventDefault()

  $('html, body').animate(
    {
      scrollTop: $($(this).attr('href')).offset().top,
    },
    900,
    'swing'
  )
})

$("#section-project h4").waypoint(function(){
    $({blurRadius: 5}).animate({blurRadius: 0}, {
    duration: 1200,
    easing: 'swing',
    step: function() {
        $(".blue-item span").css({
            "-webkit-filter": "blur("+this.blurRadius+"px)",
            "filter": "blur("+this.blurRadius+"px)"
        });
    }
});
var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(' ');
$(".blue-item span").each(function() {
    var tcount = $(this).data("count");
    $(this).animateNumber({ number: tcount,
        easing: 'easeInQuad',
        numberStep: comma_separator_number_step},
        2400);
}); this.destroy();
}, {
        offset: '40%'
})



$("#accordion").on("click", ".accordion-header", function() {
       if( $(this).hasClass("active")){
         $(this).next().slideUp();
          $(this).removeClass("active");
         
       } else {
         $(".accordion-header").next().slideUp();
          $(".accordion-header").removeClass("active");
    $(this).addClass("active").next().slideDown();
       }          
   
     });

$('#accordion>.accordion-content').not(':first-of-type').hide();
 
  


  $('.vCarousel').slick({
    vertical: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    verticalSwiping: true,
    arrows: true,
    prevArrow: $(".fa-angle-up"),
    nextArrow: $(".fa-angle-down"),
  });





$('.slider-for').slick({
  slidesToShow: 1,
  infinite: false,
  slidesToScroll: 1,
  arrows: false,
  autoplay: true,
  // fade: true,
  asNavFor: '.slider-nav'
});


$('.slider-nav').slick({
  slidesToShow: 3,
  infinite: true,
  infinite: false,
  slidesToScroll: 1,
  asNavFor: '.slider-for',
  dots: false,
  centerMode: true,
  centerPadding: '60px',
  focusOnSelect: true,
  arrows:false,
  responsive: [
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        // infinite: true,
        
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        // infinite: true,
        arrows:true,
        prevArrow: $(".arrow-left"),
        nextArrow: $(".arrow-right"),
      }
    }
  ]
});



var d = new Date();
    var year = d.getFullYear();
    $(".year").html(year);
    


  


  $(window).scroll(function(){
    if ( $(this).scrollTop() > $(this).height() ){
      $('.top').addClass('active');
    } else {
      $('.top').removeClass('active');
    }
  });
  $('.top').click(function(){
    $('html,body').stop().animate({scrollTop: 0},'slow','swing');
  });

$("#edit").click(function(e) {
  e.preventDefault();
  $("input").removeAttr( "disabled" );
  $('#submit').removeAttr( "hidden" );
  $('#cancel').removeAttr( "hidden" );
  $('#edit').attr( "hidden","hidden" );
  

});

$("#cancel").click(function(e) {
  e.preventDefault();
  $("input").attr( "disabled", "disabled" );
  $('#submit').attr( "hidden", "hidden"  );
  $('#cancel').attr( "hidden", "hidden"  );
  $('#edit').removeAttr( "hidden" );

 
  
});



$('#avatar').bind('change', function () {
  var filename = $("#avatar").val();
  if (/^\s*$/.test(filename)) {
    $(".file-upload").removeClass('active');
    $("#noFile").text("No file chosen..."); 
  }
  else {
    $(".file-upload").addClass('active');
    $("#noFile").text(filename.replace("C:\\fakepath\\", "")); 
  }
});

  });