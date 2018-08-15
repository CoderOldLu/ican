//-----------------------------------------------------------------------
$(function () {
    $('a.buy').bind('click', buy);
})
var buy = function () {
    alert("clcik");
    //return 0;
    //var $obj = $(this);
    //var str = $(this).attr("data-src");
    //var caption = "正在播放" + $(this).text();
    //var index = $(this).attr("data-index");
    //$('div#current_video').text("");
    //$('p#video_caption').text("");
    //$('a.video_link').removeClass("current_play");
    //$('div#Tutorial_Cover').css('display', 'none');
    //$('div#player').css('display', 'block');
    //$.ajax({
    //    url: "/polls/gv/",
    //    type: "post",
    //    dataType: "text",
    //    data: {
    //        VV: str
    //    },
    //    success: function (result) {
    //        console.log(result)
    //        if (result == 'login') {
    //            location.href = '/polls/register/login/?next=/polls/classes/14/';
    //        }
    //        else if (result == 'error') {
    //
    //        }
    //        else if (result == 'norights') {
    //            $('#prompt').modal('show')
    //        }
    //        else {
    //            api.load(result, function (event, api, video) {
    //                    $('div#current_video').text(index);
    //                    $('p#video_caption').text(caption);
    //                    $obj.addClass("current_play");
    //                }
    //            )
    //        }
    //    }
    //    ,
    //    error: function (XMLHttpRequest, textStatus, errorThrown) {
    //        console.log(XMLHttpRequest.status);
    //        console.log(XMLHttpRequest.readyState);
    //        console.log(textStatus);
    //    }
    //});
};
