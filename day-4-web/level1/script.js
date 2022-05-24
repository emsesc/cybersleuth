$('#password').focusin(function(){
  $('form').addClass('up')
});
$('#password').focusout(function(){
  $('form').removeClass('up')
});

// Panda Eye move
$(document).on( "mousemove", function( event ) {
  var dw = $(document).width() / 15;
  var dh = $(document).height() / 15;
  var x = event.pageX/ dw;
  var y = event.pageY/ dh;
  $('.eye-ball').css({
    width : x,
    height : y
  });
});

// validation


$('.btn').click(function(event){
  event.preventDefault()
  if ($('#username').val() == "guest123" && $('#password').val() == "123$") {
    $(".form-group").remove()
    $("h1").text("Welcome, Default User!")
    $("h3").html("You are signed in as guest123. The code you are looking for is <b>h1dd3n_in_pl4in_s1ght</b>")
  } else {
      $('form').addClass('wrong-entry');
    setTimeout(function(){ 
       $('form').removeClass('wrong-entry');
     },3000 );
  }

});