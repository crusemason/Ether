$(document)
    .on('contextmenu', '.file-content', function(e) {
        e.preventDefault();
        console.log(this.id);
        var i = this.id
        var url = "/star/";
        var full = url + i;
        var turl = "/trash/";
        var tfull = turl + i;
        var durl = "/download/" + i;
        var dfurl = "/downloadfolder/" + i;
        console.log(full);
      document.getElementById("rmenu").className = "show";
      document.getElementById("rmenu").style.top = mouseY(event) + 'px';
      document.getElementById("rmenu").style.left = mouseX(event) + 'px';
        document.getElementById("starred").onclick = function(){
            document.getElementById("addtostar").href = full;
        }

        document.getElementById("download").onclick = function(){
            document.getElementById("download").href = durl;
        }

        document.getElementById("downloadfolder").onclick = function(){
            document.getElementById("downloadfolder").href = dfurl;
        }

        document.getElementById("trash").onclick = function(){
            document.getElementById("addtotrash").href = tfull;
            console.log(tfull);
        }

      window.event.returnValue = false;
});

$(document).ready(function() {


  if ($(".file").addEventListener) {
    $(".file").addEventListener('contextmenu', function(e) {
      e.preventDefault();
    }, false);
  } else {

    //document.getElementById("test").attachEvent('oncontextmenu', function() {
    //$(".test").bind('contextmenu', function() {
    $('body').on('contextmenu', 'a.file', function() {


      //alert("contextmenu"+event);


    });
  }

});

// this is from another SO post...
$(document).bind("click", function(event) {
  document.getElementById("rmenu").className = "hide";
  document.getElementById("rmenufolder").className = "hide";
  document.getElementById("rmenuqa").className = "hide";
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

$(document)
    .on('contextmenu', '.qafilea', function(e) {
        e.preventDefault();
        console.log(this.id);
        var i = this.id
        var url = "/star/";
        var full = url + i;
        var turl = "/trash/";
        var tfull = turl + i;
        var durl = "/download/" + i;
        var dfurl = "/downloadfolder/" + i;
        console.log(full);
      document.getElementById("rmenuqa").className = "show";
      document.getElementById("rmenuqa").style.top = mouseY(event) + 'px';
      document.getElementById("rmenuqa").style.left = mouseX(event) + 'px';
        document.getElementById("starred").onclick = function(){
            document.getElementById("addtostar").href = full;
        }

        document.getElementById("download").onclick = function(){
            document.getElementById("download").href = durl;
        }

        document.getElementById("downloadfolder").onclick = function(){
            document.getElementById("downloadfolder").href = dfurl;
        }

        document.getElementById("trash").onclick = function(){
            document.getElementById("addtotrash").href = tfull;
            console.log(tfull);
        }

      window.event.returnValue = false;
});

$(document).ready(function() {


  if ($(".file").addEventListener) {
    $(".file").addEventListener('contextmenu', function(e) {
      e.preventDefault();
    }, false);
  } else {

    //document.getElementById("test").attachEvent('oncontextmenu', function() {
    //$(".test").bind('contextmenu', function() {
    $('body').on('contextmenu', 'a.file', function() {


      //alert("contextmenu"+event);


    });
  }

});

// this is from another SO post...
$(document).bind("click", function(event) {
  document.getElementById("rmenu").className = "hide";
  document.getElementById("rmenufolder").className = "hide";
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



$(document)
    .on('contextmenu', '.foldercontainer', function(e) {
        e.preventDefault();
        console.log(this.id);
        var i = this.id
        var url = "/starfolder/";
        var full = url + i;
        var turl = "/trashfolder/";
        var tfull = turl + i;
        var durl = "/downloadfolder/" + i;
        console.log(full);
      document.getElementById("rmenufolder").className = "show";
      document.getElementById("rmenufolder").style.top = mouseY(event) + 'px';
      document.getElementById("rmenufolder").style.left = mouseX(event) + 'px';
        document.getElementById("starredfolder").onclick = function(){
            document.getElementById("addtostarfolder").href = full;
        }

        document.getElementById("downloadfolder").onclick = function(){
            document.getElementById("downloadfolder").href = durl;
        }

        document.getElementById("trashfolder").onclick = function(){
            document.getElementById("addtotrashfolder").href = tfull;
        }

      window.event.returnValue = false;
});

$(document).ready(function() {


  if ($(".file").addEventListener) {
    $(".file").addEventListener('contextmenu', function(e) {
      e.preventDefault();
    }, false);
  } else {

    //document.getElementById("test").attachEvent('oncontextmenu', function() {
    //$(".test").bind('contextmenu', function() {
    $('body').on('contextmenu', 'a.file', function() {


      //alert("contextmenu"+event);


    });
  }

});

// this is from another SO post...
$(document).bind("click", function(event) {
  document.getElementById("rmenu").className = "hide";
  document.getElementById("rmenufolder").className = "hide";
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

