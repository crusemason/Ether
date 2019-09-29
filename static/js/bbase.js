var box = document.querySelector('#newfolder-popup');
function newFolder(){
    $('#newfolder-popup').css('display','block');
    $(".cover").fadeTo(500, 0.5);

}
function t(ele){
    console.log('.list-footer'+ele);
    $('#file-icon').css('color','black');
    $('.sub-wrapper').css('display', 'block');
    $('.vert').css('display', 'block');
    if (ele != null){

    console.log(ele);
    // adding '-' the middle of name and id for regex
    var s = ele.substring(0,1) + '-' + ele.substring(1)
    }
    document.getElementById('subhtrash').href = '/trash/' + s;

    $('.list-footer').css('background', '#ffffff');
    $('.list-footer').css('color', 'black');
    $('#file-info'+ele).css('background', '#e8f0fe');
    $('#file-info'+ele).css('color', '#1967d2');

    $('.file-icon').css('color','black');

}
function newFolderClose(){
    $('#newfolder-popup').css('display', 'none');
    $(".cover").fadeOut(500);

}



function userinfoToggel(){
    if($('#user-info-p').css('display') == 'none'){
        $('#user-info-p').css('display', 'block');
    }
    else
    {
        $('#user-info-p').css('display', 'none');
    }
}
document.addEventListener("click", function(event){
    if (event.target.closest('.new-btn-wrapper')){
        console.log("inside");
        $('#new-popup').css('display', 'block');

    }
    else if (event.target.closest('.filecontainer-wrapper')){
            }
    else if (event.target.closest('.user-info')){
        console.log("user-info");
    }
    else if (event.target.closest('.file-content')){
        console.log("filecontent");
    }
    else if (event.target.closest('#img')){
        console.log("img");
    }
    else if (event.target.closest('#fontent')){
        console.log("fontent");
    }
    else if (event.target.closest('#f')){
        console.log("f");
    }
    else{
        $('#new-popup').css('display', 'none');
        $('#user-info-p').css('display', 'none');
        $('.sub-wrapper').css('display', 'none');
        $('.vert').css('display', 'none');
        $('.list-footer').css('background', '#ffffff');
        $('.list-footer').css('color', 'black');
        $('#file-icon').css('color', 'black');

    }

});

