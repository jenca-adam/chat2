 function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
} 
$(document).ready(function(){
  $(document).keydown(function(event) {
            if (event.ctrlKey==true && (event.which == '61' || event.which == '107' || event.which == '173' || event.which == '109'  || event.which == '187'  || event.which == '189'  ) ) {
         alert('disabling zooming'); 
    event.preventDefault();
    // 107 Num Key  +
    //109 Num Key  -
    //173 Min Key  hyphen/underscor Hey
    // 61 Plus key  +/=
       }
  });

  $(window).bind('mousewheel DOMMouseScroll', function (event) {
         if (event.ctrlKey == true) {
          	var scale = 'scale(1)';
	document.body.style.webkitTransform =       // Chrome, Opera, Safari
 document.body.style.msTransform =          // IE 9
 document.body.style.transform = scale; 
	location.reload()
       event.preventDefault();
         }
  });
});
