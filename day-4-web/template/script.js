// This is the JavaScript code that determines whether or not that inputted passwords and usernames are correct.

$('.btn').click(function(event){
  // This code executes everytime the .btn class is clicked!
  event.preventDefault()
  if ($('#username').val() == "guest123" && $('#password').val() == "123$") {
    // If the username and password are correct, we will remove the form and change the text.
    $(".form-group").remove()
    $("h1").text("Welcome!")
    $("h3").html("You are signed in.")
  } else {
    // If the username and password are not correct, we will change the text to tell the user that it is incorrect.
    $("h3").html("Incorrect Credentials.")
  }

});