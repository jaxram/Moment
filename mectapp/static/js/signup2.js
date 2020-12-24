let imgdata;
let request2 = 1;

$(".dial").knob({
	'width': 60
	});

	$(window).on("load", function() {
    $(".dial").show();
  });

$(".add-image").on("click", function () {
	$(".file").click();
});

$(".img").on("click", function () {
	$(".file").click();
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('.img').attr('src', e.target.result);
			imgdata = (e.target.result.replace(/^data:image\/(png|jpg);base64,/, ""));
    }

    reader.readAsDataURL(input.files[0]); // convert to base64 string
	$(".add-image").hide();
	$("img").show();
  }
}

$(".file").change(function() {
  readURL(this);
});

$(".next").on("click", function () {
  $.ajax({
				url: "/t4",
				type: "POST",
				data: {request2,imgdata,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
				success:function(){
          console.log("Success");
					window.location.replace("accountcreated");
			}
    });
});
