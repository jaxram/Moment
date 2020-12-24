
let email;
let pwd;
let cpwd;
let request;

 $(".dial").knob({
	'width': 60
	});

  $(window).on("load", function() {
    $(".dial").show();
  });

$(".next").on("click", function () {
  email = $(".mail").val();
  pwd = $(".password").val();
  cpwd = $(".confirm-password").val();
  request = 1;
  if(pwd == cpwd) {
    $.ajax({
  				url: "/t1",
  				type: "POST",
  				data: {email,pwd,cpwd,request,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
  				success:function(data){
            var parsedData = JSON.parse(data);
            console.log(parsedData);
            if(parsedData == "email exists") {
              $(".error").text("Email already exists!");
              $(".error").fadeIn();
              $(".main").css("marginTop","0px");
            }
            else {
              window.location.replace("signup1");
            }
  			}
      });
  }
  else {
    $(".error").text("Passwords did not match!")
    $(".error").fadeIn();
    $(".main").css("marginTop","0px");
  }
});
