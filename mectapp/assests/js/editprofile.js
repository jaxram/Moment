let request1 = 1;
let email;
let name;
let mobilenumber;
let department;
let typeofaccount;
let designation;
$(".password").on("click", function () {
  window.location.replace("cpass");
});



 $(".dial").knob({
	'width': 60
	});

  $(window).on("load", function() {
    $(".dial").show();
  });

$(".dp").on("click", function () {
  name = $(".name").val();
  mobilenumber = $(".mobilenumber").val();
if (name=='' && mobilenumber==''){
  window.location.replace("editprofdp");
}
else
{
  $.ajax({
    url: "/t30",
    type: "POST",
    data: {name,mobilenumber,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
    success:function(data){
      console.log("Success");

      if(data == "mobile number already exists") {
        $(".error").text("Mobile Number already exists!");
        $(".error").fadeIn();
        $(".name").css("marginTop","20px");
      }
      else {
        window.location.replace("editprofdp");
      }

  }
});
}
});


$(".next").on("click", function () {

  name = $(".name").val();
  mobilenumber = $(".mobilenumber").val();

	if (name=='' && mobilenumber==''){
    window.location.replace("accountcreated");
  }
  else
  {
    $.ajax({
      url: "/t30",
      type: "POST",
      data: {name,mobilenumber,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
      success:function(data){
        console.log("Success");

        if(data == "mobile number already exists") {
          $(".error").text("Mobile Number already exists!");
          $(".error").fadeIn();
          $(".name").css("marginTop","20px");
        }
        else {
          window.location.replace("accountcreated");
        }

    }
  });
  }
  });
