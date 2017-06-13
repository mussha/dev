// function showflashMessage(message) {
// 	var template = "<div class='container container-alert-flash'>" +
// 	"<div class='col-sm-3 col-sm-offset-8'>" + 
// 	"<div class='alert alert-success alert-dismissible' role='alert'>" + 
// 	"<button type='button' class='close' data-dismiss='alert' aria-label='Close'>" +
// 	"<span aria-hidden='true'>&times;</span></button>" + 
// 	+ message + "</div></div></div>"
// 	$("body").append(template);
// 	setTimeout(function(){
// 		$("container-alert-flash").fadeIn();	
// 	}, 1)
// }


function showFlashMessage(message) {
	// var template = "{% include 'alert.html' with message='" + message + "' %}"
	var template = "<div class='container container-alert-flash'>" + 
	"<div class='col-sm-3 col-sm-offset-8'> " + 
	"<div class='alert alert-success alert-dismissible' role='alert'>" + 
	"<button type='button' class='close' data-dismiss='alert' aria-label='Close'>" +
	"<span aria-hidden='true'>&times;</span></button>" 
	+ message + "</div></div></div>"
	$("body").append(template);
	$(".container-alert-flash").fadeIn();
	setTimeout(function(){ 
		$(".container-alert-flash").fadeOut();
	}, 1800);

}

$(function() {

  // Because  element with 'position: fixed' overlay the content,
  // for pushing content down need to create element which will be do it
  // and need to find natural width of collapsed menu.
  // By default navbar has 'display: none', so it will show 'height = 0'.
  // We need to detect height of element without showing it to user. 
  // Hide the element in another way, then take height, and finaly hide it as it was.
  // Everythin it at loading page and just one time.
  
  var nav = $('.navbar-collapse');

  nav.css('visibility', 'hidden')
     .css('position', 'fixed')
     .css('display', 'block');
  
  var height = nav.height();

  nav.css('display', '')
     .css('position', '')
     .css('visibility', '');

  $('.navbar-toggle').click(function () {

      var preExpand = $('.navbar-pre-expand');

      if (this.attributes['aria-expanded'].value == 'false') {
      
        if (!preExpand.hasClass('expanded')) {
          preExpand.css('height', height + 50).addClass('expanded');
        }
        
      } else {
      
        if (preExpand.hasClass('expanded')) {
          preExpand.css('height', '50px').removeClass('expanded');
        }
        
      }
   
  });

});
