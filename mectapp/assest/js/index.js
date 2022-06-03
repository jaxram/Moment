let login = 1;
let email;
let password;
let a;
$(window).on("load", function() {
	setTimeout(function () {
	$(".loading").hide();
	$(".main").fadeIn(800);
}, 3000);
});

$(".signup").on("click", function () {
	window.location.replace("signup");
});

$(".login").on("click", function () {
	email = $(".email").val();
	password = $(".password").val();
	$.ajax({
				url: "/t5",
				type: "POST",
				data: {login,email,password,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
				success:function(data){
          console.log("Success");
					a=data;
					if(a=='Success'){
						window.location.replace("home");
					}
					else
					{
						$(".error").slideDown();
					}
			}
    });
});
