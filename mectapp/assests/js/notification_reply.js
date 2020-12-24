$(".search").on("click", function () {
  window.location.replace("/search");
});

$(".home").on("click", function () {
  window.location.replace("/home");
});

$(".notifications").on("click", function () {
  window.location.replace("/notifications");
});

$(".settings").on("click", function () {
  window.location.replace("/settings");
});

let request=1;

$.ajax({
      url: "/t36",
      type: "GET",
      data: {request},
      success:function(data){
        var parsedData = JSON.parse(data);
        console.log(parsedData);
        let like = parsedData.pdata[0].likestatus;
        let userdp = parsedData.logindp[0];

        let groupname = parsedData.pdata[0].groupname;
        groupname = groupname.slice(0,20);
        if(groupname.length >= 20) {
          groupname += ".."
        }


      if(parsedData.pdata[0].imgdata != 'NULL' && parsedData.pdata[0].postdata != 'NULL') {
        $(".main").append(`
        <div class="post-image" id="` + parsedData.pdata[0].postid +`">
         <div class="group-info">
           <img src="/`+ parsedData.pdata[0].gdp +`" class="group-img-post">
           <h1 class="group-name-post">`+ groupname +`</h1>
           <h2 class="time-post">` + parsedData.pdata[0].posttime +`</h2>
         </div>
         <div class="delte-post">
          `+(parsedData.pdata[0].delete == 1 ? '<button class="delete-icon"><i class="fa fa-trash" aria-hidden="true"></i></button>':'')+`
          <div class="delete-confirmation">
            <center><h1 class="delete-text">Do you want to delete this post?</h1></center>
            <center><button class="delete-yes"><i class="fa fa-check" aria-hidden="true"></i></button>
            <button class="delete-no"><i class="fa fa-times" aria-hidden="true"></i></button></center>
          </div>
         </div>
         <div class="post-data">
           <h1 class="post-text-data">` + parsedData.pdata[0].postdata + `</h1>
           <center><img src="/` + parsedData.pdata[0].imgdata + `" class="post-img"></center>
         </div>
         <div class="post-actions">` +
         (like == 0 ? '<button class="like" id='+ like +'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' + parsedData.pdata[0].likecount +'</span>': '<button class="liked" id=' + like + '><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' +  parsedData.pdata[0].likecount  +'</span>')
          +`
           <button class="comment commentbutton"><i class="fa fa-comment" aria-hidden="true"></i></button>
           <button class="reply" id="` + parsedData.pdata[0].userid + `"><i class="fa fa-reply" aria-hidden="true"></i></button>
           <button class="replied"><i class="fa fa-reply" aria-hidden="true"></i></button>
           <div class="reply-div">
             <input class="reply-post" placeholder="Add a private reply"/>
             <button class="reply-send"><i class="fa fa-share" aria-hidden="true"></i></button>
           </div>
           <h2 class="posted-by">Posted by ` + parsedData.pdata[0].name + `</h2>
         </div>
         <div class="replyresponse-div">
          <h1 class="replies-heading">Replies</h1>
          <img class="replies-img" src="/`+ parsedData.rdp[0] +`">
          <h1 class="replies-text">`+ parsedData.rdata[0] +`</h1>
         </div>
       </div>
         `);
      }

      else if(parsedData.pdata[0].imgdata == 'NULL' && parsedData.pdata[0].postdata != 'NULL') {
        $(".main").append(`
          <div class="post-text" id="` + parsedData.pdata[0].postid +`">
           <div class="group-info">
             <img src="/` + parsedData.pdata[0].gdp + `" class="group-img-post">
             <h1 class="group-name-post">` + groupname + `</h1>
             <h2 class="time-post">` + parsedData.pdata[0].posttime +`</h2>
           </div>
           <div class="delte-post">
            `+(parsedData.pdata[0].delete == 1 ? '<button class="delete-icon"><i class="fa fa-trash" aria-hidden="true"></i></button>':'')+`
            <div class="delete-confirmation">
              <center><h1 class="delete-text">Do you want to delete this post?</h1></center>
              <center><button class="delete-yes"><i class="fa fa-check" aria-hidden="true"></i></button>
              <button class="delete-no"><i class="fa fa-times" aria-hidden="true"></i></button></center>
            </div>
           </div>
           <div class="post-data">
             <h1 class="post-text-data">`+ parsedData.pdata[0].postdata +`</h1>
           </div>
           <div class="post-actions-text">` +
           (like == 0 ? '<button class="like" id='+ like +'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' + parsedData.pdata[0].likecount +'</span>': '<button class="liked" id='+ like +'><i class="fa fa-thumbs-up" aria-hidden="true"></i></button><span class="like-count">' +  parsedData.pdata[0].likecount  +'</span>')
            +`
             <button class="comment commentbutton"><i class="fa fa-comment" aria-hidden="true"></i></button>
             <button class="reply" id="` + parsedData.pdata[0].userid + `"><i class="fa fa-reply" aria-hidden="true"></i></button>
             <button class="replied"><i class="fa fa-reply" aria-hidden="true"></i></button>
             <div class="reply-div">
               <input class="reply-post" placeholder="Add a private reply"/>
               <button class="reply-send"><i class="fa fa-share" aria-hidden="true"></i></button>
             </div>
             <h2 class="posted-by">Posted by `+ parsedData.pdata[0].name +`</h2>
           </div>
           <div class="replyresponse-div">
            <h1 class="replies-heading">Replies</h1>
            <img class="replies-img" src="/`+ parsedData.rdp[0] +`">
            <h1 class="replies-text">`+ parsedData.rdata[0] +`</h1>
           </div>
         </div>
          `);
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
        $(this).siblings(".delete-confirmation").show();
        $(this).parent().siblings(".post-data").hide();
        $(this).parent().siblings(".post-actions").hide();
        $(this).parent().siblings(".post-actions-text").hide();
        $(this).parent().siblings(".commentdiv").hide();
        $(this).parent().siblings(".all-comments").hide();
        $(this).parent().siblings(".replyresponse-div").hide();
      });

      $(".delete-no").on("click", function () {
        $(this).parent().parent().hide();
        $(this).parent().parent().parent().siblings(".post-data").show();
        $(this).parent().parent().parent().siblings(".post-actions").show();
        $(this).parent().parent().parent().siblings(".post-actions-text").show();
        $(this).parent().parent().parent().siblings(".commentdiv").show();
        $(this).parent().parent().parent().siblings(".all-comments").show();
        $(this).parent().parent().parent().siblings(".replyresponse-div").show();
      });

      $('.delete-yes').on("click", function () {
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

      $(".commentbutton").on("click", function () {
          $(this).parent().siblings(".all-comments").show();
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
                <img class="comment-img" src="/` + userdp +`">
                <h1 class="comment-text">` + commentdata + `</h1>
               </div>`);
           }
          });
      });
    }
  });


  $.ajax({
    url: "/t40",
    type: "GET",
    data: {request},
    success:function(){
      console.log('sucess')
  }
  });
