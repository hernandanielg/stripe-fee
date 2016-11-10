function animationHover(element, animation){
  element = $(element)
  element.hover(
      function() {
          element.addClass('animated ' + animation)
      },
      function(){
          window.setTimeout( function(){
              element.removeClass('animated ' + animation)
          }, 2000)
      })
}

$(document).ready(function(){
  $('.panel-footer').each(function() {
    animationHover(this, 'tada')
  })
})
