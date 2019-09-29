var count = 0;
var numdone = 0;
function startHover(){
$(document).on("mouseenter", ".fufilewrapper", function() {
    console.log("mouseneter");
    console.log(this);
  var elecheck = 'check' + this.id;
  console.log(elecheck);
  $(this).children('.fucheck').css('display','none');
   $(this).children('.fufolder').css('display','flex');

});

$(document).on("mouseleave", ".fufilewrapper", function() {
    // hover ends code here
          $(this).children('.fufolder').css('display','none');
      $(this).children('.fucheck').css('display','flex');

       console.log("mouseleave");
       console.log(this);
});
}
$(function () {

  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true,

    start: function (e) {
       $("#fu").css('display','block');
      console.log(e)
      startHover();
      $("#modal-progress").modal("show");
      $(".fuheader").css('display','flex');
        if(count == 0)
        {
            $(".futitle").text("Uploading 1 item");
        }
        else
        {
            $(".futitle").text("Uploading"+count+" items");
        }
        count = count + 1;
    },

    stop: function (e) {
      $("#modal-progress").modal("hide");
    },

    progressall: function (e, data) {
      console.log(data);
        if(count == 0)
        {
            $(".futitle").text("Uploading 1 item");
        }
        else
        {
            $(".futitle").text("Uploading "+count+" items");
        }
        count = count + 1;
      console.log('here0');
      var $fufilewrapper = $("<div class='fufilewrapper'><i id='futype' class='far fa-image fa-lg'></i><span id='funame'>"+"</span></div>");
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      $(".progress-bar").text(strProgress);
    },
    done: function (e, data) {
       $("#fu").css('display','block');
        numdone++;
        if(numdone== 1)
        {
            $(".futitle").text("Uploaded 1 item");
        }
        else
        {
            $(".futitle").text("Uploaded "+numdone+" items");
        }
      if (data.result.is_valid) {
      console.log('here0');
      var checkid = 'check' + numdone;
      var folderid = 'folder' + numdone;
      var $fufilewrapper = $("<div class='fufilewrapper' id="+numdone+"><i id='futype' class='far fa-image fa-lg'></i><span id='funame'>"+data.result.name+"</span><div class='fucheck' id="+checkid+"><i class='fas fa-check'></i></div><div id="+folderid+" class='fufolder'><i class='far fa-folder fa-lg'></i></div></div></div>");
      $("#mbody tbody").prepend($fufilewrapper);
        $("#gallery tbody").prepend(
          "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
        )
      }
    }

  });

});
