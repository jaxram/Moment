$(".menu").on("click", function () {
  $(".modal").fadeIn();
  $(".menues").show();
  $(".menu").hide();
});

$(".menues").on("click", function () {
  $(".modal").fadeOut();
  $(".menu").show();
  $(".menues").hide();
});

$(".back").on("click", function () {
  window.location.replace("/search");
});

var getprofile = 1;

$.ajax({
  url: "/t22",
  type: "GET",
  data: {getprofile},
  success:function(data){
    var parsedData = JSON.parse(data);
    var designation;
    console.log(parsedData);
    $(".user-name").text(parsedData[0].name);
    $(".user-img").attr("src", "/"+parsedData[0].profilepic);
    $(".user-img").show();
    if(parsedData[0].designation == 0) {
      designation = "Professor";
    }
    else if(parsedData[0].designation == 1) {
      designation = "Associate Professor";
    }

    else if(parsedData[0].designation == 2) {
      designation = "Assistant Professor";
    }

    else if(parsedData[0].designation == 3) {
      designation = "Student";
    }

    else if(parsedData[0].designation == 4) {
      designation = "Others";
    }

    $(".user-designation").text(designation);

    if(parsedData[1] == "fstatus:0") {
      $(".follow").html("<i class='fa fa-plus' aria-hidden='true'></i> Follow");
    }
    else {
      $(".follow").html('<i class="fa fa-check" aria-hidden="true"></i> Following');
    }

    var follow = 0;

    $(".follow").on("click", function () {
      console.log($(".follow").text());
      if($(".follow").text() == " Follow") {
        $(".follow").html('<i class="fa fa-check" aria-hidden="true"></i> Following');
        follow = 1;
      }
      else if($(".follow").text() == " Following") {
        $(".follow").html("<i class='fa fa-plus' aria-hidden='true'></i> Follow");
        follow = 0;
      }

      $.ajax({
        url: "/t23",
        type: "POST",
        data: {follow,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
        success:function(data){
          console.log("Success");
      }
    });

    });

}
});
