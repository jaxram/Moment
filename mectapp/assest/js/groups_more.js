let groups = 1;

$.ajax({
      url: "/t14",
      type: "GET",
      data: {groups},
      success:function(data){
       var parsedData = JSON.parse(data);
       console.log(parsedData);
       for(let i=0; i<parsedData.length; i++) {
        $(".groups").append(`
          <div class="group" id="` + parsedData[i].groupid + `">
            <img src="` + parsedData[i].groupdp + `" class="group-img">
            <button class="group-name group-name1">` + parsedData[i].groupname + `</button>
          </div>
        `);

       }

       $(".group").on("click", function() {
         var groupid = $(this).attr("id");
         window.location.replace("search/group/"+ groupid +"");
       });

    }
  });

$(".close").on("click", function () {
  window.location.replace("home");
});
