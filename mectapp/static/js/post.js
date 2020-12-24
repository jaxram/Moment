let postdata = 1;
let posttext;
let postimg;
let userid;
let groupname;

$.ajax({
      url: "/t10",
      type: "GET",
      data: {postdata},
      success:function(data){
        console.log("Success");
        var parsedData = JSON.parse(data);
        userid = parsedData[0].userid;
        var name = parsedData[0].name;
        var dp = parsedData[0].profilepic;
        console.log(name);
        console.log(dp);
        $(".user-img").attr("src",dp);
        $(".user-img").show();
        $(".user-name").text(name);
        for(let i=1; i<parsedData.length; i++) {
          $("select").append(`<option>` + parsedData[i].groupname +`</option>`);
        }
    }
  });

$(".add-img").on("click", function () {
  $("input").click();
});

$(".add-tag").on("click", function () {
  window.location.replace("tag");
});

$(".back").on("click", function () {
  window.location.replace("home");
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('.post-img').attr('src', e.target.result);
      postimg = (e.target.result.replace(/^data:image\/(png|jpg);base64,/, ""));
    }

    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("input").change(function() {
  readURL(this);
});

setInterval(function () {
  var vals = $("textarea").val();
  if(vals.length >= 1) {
    $(".post").css("color", "#ff914d");
    $(".add-post").css("color", "green");
  }
  else {
    $(".post").css("color", "#727272");
    $(".add-post").css("color", "#727272");
  }
}, 300)

//Send post datas to the server

$(".add-post").on("click", function () {
  posttext = $(".post-input").val();
  groupname = $("select").val();
  $.ajax({
				url: "/t11",
				type: "POST",
				data: {posttext,postimg,userid,groupname,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
				success:function(){
          if(groupname=='Tutor Ward')
          {
            window.location.replace("target1");
          }
          else
          {
            window.location.replace("target");
          }
          
			}
    });
})

$(".post").on("click", function () {
  posttext = $(".post-input").val();
  groupname = $("select").val();
  $.ajax({
				url: "/t11",
				type: "POST",
				data: {posttext,postimg,userid,groupname,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
				success:function(){
          if(groupname=='Tutor Ward')
          {
            window.location.replace("target1");
          }
          else
          {
            window.location.replace("target");
          }
          
					
			}
    });
})
