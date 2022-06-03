let request1 = 1;
let email;
let name;
let mobilenumber;
let department;
let typeofaccount;
let designation;

$.ajax({
      url: "/t2",
      type: "GET",
      data: {request1},
      success:function(data){
       email = data;
    }
  });

 $(".dial").knob({
	'width': 60
	});

  $(window).on("load", function() {
    $(".dial").show();
  });

$(".typeofaccount").on("change", function () {
  if($(this).val() == 'Staff') {
    $(".designation option:selected").siblings().remove();
    $(".designation").append(`
    <option value="Professor">Professor</option>
    <option value="Associate Professor">Associate Professor</option>
    <option value="Assistant Professor">Assistant Professor</option>
    `);
  }
  else {
    $(".designation").val("Student");
    $(".designation option:selected").siblings().remove();
  }
});

$(".next").on("click", function () {

  name = $(".name").val();
  mobilenumber = $(".mobilenumber").val();
  typeofaccount = $(".typeofaccount").val();
  designation = $(".designation").val();

  if(typeofaccount == "Staff") {
    typeofaccount = 0;
  }
  else {
    typeofaccount = 1;
  }

  if(designation == "Professor") {
    designation = 0;
  }

  else if(designation == "Associate Professor") {
    designation = 1;
  }

  else if(designation == "Assistant Professor") {
    designation = 2;
  }

  else if(designation == "Student") {
    designation = 3;
  }

  else {
    designation = 4;
  }

  console.log(typeofaccount);
  console.log(designation);

	$.ajax({
    url: "/t3",
    type: "POST",
    data: {email,name,mobilenumber,typeofaccount,designation,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
    success:function(data){
      console.log("Success");
      var parsedData = JSON.parse(data);
      if(parsedData == "mobile number already exists") {
        $(".error").text("Mobile Number already exists!");
        $(".error").fadeIn();
        $(".name").css("marginTop","20px");
      }
      else {
        window.location.replace("signup2");
      }

  }
});
});
