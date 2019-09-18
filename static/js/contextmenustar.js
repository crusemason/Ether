$(document)
    .on('contextmenu', '.file-content', function(e) {
        e.preventDefault();
        console.log(this.id);
        var i = this.id
        var url = "/removestar/";
        var full = url + i;
        var turl = "/trash/";
        var tfull = turl + i;
        console.log(full);
      document.getElementById("rmenu").className = "show";
      document.getElementById("rmenu").style.top = mouseY(event) + 'px';
      document.getElementById("rmenu").style.left = mouseX(event) + 'px';
        document.getElementById("starred").onclick = function(){
            document.getElementById("addtostar").href = full;
        }

        document.getElementById("trash").onclick = function(){
            document.getElementById("addtotrash").href = tfull;
        }

      window.event.returnValue = false;
});

$(document).ready(function() {


  if ($(".file").addEventListener) {
    $(".file").addEventListener('contextmenu', function(e) {
      alert("You've tried to open context menu"); //here you draw your own menu
      e.preventDefault();
    }, false);
  } else {

    //document.getElementById("test").attachEvent('oncontextmenu', function() {
    //$(".test").bind('contextmenu', function() {
    $('body').on('contextmenu', 'a.file', function() {


      //alert("contextmenu"+event);
      alert(this);


    });
  }

});

// this is from another SO post...
$(document).bind("click", function(event) {
  document.getElementById("rmenu").className = "hide";
});



function mouseX(evt) {
  if (evt.pageX) {
    return evt.pageX;
  } else if (evt.clientX) {
    return evt.clientX + (document.documentElement.scrollLeft ?
      document.documentElement.scrollLeft :
      document.body.scrollLeft);
  } else {
    return null;
  }
}

function mouseY(evt) {
  if (evt.pageY) {
    return evt.pageY;
  } else if (evt.clientY) {
    return evt.clientY + (document.documentElement.scrollTop ?
      document.documentElement.scrollTop :
      document.body.scrollTop);
  } else {
    return null;
  }
}

