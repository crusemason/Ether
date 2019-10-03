$(".search").click(function() {
    $("#searchui").css('display','block');
    $(".search").css('display','none');
});

$(".searchinput").click(function() {
    $(".searchinput").attr('value','');
    if($(this).val().length === 0){
    $("#sclosehover").css('display','none');
    }
})

$(".searchinput").on('input', function(){

    if($(this).val().length === 0){
    $("#sclosehover").css('display','none');
    $('#search-results').css('display','none');
    }
    $("#sclosehover").css('display','flex');
});

$(function() {
  $("body").click(function(e) {
    if (e.target.id == "searchui" || e.target.id == "searchheader" || $(e.target).parents("#searchui").length) {
    } else {
        if($('#searchui').css('display') == 'none'){

        }
        {
        $("#searchui").css('display','none');
        $("#searchheader").css('display','block');
        }
    }
  });
})
