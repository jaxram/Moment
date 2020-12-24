$(".group1").on("click", function() {

  $.ajax({
    url: "/t40",
    type: "GET",
    data: {userrequest},
    success:function(data){
     console.log(data);
     userid=data;
     console.log(userid)
     window.location.replace("/search/group/7");
  }
});
});

$(".group2").on("click", function() {
  $.ajax({
    url: "/t40",
    type: "GET",
    data: {userrequest},
    success:function(data){
     console.log(data);
     userid=data;
     console.log(userid)
     window.location.replace("/search/group/8");
  }
});
  
});

$(".group3").on("click", function() {
  $.ajax({
    url: "/t40",
    type: "GET",
    data: {userrequest},
    success:function(data){
     console.log(data);
     userid=data;
     console.log(userid)
     window.location.replace("/search/group/10");
  }
});
  
});

$(".group4").on("click", function() {

  $.ajax({
    url: "/t40",
    type: "GET",
    data: {userrequest},
    success:function(data){
     console.log(data);
     userid=data;
     console.log(userid)
     window.location.replace("/search/group/11");
  }
});

});

$(".group5").on("click", function() {
  
  $.ajax({
    url: "/t40",
    type: "GET",
    data: {userrequest},
    success:function(data){
     console.log(data);
     userid=data;
     console.log(userid)
     window.location.replace("/search/group/12");
  }
});

});

$(".group6").on("click", function() {
  
  $.ajax({
    url: "/t40",
    type: "GET",
    data: {userrequest},
    success:function(data){
     console.log(data);
     userid=data;
     console.log(userid)
     window.location.replace("/search/group/13");
  }
});
});
let userrequest = 1;
let postrequest = 1;
let userid;
let startpost=0;
let endpost=10;
let groupname;
let groupnames;
let like;
let likestatus;
let postid;
let totalposts;
let numberofposts;
let postcount=0;
let indexOfTheComment;
let userdp;

let parsedDatas = [];

$.ajax({
      url: "/t15",
      type: "GET",
      data: {userrequest},
      success:function(data){
       console.log(data);
       userid=data;
       console.log(userid)
    }
  });

let request=1;
$(".post").on("click", function () {
  window.location.replace("post");
});

$(".notifications").on("click", function () {
  $.ajax({
    url: "/t40",
    type: "GET",
    data: {request},
    success:function(){
      console.log('sucess')
  }
  });
  window.location.replace("notifications");
});

$(".search").on("click", function () {
  window.location.replace("search");
});

$(".comment-see-all").on("click", function () {
  $(".all-comments").show();
  $(".comment-see-all").hide();
});

$(".comment").on("click", function () {
  $(".all-comments").show();
  $(".comment-see-all").hide();
});

$(".reply").on("click", function () {
  $(".replied").show();
  $(".reply").hide();
  $(".reply-div").show();
});

$(".replied").on("click", function () {
  $(".replied").hide();
  $(".reply").show();
  $(".reply-div").hide();
});

$(".reply-send").on("click", function () {
  $(".replied").hide();
  $(".reply").show();
  $(".reply-div").hide();
});

$(".group7").on("click", function () {
  window.location.replace("groups_more");
  $.ajax({
    url: "/t40",
    type: "GET",
    data: {userrequest},
    success:function(data){
     console.log(data);
     userid=data;
     console.log(userid)
  }
});
});

$(".settings").on("click", function () {
  window.location.replace("settings");
});

$.ajax({
      url: "/t16",
      type: "GET",
      data: {postrequest,userid},
      success:function(data){
       var parsedData = JSON.parse(data);
       console.log(data);
       console.log(parsedData);
       userdp = parsedData.userdp;
       if(parsedData.post.length == 0) {
         $(".no-post").show();
         $(".post-main").hide();
       }
       else {
         totalposts = parsedData.length;
         totalposts = totalposts - 10;
         numberofposts = parsedData.length;
       for(let i = 0; i < parsedData.post.length; i++) {
         postcount++;
         console.log(parsedData.post[i].posttime);
         groupname = parsedData.group[i].groupname;
         groupname = groupname.slice(0,20);
         like = parsedData.post[i].likestatus;
         if(groupname.length >= 20) {
           groupname += ".."
         }
         if(parsedData.post[i].imgdata != 'NULL' && parsedData.post[i].postdata != 'NULL') {
           $(".posts-append").append(`
            <div class="post-image" id="` + parsedData.post[i].postid +`">
             <div class="group-info">
               <img src="`+ parsedData.group[i].groupdp +`" class="group-img-post">
               <h1 class="group-name-post">`+ groupname +`</h1>
               <h2 class="time-post">` + parsedData.post[i].posttime +`</h2>
             </div>
             <div class="delte-post">
              `+(parsedData.post[i].delete == 1 ? '<button class="delete-icon"><i class="fa fa-trash" aria-hidden="true"></i></button>':'')+`
              <div class="delete-confirmation">
                <center><h1 class="delete-text">Do you want to delete this post?</h1></center>
                <center><button class="delete-yes"><i class="fa fa-check" aria-hidden="true"></i></button>
                <button class="delete-no"><i class="fa fa-times" aria-hidden="true"></i></button></center>
              </div>
             </div>
             <div class="post-data">
               <h1 class="post-text-data">` + parsedData.post[i].postdata + `</h1>
               <center><img src="` + parsedData.post[i].imgdata + `" class="post-img"></center>
             </div>
             <div class="post-actions">` +
             (like == 0 ? '<button class="like" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' + parsedData.post[i].likecount +'</span>': '<button class="liked" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' +  parsedData.post[i].likecount  +'</span>')
              +`
               <button class="comment commentbutton"><i class="fa fa-comment" aria-hidden="true"></i></button>
               <button class="reply" id="` + parsedData.post[i].userid + `"><i class="fa fa-reply" aria-hidden="true"></i></button>
               <button class="replied"><i class="fa fa-reply" aria-hidden="true"></i></button>
               <div class="reply-div">
                 <input class="reply-post" placeholder="Add a private reply"/>
                 <button class="reply-send"><i class="fa fa-share" aria-hidden="true"></i></button>
               </div>
               <h2 class="posted-by">Posted by ` + parsedData.user[i].name + `</h2>
             </div>

             `+ (parsedData.post[i].commentdata == 'null' ? '' : '<div class="comment commentdiv"><img class="comment-img" src="'+ parsedData.post[i].dp[0] +'"><h1 class="comment-text">'+ parsedData.post[i].commentdata[0] +'</h1><h2 class="comment-see-all">See all Comments</h2></div>') +`


             <div class="all-comments" id="`+ i +`">
               <div class="individual-comment-input">
                 <img class="comment-img" src="`+ userdp +`">
                 <input type="text" placeholder="Your Comment" class="comment-input"></input>
                 <button class="comment-submit"><i class="fa fa-chevron-circle-right" aria-hidden="true"></i></button>
               </div>
             </div>
           </div>
           `);
         }
         else if(parsedData.post[i].imgdata == 'NULL' && parsedData.post[i].postdata != 'NULL') {

           $(".posts-append").append(`
            <div class="post-text" id="` + parsedData.post[i].postid +`">
             <div class="group-info">
               <img src="` + parsedData.group[i].groupdp + `" class="group-img-post">
               <h1 class="group-name-post">` + groupname + `</h1>
               <h2 class="time-post">` + parsedData.post[i].posttime +`</h2>
             </div>
             <div class="delte-post">
              `+(parsedData.post[i].delete == 1 ? '<button class="delete-icon"><i class="fa fa-trash" aria-hidden="true"></i></button>':'')+`
              <div class="delete-confirmation">
                <center><h1 class="delete-text">Do you want to delete this post?</h1></center>
                <center><button class="delete-yes"><i class="fa fa-check" aria-hidden="true"></i></button>
                <button class="delete-no"><i class="fa fa-times" aria-hidden="true"></i></button></center>
              </div>
             </div>
             <div class="post-data">
               <h1 class="post-text-data">`+ parsedData.post[i].postdata +`</h1>
             </div>
             <div class="post-actions-text">` +
             (like == 0 ? '<button class="like" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' + parsedData.post[i].likecount +'</span>': '<button class="liked" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' +  parsedData.post[i].likecount  +'</span>')
              +`
               <button class="comment commentbutton"><i class="fa fa-comment" aria-hidden="true"></i></button>
               <button class="reply" id="` + parsedData.post[i].userid + `"><i class="fa fa-reply" aria-hidden="true"></i></button>
               <button class="replied"><i class="fa fa-reply" aria-hidden="true"></i></button>
               <div class="reply-div">
                 <input class="reply-post" placeholder="Add a private reply"/>
                 <button class="reply-send"><i class="fa fa-share" aria-hidden="true"></i></button>
               </div>
               <h2 class="posted-by">Posted by `+ parsedData.user[i].name +`</h2>
             </div>

             `+ (parsedData.post[i].commentdata == 'null' ? '' : '<div class="comment commentdiv"><img class="comment-img" src="'+ parsedData.post[i].dp[0] +'"><h1 class="comment-text">'+ parsedData.post[i].commentdata[0] +'</h1><h2 class="comment-see-all">See all Comments</h2></div>') +`

             <div class="all-comments" id="`+ i +`">
               <div class="individual-comment-input">
                 <img class="comment-img" src="`+ userdp +`">
                 <input type="text" placeholder="Your Comment" class="comment-input"></input>
                 <button class="comment-submit"><i class="fa fa-chevron-circle-right" aria-hidden="true"></i></button>
               </div>
             </div>
           </div>
           `);

         }

         else if(parsedData.post[i].imgdata != 'NULL' && parsedData.post[i].postdata == 'NULL') {
           $(".posts-append").append(`
            <div class="post-image-only" id="` + parsedData.post[i].postid +`">
             <div class="group-info group-info-image-only-post">
               <img src="` + parsedData.group[i].groupdp + `" class="group-img-post">
               <h1 class="group-name-post">` + groupname + `</h1>
               <h2 class="time-post">` + parsedData.post[i].posttime +`</h2>
             </div>
             <div class="delte-post">
              `+(parsedData.post[i].delete == 1 ? '<button class="delete-icon"><i class="fa fa-trash" aria-hidden="true"></i></button>':'')+`
              <div class="delete-confirmation">
                <center><h1 class="delete-text">Do you want to delete this post?</h1></center>
                <center><button class="delete-yes"><i class="fa fa-check" aria-hidden="true"></i></button>
                <button class="delete-no"><i class="fa fa-times" aria-hidden="true"></i></button></center>
              </div>
             </div>
             <div class="post-data">
               <center><img src="` + parsedData.post[i].imgdata +`" class="post-img"></center>
             </div>
             <div class="post-actions">` +
             (like == 0 ? '<button class="like" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' + parsedData.post[i].likecount +'</span>': '<button class="liked" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' +  parsedData.post[i].likecount  +'</span>')
              +`
               <button class="comment commentbutton"><i class="fa fa-comment" aria-hidden="true"></i></button>
               <button class="reply" id="` + parsedData.post[i].userid + `"><i class="fa fa-reply" aria-hidden="true"></i></button>
               <button class="replied"><i class="fa fa-reply" aria-hidden="true"></i></button>
               <div class="reply-div">
                 <input class="reply-post" placeholder="Add a private reply"/>
                 <button class="reply-send"><i class="fa fa-share" aria-hidden="true"></i></button>
               </div>
               <h2 class="posted-by">Posted by ` + parsedData.user[i].name + `</h2>
             </div>

             `+ (parsedData.post[i].commentdata == 'null' ? '' : '<div class="comment commentdiv"><img class="comment-img" src="'+ parsedData.post[i].dp[0] +'"><h1 class="comment-text">'+ parsedData.post[i].commentdata[0] +'</h1><h2 class="comment-see-all">See all Comments</h2></div>') +`

             <div class="all-comments" id="`+ i +`">
               <div class="individual-comment-input">
                 <img class="comment-img" src="`+ userdp +`">
                 <input type="text" placeholder="Your Comment" class="comment-input"></input>
                 <button class="comment-submit"><i class="fa fa-chevron-circle-right" aria-hidden="true"></i></button>
               </div>
             </div>
           </div>
           `);
         }


       }
     }

       $(".like").off('click');
       $(".liked").off('click');
       $(".reply").off('click');
       $(".replied").off('click');
       $(".reply-send").off('click');
       $(".comment-see-all").off('click');
       $(".commentbutton").off('click');
       $(".comment-submit").off('click');
       $(".delete-icon").off('click');
       $(".delete-no").off('click');
       $(".delete-yes").off('click');

       $(".delete-icon").on("click", function () {
         $(this).parent().siblings(".post-data").hide();
         $(this).parent().siblings(".post-actions").hide();
         $(this).parent().siblings(".post-actions-text").hide();
         $(this).parent().siblings(".commentdiv").hide();
         $(this).parent().siblings(".all-comments").hide();
         $(this).siblings(".delete-confirmation").show();
       });

       $(".delete-no").on("click", function () {
         $(this).parent().parent().hide();
         $(this).parent().parent().parent().siblings(".post-data").show();
         $(this).parent().parent().parent().siblings(".post-actions").show();
         $(this).parent().parent().parent().siblings(".post-actions-text").show();
         $(this).parent().parent().parent().siblings(".commentdiv").show();
       });

       $(".delete-yes").on("click", function () {
         var postid = $(this).parent().parent().parent().parent().attr("id");
         $(this).parent().parent().parent().parent().fadeOut();
         var deletepost = 1;
         $.ajax({
               url: "/t41",
               type: "POST",
               data: {deletepost,postid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
               success:function(data){
                console.log("Success");
             }
           });
       });

       $(".like").on("click", function () {
         var post = $(this).parent().parent();
         postid = post.attr("id");
         var likecount = $(this).siblings(".like-count").text();
         likecount = parseInt(likecount);
         var clickchecklike = $(this).attr("id");
         clickchecklike = parseInt(clickchecklike);
         console.log(clickchecklike);
         if(clickchecklike == 0) {
           likestatus = 1;
           $(this).css("color", "#ff914d");
           clickchecklike = 1;
           $(this).attr("id",1);
           likecount+=1;
           $(this).siblings(".like-count").text(likecount);
         }
         else if(clickchecklike == 1) {
           likestatus = 0;
           $(this).css("color", "#727272");
           clickchecklike = 0;
           $(this).attr("id",0);
           likecount-=1;
           $(this).siblings(".like-count").text(likecount);
         }
         console.log(likestatus);
         $.ajax({
              url: "/t18",
              type: "POST",
              data: {likestatus,postid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
              success:function(){
                 console.log("Success");
                 $.ajax({
                  url: "/t40",
                  type: "GET",
                  data: {request},
                  success:function(){
                    console.log('sucess')
                }
                });
            }
           });

       });

       $(".liked").on("click", function () {
         var post = $(this).parent().parent();
         postid = post.attr("id");
         var likecount = $(this).siblings(".like-count").text();
         likecount = parseInt(likecount);
         var clickcheckliked = $(this).attr("id");
         clickcheckliked = parseInt(clickcheckliked);
         console.log(clickcheckliked);
         if(clickcheckliked == 1) {
           likestatus = 0;
           $(this).css("color", "#727272");
           clickcheckliked = 0;
           $(this).attr("id",0);
           likecount-=1;
           $(this).siblings(".like-count").text(likecount);
         }
         else if(clickcheckliked == 0) {
           likestatus = 1;
           $(this).css("color", "#ff914d");
           clickcheckliked = 1;
           $(this).attr("id",1);
           likecount+=1;
           $(this).siblings(".like-count").text(likecount);
         }
         console.log(likestatus);
         $.ajax({
              url: "/t18",
              type: "POST",
              data: {likestatus,postid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
              success:function(){
                 console.log("Success");
                 $.ajax({
                  url: "/t40",
                  type: "GET",
                  data: {request},
                  success:function(){
                    console.log('sucess')
                }
                });
            }
           });
       });

       $(".reply").on("click", function () {
         $(this).hide();
         $(this).next().show();
         $(this).siblings(".reply-div").show();
       });

       $(".replied").on("click", function () {
         $(this).hide();
         $(this).prev().show();
         $(this).siblings(".reply-div").hide();
       });

       $(".reply-send").on("click", function () {
         var replydata = $(this).prev().val();
         var post_id = $(this).parent().parent().parent().attr("id");
         var reply_to = $(this).parent().siblings(".reply").attr("id");
         var replysend = $(this);
         $.ajax({
              url: "/t20",
              type: "POST",
              data: {replydata,post_id,reply_to,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
              success:function(){
                replysend.parent().hide();
                replysend.parent().siblings(".replied").hide();
                replysend.parent().siblings(".reply").show();
            }
           });
       });

       $(".comment-see-all").on("click", function () {
         $(this).parent().siblings(".all-comments").show();
         var commentid = $(this).parent().siblings(".all-comments").attr("id");
         $(this).hide();
         $(this).parent().siblings(".all-comments").children(".individual-comment").remove();
         for(var i=(parsedData.post[commentid].commentdata.length)-1; i>=0; i--) {
           if(parsedData.post[commentid].commentdata != 'null') {

             $(this).parent().siblings(".all-comments").prepend(`
              <div class="individual-comment indcom">
               <img class="comment-img" src="` + parsedData.post[commentid].dp[i] +`">
               <h1 class="comment-text">` + parsedData.post[commentid].commentdata[i] + `</h1>
              </div>
             `);

             $(this).parent().hide();

           }
         }
       });

       var clickcomment = 0;

       $(".commentbutton").on("click", function () {
         var commentid = $(this).parent().siblings(".all-comments").attr("id");
         var currentpostid = $(this).parent().parent().attr("id");
         if(clickcomment == 0) {
           $(this).parent().siblings(".all-comments").show();
           $(this).parent().siblings(".comment").children(".comment-see-all").hide();
           $(this).parent().siblings(".commentdiv").hide();
           clickcomment = 1;
           $(this).parent().siblings(".all-comments").children(".indcom").remove();
         }

         else if(clickcomment == 1){
           clickcomment = 0;
           $(this).parent().siblings(".all-comments").children(".indcom").remove();
         }


         for(var i=(parsedData.post[commentid].commentdata.length)-1; i>=0; i--) {
           if(parsedData.post[commentid].commentdata != 'null') {

             $(this).parent().siblings(".all-comments").prepend(`
              <div class="individual-comment indcom">
               <img class="comment-img" src="` + parsedData.post[commentid].dp[i] +`">
               <h1 class="comment-text">` + parsedData.post[commentid].commentdata[i] + `</h1>
              </div>
             `);

           }

         }
       });

       $(".comment-submit").on("click", function () {
         var commentdata = $(this).siblings(".comment-input").val();
         var comment = $(this).siblings(".comment-input");
         var post_id = $(this).parent().parent().parent().attr("id");
         $.ajax({
              url: "/t21",
              type: "POST",
              data: {commentdata,post_id,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
              success:function(){
                comment.val("");
                comment.parent().parent().prepend(`<div class="individual-comment">
                 <img class="comment-img" src="` + userdp +`">
                 <h1 class="comment-text">` + commentdata + `</h1>
                </div>`);
            }
           });
       });


    }
  });

$(window).scroll(function() {
   if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
     startpost += 10;
     endpost += 10;
     console.log(startpost);
     console.log(endpost);
     if(postcount < numberofposts) {
     $.ajax({
           url: "/t17",
           type: "GET",
           data: {startpost,endpost,postrequest,userid},
           success:function(data){
           var parsedData = JSON.parse(data);
           parsedDatas.push(parsedData);
           console.log(parsedData);
           for(let i = 0; i < parsedData.post.length; i++) {
             postcount++;
             groupnames = parsedData.group[i].groupname;
             groupnames = groupnames.slice(0,20);
             like = parsedData.post[i].likestatus;
             if(groupnames.length >= 20) {
               groupnames += ".."
             }
             if(parsedData.post[i].imgdata != 'NULL' && parsedData.post[i].postdata != 'NULL') {
               $(".posts-append").append(`
                <div class="post-image" id="` + parsedData.post[i].postid +`" name="`+ postcount +`">
                 <div class="group-info">
                   <img src="`+ parsedData.group[i].groupdp +`" class="group-img-post">
                   <h1 class="group-name-post">`+ groupnames +`</h1>
                   <h2 class="time-post">` + parsedData.post[i].posttime +`</h2>
                 </div>
                 <div class="delte-post">
                  `+(parsedData.post[i].delete == 1 ? '<button class="delete-icon"><i class="fa fa-trash" aria-hidden="true"></i></button>':'')+`
                  <div class="delete-confirmation">
                    <center><h1 class="delete-text">Do you want to delete this post?</h1></center>
                    <center><button class="delete-yes"><i class="fa fa-check" aria-hidden="true"></i></button>
                    <button class="delete-no"><i class="fa fa-times" aria-hidden="true"></i></button></center>
                  </div>
                 </div>
                 <div class="post-data">
                   <h1 class="post-text-data">` + parsedData.post[i].postdata + `</h1>
                   <center><img src="` + parsedData.post[i].imgdata + `" class="post-img"></center>
                 </div>
                 <div class="post-actions">` +
                 (like == 0 ? '<button class="like" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' + parsedData.post[i].likecount +'</span>': '<button class="liked" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' +  parsedData.post[i].likecount  +'</span>')
                  +`
                   <button class="comment commentbuttons"><i class="fa fa-comment" aria-hidden="true"></i></button>
                   <button class="reply" id="` + parsedData.post[i].userid + `"><i class="fa fa-reply" aria-hidden="true"></i></button>
                   <button class="replied"><i class="fa fa-reply" aria-hidden="true"></i></button>
                   <div class="reply-div">
                     <input class="reply-post" placeholder="Add a private reply"/>
                     <button class="reply-send"><i class="fa fa-share" aria-hidden="true"></i></button>
                   </div>
                   <h2 class="posted-by">Posted by ` + parsedData.user[i].name + `</h2>
                 </div>

                 `+ (parsedData.post[i].commentdata == 'null' ? '' : '<div class="comment commentdiv"><img class="comment-img" src="'+ parsedData.post[i].dp[0] +'"><h1 class="comment-text">'+ parsedData.post[i].commentdata[0] +'</h1><h2 class="comment-see-all">See all Comments</h2></div>') +`

                 <div class="all-comments" id="`+ i +`">
                   <div class="individual-comment-input">
                     <img class="comment-img" src="`+ userdp +`">
                     <input type="text" placeholder="Your Comment" class="comment-input"></input>
                     <button class="comment-submit"><i class="fa fa-chevron-circle-right" aria-hidden="true"></i></button>
                   </div>
                 </div>
               </div>
               `);
             }
             else if(parsedData.post[i].imgdata == 'NULL' && parsedData.post[i].postdata != 'NULL') {

               $(".posts-append").append(`
                <div class="post-text" id="` + parsedData.post[i].postid +`" name="`+ postcount +`">
                 <div class="group-info">
                   <img src="` + parsedData.group[i].groupdp + `" class="group-img-post">
                   <h1 class="group-name-post">` + groupnames + `</h1>
                   <h2 class="time-post">` + parsedData.post[i].posttime +`</h2>
                 </div>
                 <div class="delte-post">
                  `+(parsedData.post[i].delete == 1 ? '<button class="delete-icon"><i class="fa fa-trash" aria-hidden="true"></i></button>':'')+`
                  <div class="delete-confirmation">
                    <center><h1 class="delete-text">Do you want to delete this post?</h1></center>
                    <center><button class="delete-yes"><i class="fa fa-check" aria-hidden="true"></i></button>
                    <button class="delete-no"><i class="fa fa-times" aria-hidden="true"></i></button></center>
                  </div>
                 </div>
                 <div class="post-data">
                   <h1 class="post-text-data">`+ parsedData.post[i].postdata +`</h1>
                 </div>
                 <div class="post-actions-text">` +
                 (like == 0 ? '<button class="like" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' + parsedData.post[i].likecount +'</span>': '<button class="liked" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' +  parsedData.post[i].likecount  +'</span>')
                  +`
                   <button class="comment commentbuttons"><i class="fa fa-comment" aria-hidden="true"></i></button>
                   <button class="reply" id="` + parsedData.post[i].userid + `"><i class="fa fa-reply" aria-hidden="true"></i></button>
                   <button class="replied"><i class="fa fa-reply" aria-hidden="true"></i></button>
                   <div class="reply-div">
                     <input class="reply-post" placeholder="Add a private reply"/>
                     <button class="reply-send"><i class="fa fa-share" aria-hidden="true"></i></button>
                   </div>
                   <h2 class="posted-by">Posted by `+ parsedData.user[i].name +`</h2>
                 </div>

                 `+ (parsedData.post[i].commentdata == 'null' ? '' : '<div class="comment commentdiv"><img class="comment-img" src="'+ parsedData.post[i].dp[0] +'"><h1 class="comment-text">'+ parsedData.post[i].commentdata[0] +'</h1><h2 class="comment-see-all">See all Comments</h2></div>') +`

                 <div class="all-comments" id="`+ i +`">
                   <div class="individual-comment-input">
                     <img class="comment-img" src="`+ userdp +`">
                     <input type="text" placeholder="Your Comment" class="comment-input"></input>
                     <button class="comment-submit"><i class="fa fa-chevron-circle-right" aria-hidden="true"></i></button>
                   </div>
                 </div>
               </div>
               `);

             }

             else if(parsedData.post[i].imgdata != 'NULL' && parsedData.post[i].postdata == 'NULL') {
               $(".posts-append").append(`
                <div class="post-image-only" id="` + parsedData.post[i].postid +`" name="`+ postcount +`">
                 <div class="group-info group-info-image-only-post">
                   <img src="` + parsedData.group[i].groupdp + `" class="group-img-post">
                   <h1 class="group-name-post">` + groupnames + `</h1>
                   <h2 class="time-post">` + parsedData.post[i].posttime +`</h2>
                 </div>
                 <div class="delte-post">
                  `+(parsedData.post[i].delete == 1 ? '<button class="delete-icon"><i class="fa fa-trash" aria-hidden="true"></i></button>':'')+`
                  <div class="delete-confirmation">
                    <center><h1 class="delete-text">Do you want to delete this post?</h1></center>
                    <center><button class="delete-yes"><i class="fa fa-check" aria-hidden="true"></i></button>
                    <button class="delete-no"><i class="fa fa-times" aria-hidden="true"></i></button></center>
                  </div>
                 </div>
                 <div class="post-data">
                   <center><img src="` + parsedData.post[i].imgdata +`" class="post-img"></center>
                 </div>
                 <div class="post-actions">` +
                 (like == 0 ? '<button class="like" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' + parsedData.post[i].likecount +'</span>': '<button class="liked" id='+like+'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' +  parsedData.post[i].likecount  +'</span>')
                  +`
                   <button class="comment commentbuttons"><i class="fa fa-comment" aria-hidden="true"></i></button>
                   <button class="reply" id="` + parsedData.post[i].userid + `"><i class="fa fa-reply" aria-hidden="true"></i></button>
                   <button class="replied"><i class="fa fa-reply" aria-hidden="true"></i></button>
                   <div class="reply-div">
                     <input class="reply-post" placeholder="Add a private reply"/>
                     <button class="reply-send"><i class="fa fa-share" aria-hidden="true"></i></button>
                   </div>
                   <h2 class="posted-by">Posted by ` + parsedData.user[i].name + `</h2>
                 </div>

                 `+ (parsedData.post[i].commentdata == 'null' ? '' : '<div class="comment commentdiv"><img class="comment-img" src="'+ parsedData.post[i].dp[0] +'"><h1 class="comment-text">'+ parsedData.post[i].commentdata[0] +'</h1><h2 class="comment-see-all">See all Comments</h2></div>') +`

                 <div class="all-comments" id="`+ i +`">
                   <div class="individual-comment-input">
                     <img class="comment-img" src="`+ userdp +`">
                     <input type="text" placeholder="Your Comment" class="comment-input"></input>
                     <button class="comment-submit"><i class="fa fa-chevron-circle-right" aria-hidden="true"></i></button>
                   </div>
                 </div>
               </div>
               `);
             }
           }


           $(".like").off('click');
           $(".liked").off('click');
           $(".reply").off('click');
           $(".replied").off('click');
           $(".reply-send").off('click');
           $(".comment-see-all").off('click');
           $(".commentbuttons").off('click');
           $(".comment-submit").off('click');
           $(".delete-icon").off('click');
           $(".delete-no").off('click');
           $(".delete-yes").off('click');

           $(".delete-icon").on("click", function () {
             $(this).parent().siblings(".post-data").hide();
             $(this).parent().siblings(".post-actions").hide();
             $(this).parent().siblings(".post-actions-text").hide();
             $(this).parent().siblings(".commentdiv").hide();
             $(this).parent().siblings(".all-comments").hide();
             $(this).siblings(".delete-confirmation").show();
           });

           $(".delete-no").on("click", function () {
             $(this).parent().parent().hide();
             $(this).parent().parent().parent().siblings(".post-data").show();
             $(this).parent().parent().parent().siblings(".post-actions").show();
             $(this).parent().parent().parent().siblings(".post-actions-text").show();
             $(this).parent().parent().parent().siblings(".commentdiv").show();
           });

           $(".delete-yes").on("click", function () {
             var postid = $(this).parent().parent().parent().parent().attr("id");
             $(this).parent().parent().parent().parent().fadeOut();
             var deletepost = 1;
             $.ajax({
                   url: "/t41",
                   type: "POST",
                   data: {deletepost,postid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
                   success:function(data){
                    console.log("Success");
                 }
               });
           });

           $(".like").on("click", function () {
             var post = $(this).parent().parent();
             postid = post.attr("id");
             var likecount = $(this).siblings(".like-count").text();
             likecount = parseInt(likecount);
             var clickchecklikes = $(this).attr("id");
             clickchecklikes = parseInt(clickchecklikes);
             console.log(clickchecklikes);
             if(clickchecklikes == 0) {
               likestatus = 1;
               $(this).css("color", "#ff914d");
               clickchecklikes = 1;
               $(this).attr("id",1);
               likecount+=1;
               $(this).siblings(".like-count").text(likecount);
             }
             else if(clickchecklikes == 1) {
               likestatus = 0;
               $(this).css("color", "#727272");
               clickchecklikes = 0;
               $(this).attr("id",0);
               likecount-=1;
               $(this).siblings(".like-count").text(likecount);
             }
             console.log(likestatus);
             $.ajax({
                  url: "/t18",
                  type: "POST",
                  data: {likestatus,postid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
                  success:function(){
                     console.log("Success");
                }
               });

           });

           $(".liked").on("click", function () {
             var post = $(this).parent().parent();
             postid = post.attr("id");
             var likecount = $(this).siblings(".like-count").text();
             likecount = parseInt(likecount);
             var clickchecklikesd = $(this).attr("id");
             clickchecklikesd = parseInt(clickchecklikesd);
             console.log(clickchecklikesd);
             if(clickchecklikesd == 1) {
               likestatus = 0;
               $(this).css("color", "#727272");
               clickchecklikesd = 0;
               $(this).attr("id",0);
               likecount-=1;
               $(this).siblings(".like-count").text(likecount);
             }
             else if(clickchecklikesd == 0) {
               likestatus = 1;
               $(this).css("color", "#ff914d");
               clickchecklikesd = 1;
               $(this).attr("id",1);
               likecount+=1;
               $(this).siblings(".like-count").text(likecount);
             }
             console.log(likestatus);
             $.ajax({
                  url: "/t18",
                  type: "POST",
                  data: {likestatus,postid,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
                  success:function(){
                     console.log("Success");
                }
               });
           });

           $(".reply").on("click", function () {
             $(this).hide();
             $(this).next().show();
             $(this).siblings(".reply-div").show();
           });

           $(".replied").on("click", function () {
             $(this).hide();
             $(this).prev().show();
             $(this).siblings(".reply-div").hide();
           });

           $(".reply-send").on("click", function () {
             var replydata = $(this).prev().val();
             var post_id = $(this).parent().parent().parent().attr("id");
             var reply_to = $(this).parent().siblings(".reply").attr("id");
             var replysend = $(this);
             $.ajax({
                  url: "/t20",
                  type: "POST",
                  data: {replydata,post_id,reply_to,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
                  success:function(){
                    replysend.parent().hide();
                    replysend.parent().siblings(".replied").hide();
                    replysend.parent().siblings(".reply").show();
                }
               });
           });



           $(".comment-submit").on("click", function () {
             var commentdata = $(this).siblings(".comment-input").val();
             var comment = $(this).siblings(".comment-input");
             var post_id = $(this).parent().parent().parent().attr("id");
             $.ajax({
                  url: "/t21",
                  type: "POST",
                  data: {commentdata,post_id,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
                  success:function(){
                    comment.val("");
                    comment.parent().parent().prepend(`<div class="individual-comment">
                     <img class="comment-img" src="` + userdp +`">
                     <h1 class="comment-text">` + commentdata + `</h1>
                    </div>`);
                }
               });
           });

           function indexOfComment(currentpostid) {
             //var k = 0;
             /*for(let j = totalposts; j >= currentpostid; j--) {
               k++;
             }*/
             if(currentpostid%10 == 0) {
              indexOfTheComment = Math.floor(currentpostid/10)-2;
             }
             else if(currentpostid%10 != 0) {
             indexOfTheComment = Math.floor(currentpostid/10)-1;
            }
           }

           $(".comment-see-all").on("click", function () {
             $(this).parent().siblings(".all-comments").show();
             let commentid = $(this).parent().siblings(".all-comments").attr("id");
             var currentpostid = $(this).parent().parent().attr("name");
             console.log(parsedDatas);
             currentpostid = parseInt(currentpostid);
             indexOfComment(currentpostid);
             $(this).hide();
             console.log(parsedDatas);
             $(this).parent().siblings(".all-comments").children(".individual-comment").remove();
             for(let i=(parsedDatas[indexOfTheComment].post[commentid].commentdata.length)-1; i>=0; i--) {
               if(parsedDatas[indexOfTheComment].post[commentid].commentdata != 'null') {

                 $(this).parent().siblings(".all-comments").prepend(`
                  <div class="individual-comment indcom">
                   <img class="comment-img" src="` + parsedDatas[indexOfTheComment].post[commentid].dp[i] +`">
                   <h1 class="comment-text">` + parsedDatas[indexOfTheComment].post[commentid].commentdata[i] + `</h1>
                  </div>
                 `);

                 $(this).parent().hide();

               }
             }
           });

           var clickcomment = 0;

           $(".commentbuttons").on("click", function () {
             var commentid = $(this).parent().siblings(".all-comments").attr("id");
             var currentpostid = $(this).parent().parent().attr("name");
             currentpostid = parseInt(currentpostid);
             indexOfComment(currentpostid);
             if(clickcomment == 0) {
               $(this).parent().siblings(".all-comments").show();
               $(this).parent().siblings(".comment").children(".comment-see-all").hide();
               $(this).parent().siblings(".commentdiv").hide();
               clickcomment = 1;
               $(this).parent().siblings(".all-comments").children(".indcom").remove();
             }
             else if(clickcomment == 1){
               clickcomment = 0;
               $(this).parent().siblings(".all-comments").children(".indcom").remove();

             }

             //alert(commentid);
             for(var i=(parsedDatas[indexOfTheComment].post[commentid].commentdata.length)-1; i>=0; i--) {
               if(parsedDatas[indexOfTheComment].post[commentid].commentdata != 'null') {

                 $(this).parent().siblings(".all-comments").prepend(`
                  <div class="individual-comment indcom">
                   <img class="comment-img" src="` + parsedDatas[indexOfTheComment].post[commentid].dp[i] +`">
                   <h1 class="comment-text">` + parsedDatas[indexOfTheComment].post[commentid].commentdata[i] + `</h1>
                  </div>
                 `);

               }


           }
         });

         }


       });
     }
   }
});
