(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $(document).on('click', 'a.page-scroll', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 51
    });

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });

    // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    })

    // Initialize and Configure Scroll Reveal Animation
    window.sr = ScrollReveal();
    sr.reveal('.sr-icons', {
        duration: 600,
        scale: 0.3,
        distance: '0px'
    }, 200);
    sr.reveal('.sr-button', {
        duration: 1000,
        delay: 200
    });
    sr.reveal('.sr-contact', {
        duration: 600,
        scale: 0.3,
        distance: '0px'
    }, 300);

    // Initialize and Configure Magnific Popup Lightbox Plugin
    /*$('.popup-gallery').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
        }
    });*/



    var getGif = function() {
      var gif = [];
      $('img').each(function() {
        var data = $(this).data('alt');
        gif.push(data);
      });
      return gif;
    }
    var gif = getGif();
    // Preload all the GIF.
    var image = [];

    $.each(gif, function(index) {
      image[index]     = new Image();
      image[index].src = gif[index];
    });

    $('figure').on('mouseover', function() {

      var $this   = $(this),
              $index  = $this.index(),
              $img    = $this.children('img'),
              $imgSrc = $img.attr('src'),
              $imgAlt = $img.attr('data-alt'),
              $imgExt = $imgAlt.split('.');

      if($imgExt[1] === 'gif') {
          $img.attr('src', $img.data('alt')).attr('data-alt', $imgSrc);
      } //else {
      //    $img.attr('src', $imgAlt).attr('data-alt', $img.data('alt'));
      //    $img.attr('src', $img.data('alt')).attr('data-alt', $imgSrc);
      //}

    });
})(jQuery); // End of use strict
