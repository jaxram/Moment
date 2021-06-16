let target = 1;
let loggedin;
let postid;
let userid=[1];
let wholeid=[1];
let z1;

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
    url: "/t47",
    type: "GET",
    data: {target},
    success:function(data){
      console.log("Success");
      var parsedData = JSON.parse(data);
      console.log(parsedData);
      length = parsedData.z1.length;
      console.log('length',length);
      postid = parsedData.z3[0];
        console.log('pid',postid);
	    for (let i=0; i<(parsedData.z1.length); i++) {
        $(".members").append(`
        <div class="member">
          <img src="` + parsedData.z1[i].profilepic + `" class="member-img ` + i + `">
          <button class="member-name">` + parsedData.z1[i].name + `</button>
        </div>`);

      }
      length = parsedData.z2.length;
      for (let j=0; j<(parsedData.z2.length); j++)
      {
        wholeid.push(parsedData.z2[j]);

      }
      for (let j=0; j<(parsedData.z1.length)-1; j++)
      {
        wholeid.push(parsedData.z1[j].userid);

      }
      console.log(wholeid);
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
    $.ajax({
      url: "/t48",
      type: "POST",
      data: {wholeid,postid,userid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
      success:function(){
        console.log("Success");
        console.log(postid);
        console.log(userid);
        console.log(wholeid);
        window.location.replace("home");
    }
  });

  }
  else {
    $.ajax({
  				url: "/t13",
  				type: "POST",
  				data: {wholeid,postid,userid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
  				success:function(){
            console.log("Success");
            console.log(postid);
            console.log(userid);
            console.log(wholeid);
  					window.location.replace("home");
  			}
      });
  }
});
