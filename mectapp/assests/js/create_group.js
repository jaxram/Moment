let groupimgdata;
let groupname;
let create_group = 1;

$(".add-image").on("click", function () {
  $("#file").click();
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('.img').attr('src', e.target.result);
      groupimgdata = (e.target.result.replace(/^data:image\/(png|jpg);base64,/, ""));
    }

    reader.readAsDataURL(input.files[0]); // convert to base64 string
	$(".add-image").hide();
	$(".img").show();
  }
}

$("#file").change(function() {
  readURL(this);
});

$(".close").on("click", function () {
  window.location.replace("settings");
});

$(".create").on("click", function () {
  groupname = $(".add-name").val();
  $.ajax({
    url: "/t6",
    type: "POST",
    data: {groupimgdata,groupname,create_group,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
    success:function(data){
      console.log("Success");
  }
});
});
