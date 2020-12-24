$(".back").on("click", function () {
  window.location.replace("edit");
});

var nextCount = 1;

$(".next").on("click", function () {
  if(nextCount == 1) {
    var currentpassword = $(".currentpassword").val();
    $.ajax({
          url: "/t42",
          type: "POST",
          data: {currentpassword, csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
          success:function(data){
           if(data=="Success") {
             $(".main").hide();
             $(".error").hide();
             $(".changepassword").fadeIn();
             nextCount++;
           }
           else if(data=="Error") {
             $(".error").fadeIn();
           }
        }
      });
  }
  else if(nextCount == 2) {
    var newpassword = $(".newpassword").val();
    var confirmpassword = $(".confirmpassword").val();
    if(newpassword == confirmpassword) {
      $(".error").hide();
      $.ajax({
            url: "/t43",
            type: "POST",
            data: {newpassword, csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
            success:function(data){
              window.location.replace("accountcreated");
          }
        });
    }
    else {
      $(".error").text("Passwords Don't Match")
      $(".error").fadeIn();
    }
  }
});
