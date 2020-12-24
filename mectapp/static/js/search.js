let name;
let search = 1;
let type1;
/*setInterval(function () {
name = $(".search-input").val();
if(name.length >= 1) {
  $(".search-label").hide();
}
else {
  $(".search-label").show();
}
}, 300);*/

$(".search-input").on("input", function () {
  name = $(".search-input").val();
  $(".recent-searches").show();
  if(name.length >= 1) {
    $(".search-label").hide();
  }
  else {
    $(".search-label").show();
  }
  $.ajax({
				url: "/t7",
				type: "POST",
				data: {search,name,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
				success:function(data){
          var parsedData = JSON.parse(data);
          $(".search-result").remove();
            for(let i=0; i<parsedData.length; i++) {
              if(parsedData[i].name) {
                console.log(parsedData);
                $(".search-results").append(`
                <div class='search-result userredirect' id='` + parsedData[i].userid + `'>
                  <img src="` + parsedData[i].profilepic + `" class='search-img'>
                  <h1 class='search-name'>`+ parsedData[i].name + `</h1>
                </div>`
                );
              }
              else if(parsedData[i].groupname) {
                console.log(parsedData);
                $(".search-results").append(`
                <div class='search-result groupredirect' id='` + parsedData[i].groupid + `'>
                  <img src="` + parsedData[i].groupdp + `" class='search-img'>
                  <h1 class='search-name'>`+ parsedData[i].groupname + `</h1>
                </div>`
                );
              }
          }

          if(name.length < 1) {
            $(".search-result").remove();
          }

          $(".userredirect").on("click", function () {
            var id = $(this).attr('id');
            type1 = "user";
            console.log("User");
            console.log(id);


            $.ajax({
              url: "/t8",
              type: "POST",
              data: {type1,id,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
              success:function(data){
                window.location.replace("search/"+type1+"/"+id);
            }
          });

          });

          $(".groupredirect").on("click", function () {
            var id = $(this).attr('id');
            var type1 = "group";
            console.log("Group");
            console.log(id);


            $.ajax({
              url: "/t9",
              type: "POST",
              data: {type1,id,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
              success:function(data){
                window.location.replace("search/"+type1+"/"+id);
            }
          });

          });
			}
    });
});

$(".notifications").on("click", function () {
  window.location.replace("notifications");
});

$(".home").on("click", function () {
  window.location.replace("home");
});
$(".settings").on("click", function () {
  window.location.replace("settings");
});
