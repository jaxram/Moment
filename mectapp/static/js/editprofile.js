let dummy=1;
$.ajax({
  url: "/t50",
  type: "GET",
  data:{dummy},
  success:function(data){
    console.log(data);
    if(data>=1 && data<13)
    {
      $(".sdetails").hide("fast");
    }
  }
});
let request1 = 1;
let email;
let name;
let mobilenumber;
let department;
let typeofaccount;
let designation;
$(".password").on("click", function () {
  window.location.replace("cpass");
});

let box=[];
let box1=[];
let box2=[]
let s1;
let s2;
let s3;
  $(function() {
    $(".multiselect").multiselect();
    console.log("success")
});
jQuery.fn.multiselect = function() {
    $(this).each(function() {
        var checkboxes = $(this).find("input:checkbox");
        checkboxes.each(function() {
            var checkbox = $(this);
            // Highlight pre-selected checkboxes
            if (checkbox.prop("checked"))
              
                checkbox.parent().addClass("multiselect-on");
 
            // Highlight checkboxes that the user selects
            checkbox.click(function() {
                if (checkbox.prop("checked"))
                {
                    checkbox.parent().addClass("multiselect-on");
                    s1=checkbox.val()
                    box.push(s1)
                    console.log(box)
               
                }
                    
                else
                    {
                      checkbox.parent().removeClass("multiselect-on");
                    box.splice(box.indexOf(checkbox.val()),1)
                    console.log(box)
                    }
            });
        });
    });
};
$(function() {
  $(".multiselect1").multiselect1();
  console.log("success")
});
jQuery.fn.multiselect1 = function() {
  $(this).each(function() {
      var checkboxes = $(this).find("input:checkbox");
      checkboxes.each(function() {
          var checkbox = $(this);
          // Highlight pre-selected checkboxes
          if (checkbox.prop("checked"))
            
              checkbox.parent().addClass("multiselect-on");

          // Highlight checkboxes that the user selects
          checkbox.click(function() {
              if (checkbox.prop("checked"))
              {
                
                  checkbox.parent().addClass("multiselect-on");
                  s2=checkbox.val()
                  box1.push(s2)
                  console.log(box1)
             
              }
                  
              else
                  {
                    checkbox.parent().removeClass("multiselect-on");
                  box1.splice(box1.indexOf(checkbox.val()),1)
                  console.log(box1 )
                  }
          });
      });
  });
};
$(function() {
  $(".multiselect2").multiselect2();
  console.log("success")
});
jQuery.fn.multiselect2 = function() {
  $(this).each(function() {
      var checkboxes = $(this).find("input:checkbox");
      checkboxes.each(function() {
          var checkbox = $(this);
          // Highlight pre-selected checkboxes
          if (checkbox.prop("checked"))
            
              checkbox.parent().addClass("multiselect-on");

          // Highlight checkboxes that the user selects
          checkbox.click(function() {
              if (checkbox.prop("checked"))
              {
                 
                  checkbox.parent().addClass("multiselect-on");
                  s3=checkbox.val()
                  box2.push(s3)
                  console.log(box2)
             
              }
                  
              else
                  {
                    checkbox.parent().removeClass("multiselect-on");
                  box2.splice(box2.indexOf(checkbox.val()),1)
                  console.log(box2 )
                  }
          });
      });
  });
};
let gender;
$(".gender").on("change", function () {
gender=$(".gender").val();
console.log(gender);
});
let degree;
$(".degree").on("change", function () {
  degree=$(".degree").val();
  console.log(degree);
  });
let admission;
$(".admission").on("change", function () {
  admission=$(".admission").val();
  console.log(admission);
  });
let community;
$(".community").on("change", function () {
  community=$(".community").val();
  console.log(community);
  });
let foccudes;
$(".occu-des").on("change", function () {
  foccudes=$(".occu-des").val();
  console.log(foccudes);
  });
let moccudes;
$(".moccu-des").on("change", function () {
  moccudes=$(".moccu-des").val();
  console.log(moccudes);
  });
let schoolloc;
$(".school-loc").on("change", function () {
  schoolloc=$(".school-loc").val();
  console.log(schoolloc);
  });
let schooltype;
$(".school-type").on("change", function () {
  schooltype=$(".school-type").val();
  console.log(schooltype);
  });
let mediumstudy;
$(".medium-study").on("change", function () {
  mediumstudy=$(".medium-study").val();
  console.log(mediumstudy);
  });
let aftersslc;
$(".aftersslc").on("change", function () {
  aftersslc=$(".aftersslc").val();
  if(aftersslc=="12th")
  {
    $(".hsc").css("display","block");
  }
  else if(aftersslc=="diploma")
  {
    $(".diploma").css("display","block");
    $(".hsc").css("display","none");
  }
  else
  {
    $(".diploma").css("display","none");
    $(".hsc").css("display","none");
  }
  console.log(aftersslc);
  });
let hscschoollocation;
$(".school-loch").on("change", function () {
  hscschoollocation=$(".school-loch").val();
  console.log(hscschoollocation);
  });
let hscschooltype;
$(".school-typeh").on("change", function () {
  hscschooltype=$(".school-typeh").val();
  console.log(hscschooltype);
  });
let hscmediumstudy;
$(".medium-studyh").on("change", function () {
  hscmediumstudy=$(".medium-studyh").val();
  console.log(hscmediumstudy);
 });
let fgraduate;
$(".fg").on("change", function () {
  fgraduate=$(".fg").val();
  console.log(fgraduate);
  });  
  let physicalc;
  $(".physicalc").on("change", function () {
    physicalc=$(".physicalc").val();
    if(physicalc=="yes") 
    $(".physical").css("display","block");
    else if(physicalc=="no")
    $(".physical").css("display","none");
    else
    $(".physical").css("display","none");
    console.log(physicalc);
    });
let eloan;
$(".eloan").on("change", function () {
  eloan=$(".eloan").val();
  if(eloan=="yes")
  $(".eloandetails").css("display","block");
  else if(eloan=="no")
  $(".eloandetails").css("display","none");
  else
  $(".eloandetails").css("display","none");
  console.log(eloan);
  });
let hostel;
$(".hostel").on("change", function () {
  hostel=$(".hostel").val();
  if(hostel=="yes")
  $(".roomdetails").css("display","block");
  else if(hostel=="no")
  $(".roomdetails").css("display","none");
  else
  $(".roomdetails").css("display","none");
  console.log(hostel);
  });
let scholarship;
$(".scholarship").on("change", function () {
  scholarship=$(".scholarship").val();
  if(scholarship=="yes")
  {
    $(".multiselect1").css("display","block");
    $(".amount").css("display","block");
  }
  else if(scholarship=="no")
  {
    $(".multiselect1").css("display","none");
    $(".amount").css("display","none");
  }
  else
  {
  $(".multiselect1").css("display","none");
  $(".amount").css("display","none");
  }
  console.log(scholarship);
  });
let rollno;
let regno;
let religion;
let blood;
let dob;
let address;
let brother;
let sister;
let fname;
let fmob;
let fmail;
let foccu;
let fincome;
let mname;
let mmob;
let mmail;
let moccu;
let mincome;
let sslcname;
let sslcadd;
let sslscyr;
let sslcmarks;
let hscname;
let hscadd;
let hscyr;
let hscmarks;
let maths;
let physics;
let chemistry;
let cutoff;
let dipcgpa;
let dipname;
let overall;
let communityrank;
let disability;
let amount;
let loanamount;
let room;


 $(".dial").knob({
	'width': 60
	});

  $(window).on("load", function() {
    $(".dial").show();
  });

$(".dp").on("click", function () {
  name = $(".name").val();
  mobilenumber = $(".mobilenumber").val();
  rollno=$(".rollno").val();
regno=$(".regno").val();
religion=$(".religion").val();
blood=$(".blood").val();
dob=$(".dob").val();
address=$(".address").val();
brother=$(".brother").val();
sister=$(".sister").val();
fname=$(".fname").val();
fmob=$(".fmob").val();
fmail=$(".fmail").val();
foccu=$(".foccu").val();
fincome=$(".fincome").val();
mname=$(".mname").val();
mmob=$(".mmob").val();
mmail=$(".mmail").val();
moccu=$(".moccu").val();
mincome=$(".mincome").val();
sslcname=$(".sslcname").val();
sslcadd=$(".sslcadd").val();
sslcyr=$(".sslcyr").val();
sslcmarks=$(".sslcmarks").val();
hscname=$(".hscname").val();
hscadd=$(".hscadd").val();
hscyr=$(".hscyr").val();
hscmarks=$(".hscmarks").val();
maths=$(".maths").val();
physics=$(".physics").val();
chemistry=$(".chemistry").val();
cutoff=$(".cutoff").val();
dipcgpa=$(".dipcgpa").val();
dipname=$(".dipname").val();
overall=$(".tor").val();
communityrank=$(".tcr").val();
disability=$(".disability").val();
amount=$(".amount").val();
loanamount=$(".loanamount").val();
room=$(".room").val();
scholarship=$(".scholarship").val();
hostel=$(".hostel").val();
eloan=$(".eloan").val();
physicalc=$(".physicalc").val();
fgraduate=$(".fg").val();
hscmediumstudy=$(".medium-studyh").val();
hscschooltype=$(".school-typeh").val();
hscschoollocation=$(".school-loch").val();
aftersslc=$(".aftersslc").val();
mediumstudy=$(".medium-study").val();
schooltype=$(".school-type").val();
schoolloc=$(".school-loc").val();
foccudes=$(".occu-des").val();
moccudes=$(".moccu-des").val();
community=$(".community").val();
admission=$(".admission").val();
degree=$(".degree").val();
gender=$(".gender").val();
if (name=='' && mobilenumber==''){

  window.location.replace("editprofdp");
}
else
{
  $.ajax({
    url: "/t30",
    type: "POST",
    data: {name,mobilenumber,rollno,regno,gender,religion,blood,dob,address,brother,sister,fname,fmob,fmail,foccu,fincome,mname,mmob,mmail,moccu,mincome,sslcname,sslcadd,
      sslcyr,sslcmarks,hscname,hscadd,hscyr,hscmarks,maths,physics,chemistry,cutoff,dipcgpa,dipname,overall,communityrank,disability,amount,
      loanamount,room,box,box1,box2,degree,admission,community,foccudes,moccudes,schooloc,schooltype,mediumstudy,aftersslc,hscschoollocation,hscschooltype,
      hscmediumstudy,fgraduate,physicalc,eloan,hostel,scholarship,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
    success:function(data){
      console.log("Success");
      console.log(data)

      if(data == "mobile number already exists") {
        $(".error").text("Mobile Number already exists!");
        $(".error").fadeIn();
        $(".name").css("marginTop","20px");
      }
      else {
        window.location.replace("editprofdp");
      }

  }
});
}
});


$(".next").on("click", function () {
  let gender;
  $(".gender").on("change", function () {
  gender=$(".gender").val();
  console.log(gender);
  });
  let degree;
  $(".degree").on("change", function () {
    degree=$(".degree").val();
    console.log(degree);
    });
  let admission;
  $(".admission").on("change", function () {
    admission=$(".admission").val();
    console.log(admission);
    });
  let community;
  $(".community").on("change", function () {
    community=$(".community").val();
    console.log(community);
    });
  let foccudes;
  $(".occu-des").on("change", function () {
    foccudes=$(".occu-des").val();
    console.log(foccudes);
    });
  let moccudes;
  $(".moccu-des").on("change", function () {
    moccudes=$(".moccu-des").val();
    console.log(moccudes);
    });
  let schoolloc;
  $(".school-loc").on("change", function () {
    schoolloc=$(".school-loc").val();
    console.log(schoolloc);
    });
  let schooltype;
  $(".school-type").on("change", function () {
    schooltype=$(".school-type").val();
    console.log(schooltype);
    });
  let mediumstudy;
  $(".medium-study").on("change", function () {
    mediumstudy=$(".medium-study").val();
    console.log(mediumstudy);
    });
  let aftersslc;
  $(".aftersslc").on("change", function () {
    aftersslc=$(".aftersslc").val();
    if(aftersslc=="12th")
    {
      $(".hsc").css("display","block");
    }
    else if(aftersslc=="diploma")
    {
      $(".diploma").css("display","block");
      $(".hsc").css("display","none");
    }
    else
    {
      $(".diploma").css("display","none");
      $(".hsc").css("display","none");
    }
    console.log(aftersslc);
    });
  let hscschoollocation;
  $(".school-loch").on("change", function () {
    hscschoollocation=$(".school-loch").val();
    console.log(hscschoollocation);
    });
  let hscschooltype;
  $(".school-typeh").on("change", function () {
    hscschooltype=$(".school-typeh").val();
    console.log(hscschooltype);
    });
  let hscmediumstudy;
  $(".medium-studyh").on("change", function () {
    hscmediumstudy=$(".medium-studyh").val();
    console.log(hscmediumstudy);
   });
  let fgraduate;
  $(".fg").on("change", function () {
    fgraduate=$(".fg").val();
    console.log(fgraduate);
    });  
    let physicalc;
    $(".physicalc").on("change", function () {
      physicalc=$(".physicalc").val();
      if(physicalc=="yes") 
      $(".physical").css("display","block");
      else if(physicalc=="no")
      $(".physical").css("display","none");
      else
      $(".physical").css("display","none");
      console.log(physicalc);
      });
  let eloan;
  $(".eloan").on("change", function () {
    eloan=$(".eloan").val();
    if(eloan=="yes")
    $(".eloandetails").css("display","block");
    else if(eloan=="no")
    $(".eloandetails").css("display","none");
    else
    $(".eloandetails").css("display","none");
    console.log(eloan);
    });
  let hostel;
  $(".hostel").on("change", function () {
    hostel=$(".hostel").val();
    if(hostel=="yes")
    $(".roomdetails").css("display","block");
    else if(hostel=="no")
    $(".roomdetails").css("display","none");
    else
    $(".roomdetails").css("display","none");
    console.log(hostel);
    });
  let scholarship;
  $(".scholarship").on("change", function () {
    scholarship=$(".scholarship").val();
    if(scholarship=="yes")
    {
      $(".multiselect1").css("display","block");
      $(".amount").css("display","block");
    }
    else if(scholarship=="no")
    {
      $(".multiselect1").css("display","none");
      $(".amount").css("display","none");
    }
    else
    {
    $(".multiselect1").css("display","none");
    $(".amount").css("display","none");
    }
    console.log(scholarship);
    });
  name = $(".name").val();
  mobilenumber = $(".mobilenumber").val();
  rollno=$(".rollno").val();
regno=$(".regno").val();
religion=$(".religion").val();
blood=$(".blood").val();
dob=$(".dob").val();
address=$(".address").val();
brother=$(".brother").val();
sister=$(".sister").val();
fname=$(".fname").val();
fmob=$(".fmob").val();
fmail=$(".fmail").val();
foccu=$(".foccu").val();
fincome=$(".fincome").val();
mname=$(".mname").val();
mmob=$(".mmob").val();
mmail=$(".mmail").val();
moccu=$(".moccu").val();
mincome=$(".mincome").val();
sslcname=$(".sslcname").val();
sslcadd=$(".sslcadd").val();
sslcyr=$(".sslcyr").val();
sslcmarks=$(".sslcmarks").val();
hscname=$(".hscname").val();
hscadd=$(".hscadd").val();
hscyr=$(".hscyr").val();
hscmarks=$(".hscmarks").val();
maths=$(".maths").val();
physics=$(".physics").val();
chemistry=$(".chemistry").val();
cutoff=$(".cutoff").val();
dipcgpa=$(".dipcgpa").val();
dipname=$(".dipname").val();
overall=$(".tor").val();
communityrank=$(".tcr").val();
disability=$(".disability").val();
amount=$(".amount").val();
loanamount=$(".loanamount").val();
room=$(".room").val();
scholarship=$(".scholarship").val();
hostel=$(".hostel").val();
eloan=$(".eloan").val();
physicalc=$(".physicalc").val();
fgraduate=$(".fg").val();
hscmediumstudy=$(".medium-studyh").val();
hscschooltype=$(".school-typeh").val();
hscschoollocation=$(".school-loch").val();
aftersslc=$(".aftersslc").val();
mediumstudy=$(".medium-study").val();
schooltype=$(".school-type").val();
schoolloc=$(".school-loc").val();
foccudes=$(".occu-des").val();
moccudes=$(".moccu-des").val();
community=$(".community").val();
admission=$(".admission").val();
degree=$(".degree").val();
gender=$(".gender").val();
console.log(gender);
	
  {
    $.ajax({
      url: "/t30",
      type: "POST",
      data: {name,mobilenumber,rollno,regno,gender,religion,blood,dob,address,brother,sister,fname,fmob,fmail,foccu,fincome,mname,mmob,mmail,moccu,mincome,sslcname,sslcadd,
        sslcyr,sslcmarks,hscname,hscadd,hscyr,hscmarks,maths,physics,chemistry,cutoff,dipcgpa,dipname,overall,communityrank,disability,amount,
        loanamount,room,box,box1,box2,degree,admission,community,foccudes,moccudes,schoolloc,schooltype,mediumstudy,aftersslc,hscschoollocation,hscschooltype,
        hscmediumstudy,fgraduate,physicalc,eloan,hostel,scholarship,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
      success:function(data){
        console.log("Success");
        console.log(rollno);

        if(data == "mobile number already exists") {
          $(".error").text("Mobile Number already exists!");
          $(".error").fadeIn();
          $(".name").css("marginTop","20px");
        }
        else {
          window.location.replace("accountcreated");
        }

    }
  });
  }
  });


