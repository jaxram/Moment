$(".back").on("click", function () {
  window.location.replace("settings");
});
$(".Done").on("click", function () {
  $.ajax({
    url: "/t45",
    type: "POST",
    data: {userid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
    success:function(){
      console.log("Success");
      console.log(userid);
      if (userid.length==0)
      {
        window.location.replace('settings');
      }
      else{
        window.location.replace('info');
      }
      
  }
});
});
var target=1;
let postid;
let userid=[];

$.ajax({
    url: "/t44",
    type: "GET",
    data: {target},
    success:function(data){
      console.log("Success");
      var parsedData = JSON.parse(data);
      console.log(parsedData);
      length = parsedData.length;
	    for (let i=0; i<(parsedData.length)-1; i++) {
        $(".members").append(`
        <div class="member">
          <img src="` + parsedData[i].profilepic + `" class="member-img ` + i + `">
          <button class="member-name">` + parsedData[i].name + `</button>
        </div>`);

      }
      $(".member").on("click", function () {
        var img = $(this).children(".member-img");
        var imgclass = img.attr("class");
        var imgclassarr = imgclass.split(" ");
        var imgsrc = imgclassarr[1];


        if(img.attr("src") != "static/images/tick.png" && userid.length!=1) {
          img.attr("src","static/images/tick.png");
          userid.push(parsedData[imgsrc].userid);
          console.log(userid);
        }
        else if(img.attr("src") == "static/images/tick.png" && userid.length!=2){
          img.attr("src",parsedData[imgsrc].profilepic);
          var indexs = userid.indexOf(parsedData[imgsrc].userid);
          userid.splice(indexs, 1);
          console.log(userid);
        }
      });

		}
  });
 