document.body.onkeydown = function( e ) {
    var keys = {
        //37: 'left',
        //39: 'right',
        //40: 'down',
        //38: 'rotate',
        //32: 'drop'
        81: 'left',
        68: 'right',
        83: 'down',
        90: 'rotate',
        88: 'drop'
    };
    if ( typeof keys[ e.keyCode ] != 'undefined' ) {
        keyPress( keys[ e.keyCode ] );
        render();
    }
};
