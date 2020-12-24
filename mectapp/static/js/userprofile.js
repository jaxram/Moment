let request = 1;
let designation;

$(".back").on("click", function () {
  window.location.replace("/settings");
});

$.ajax({
      url: "/t32",
      type: "GET",
      data: {request},
      success:function(data){
       var parsedData = JSON.parse(data);
       console.log(parsedData);
       $(".user-name").text(parsedData[0].name);
       $(".user-img").attr("src",parsedData[0].profilepic);
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
       $(".designation").text(designation);
       $(".user-mobile").text(parsedData[0].mobile);
    }
  });
