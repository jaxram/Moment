let target = 1;
let loggedin;
let postid;
let userid=[1];

$.ajax({
      url: "/t31",
      type: "GET",
      data: {target},
      success:function(data){
       loggedin = JSON.parse(data);
       userid.push(loggedin);
    }
  });

$.ajax({
    url: "/t12",
    type: "GET",
    data: {target},
    success:function(data){
      console.log("Success");
      var parsedData = JSON.parse(data);
      console.log(parsedData);
      length = parsedData.z1.length;
      postid = parsedData.z2[0];
	    for (let i=0; i<(parsedData.z1.length)-1; i++) {
        $(".members").append(`
        <div class="member">
          <img src="` + parsedData.z1[i].profilepic + `" class="member-img ` + i + `">
          <button class="member-name">` + parsedData.z1[i].name + `</button>
        </div>`);

      }

      $(".member").on("click", function () {
        var img = $(this).children(".member-img");
        var imgclass = img.attr("class");
        var imgclassarr = imgclass.split(" ");
        var imgsrc = imgclassarr[1];


        if(img.attr("src") != "static/images/tick.png") {
          img.attr("src","static/images/tick.png");
          userid.push(parsedData.z1[imgsrc].userid);
          console.log(userid);
        }
        else {
          img.attr("src",parsedData.z1[imgsrc].profilepic);
          var indexs = userid.indexOf(parsedData.z1[imgsrc].userid);
          userid.splice(indexs, 1);
          console.log(userid);
        }
      });

		}
	});

$(".select").on("click", function () {
  $(".members").fadeIn();
});

$(".all").on("click", function () {
  $(".members").fadeOut();
});

$(".next").on("click", function () {
  var selection = $("input[type='radio']:checked").val();
  if(selection == 'selectall') {
    window.location.replace("home");
  }
  else {
    $.ajax({
  				url: "/t13",
  				type: "POST",
  				data: {postid,userid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
  				success:function(){
            console.log("Success");
            console.log(postid);
            console.log(userid);
  					window.location.replace("home");
  			}
      });
  }
});
