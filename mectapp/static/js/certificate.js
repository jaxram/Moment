let rno;
let sd;
let ed;
let type;
let event_1;
let ndays;
var delay = 2000; 
$(".inbox option:selected").siblings().remove();
$(".inbox").append(`
<option value="Sports">Sports</option>
<option value="Culturals">Culturals</option>
<option value="Academic">Academic</option>
<option value="MOOC">MOOC</option>
<option value="Intern">Intern</option>
`);
$(".back").on("click",function(){
    window.location.replace("/settings");
});
$(".next").on("click", function () {
rno=$(".rno").val();
sd=$(".sdate").val();
ed=$(".edate").val();
type=$(".inbox").val();
event_1=$(".event").val();
ndays=$(".days").val();
eloc=$(".location").val();
if(rno=='' || sd==''|| ed=='' || type=='' || event_1=='' || ndays=='' || eloc=='')
{
  $(".miss").css("display", "block");
}
else{
  $.ajax({
    url: "/t49",
    type: "POST",
    data: {rno,sd,ed,type,event_1,ndays,eloc,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
    success:function(data){
      console.log("Success");
      $(".miss").css("display", "none");
      $(".added").css("display", "block");
      setTimeout(function(){ window.location.replace("/settings"); }, delay);
    }
});
}
});

