
$(".home").on("click", function () {
  window.location.replace("home");
});

$(".notifications").on("click", function () {
  window.location.replace("notifications");
});

$(".search").on("click", function () {
  window.location.replace("search");
});

$(".settings").on("click", function () {
  window.location.replace("settings");
});
$(".account-text").on("click", function () {
  window.location.replace("edit");
});
$(".user-profile").on("click", function () {
  window.location.replace("up");
});

$(".about").on("click", function () {
  window.location.replace("about");
});
$(".tutor").on("click",function(){
  window.location.replace("tutor");
});
$(".certificate").on("click",function(){
  window.location.replace("certificate");
});
$(".data").on("click",function(){
  $.ajax({
    url: "/data",
    type: "GET",
    success:function(){
      console.log("success");
    }
  });
});
let dark;
let request = 1;
let request_1=1;
$.ajax({
  url: "/t46",
  type: "GET",
  data: {request_1},
  success:function(data){
    var parsedData=JSON.parse(data);
    console.log(parsedData);
    if(parsedData>2 && parsedData<13)
    {
      $(".tut").hide("fast");
      $(".tutor").hide("fast");
    }
    else if(parsedData==1)
    {
      $(".tut").hide("fast");
      $(".tutor").hide("fast");
      $(".data").css("display", "block");
    }

  }
});

$.ajax({
  url: "/t28",
  type: "GET",
  data: {request},
  success:function(data){
    var parsedData = JSON.parse(data);
    console.log(parsedData);
    dark = parsedData[0].dark;
    if(dark == 0) {
      $(".dark-mode").append(`<button class="group-symbol"><i class="fa fa-moon-o" aria-hidden="true"></i></button>
      <button class="group-text">Dark Mode</button>`);
    }
    else if(dark == 1) {
      $(".dark-mode").append(`<button class="group-symbol"><i class="fa fa-sun-o" aria-hidden="true"></i></button>
      <button class="group-text">Light Mode</button>`);
    }
   
  }
 
});


$(".dark-mode").on("click", function() {
  if(dark == 0) {
    dark = 1;
    $(this).children(".group-text").text("Light Mode");
    $(this).children(".group-symbol").html('<i class="fa fa-sun-o" aria-hidden="true"></i>');
  }
  else if(dark == 1) {
    dark = 0;
    $(this).children(".group-text").text("Dark Mode");
    $(this).children(".group-symbol").html('<i class="fa fa-moon-o" aria-hidden="true"></i>');
  }

  $.ajax({
    url: "/t29",
    type: "GET",
    data: {dark},
    success:function(data){
      console.log(data);
      location.reload();
    }
  });


});

let logout = 1;

$(".log-out").on("click", function () {
  $.ajax({
        url: "/t27",
        type: "GET",
        data: {logout},
        success:function(data){
          console.log(data);
          if(data == '"success"') {
            window.location.replace("index1");
          }
          }
    });
});
