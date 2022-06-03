$(".search").on("click", function () {
  window.location.replace("search");
});

$(".home").on("click", function () {
  window.location.replace("home");
});
$(".settings").on("click", function () {
  window.location.replace("settings");
});

let notificationcount = 1;

let notificationtime = 1;

$.ajax({
      url: "/t33",
      type: "GET",
      data: {notificationcount},
      success:function(data){
        $.ajax({
              url: "/t34",
              type: "GET",
              data: {notificationtime},
              success:function(data){
                var parsedData = JSON.parse(data);
                console.log(parsedData);
                if(parsedData.latest.length > 0) {
                  $(".latest").append('<h2 class="latest-heading">Latest</h2>');
                  for(var i = 0; i < parsedData.latest.length; i++) {
                    if(parsedData.latest[i].type == 'like') {
                      $(".latest").append(
                        `
                      <div class="notification like" id="`+ parsedData.latest[i].id +`">
                        <img src="`+ parsedData.latest[i].dp +`" class="notification-img">
                        <h1 class="notification-msg">`+ parsedData.latest[i].name +` has liked your post in `+ parsedData.latest[i].gname +`</h1>
                      </div>
                      `);
                    }

                    else if(parsedData.latest[i].type == 'comment') {
                      $(".latest").append(
                        `
                      <div class="notification comment" id="`+ parsedData.latest[i].id +`">
                        <img src="`+ parsedData.latest[i].dp +`" class="notification-img">
                        <h1 class="notification-msg">`+ parsedData.latest[i].name +` has commented to your post in `+ parsedData.latest[i].gname +`</h1>
                      </div>
                      `);
                    }

                    else if(parsedData.latest[i].type == 'reply') {
                      $(".latest").append(
                        `
                      <div class="notification reply" id="`+ parsedData.latest[i].id +`">
                        <img src="`+ parsedData.latest[i].dp +`" class="notification-img">
                        <h1 class="notification-msg">`+ parsedData.latest[i].name +` has replied to your post in `+ parsedData.latest[i].gname +`</h1>
                      </div>
                      `);
                    }

                  }
                }

                if(parsedData.earlier.length > 0) {
                  $(".latest").append('<h2 class="latest-heading">Earlier</h2>');
                  for(var i = 0; i < parsedData.earlier.length; i++) {
                    if(parsedData.earlier[i].type == 'like') {
                      $(".latest").append(
                        `
                      <div class="notification like" id="`+ parsedData.earlier[i].id +`">
                        <img src="`+ parsedData.earlier[i].dp +`" class="notification-img">
                        <h1 class="notification-msg">`+ parsedData.earlier[i].name +` has liked your post in `+ parsedData.earlier[i].gname +`</h1>
                      </div>
                      `);
                    }

                    else if(parsedData.earlier[i].type == 'comment') {
                      $(".latest").append(
                        `
                      <div class="notification comment" id="`+ parsedData.earlier[i].id +`">
                        <img src="`+ parsedData.earlier[i].dp +`" class="notification-img">
                        <h1 class="notification-msg">`+ parsedData.earlier[i].name +` has commented to your post in `+ parsedData.earlier[i].gname +`</h1>
                      </div>
                      `);
                    }

                    else if(parsedData.earlier[i].type == 'reply') {
                      $(".latest").append(
                        `
                      <div class="notification reply" id="`+ parsedData.earlier[i].id +`">
                        <img src="`+ parsedData.earlier[i].dp +`" class="notification-img">
                        <h1 class="notification-msg">`+ parsedData.earlier[i].name +` has replied to your post in `+ parsedData.earlier[i].gname +`</h1>
                      </div>
                      `);
                    }

                  }
                }

                $(".notification").on("click", function () {
                  var type = $(this).attr("class");
                  type = type.split(" ");
                  type = type[1];
                  var id = $(this).attr("id");
                  console.log(type);
                  console.log(id);
                  $.ajax({
                    url: "/t35",
                    type: "POST",
                    data: {type,id,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
                    success:function(data){
                      window.location.replace("notifications/"+type+"/"+id);
                    }
                  });
                });

            }
          });
    }
  });
