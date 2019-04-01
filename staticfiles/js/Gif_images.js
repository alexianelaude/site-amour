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
      } else {
          $img.attr('src', $imgAlt).attr('data-alt', $img.data('alt'));
          $img.attr('src', $img.data('alt')).attr('data-alt', $imgSrc);
      }

    });