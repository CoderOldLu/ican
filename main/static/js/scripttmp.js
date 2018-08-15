
var api;

$(function () {
    api = flowplayer();
    $('a.video_link').bind('click', playV);
    api.bind("finish", video_play_finish);
})
var playVideo = function () {
    console.log("play video start");
    api.load('/media/videos/1.mp4');
    console.log("play video end ");
}
var playV = function () {
    var $obj = $(this);
    var str = $(this).attr("data-src");
    var caption = "正在播放:" + $(this).text();
    var index = $(this).attr("data-index");
    $('div#current_video').text("");
    $('p#video_caption').text("");
    $('a.video_link').removeClass("current_play");
    $('div#Tutorial_Cover').css('display', 'none');
    $('div#player').css('display', 'block');
    $.ajax({
        url: "/main/gv/",
        type: "post",
        dataType: "text",
        data: {
            VV: str
        },
        success: function (result) {
            console.log(result);
            api.play({
                    sources: [
                        {
                            type: "video/mp4",
                            src: result
                            // src: 'http://7xklfs.com1.z0.glb.clouddn.com/08_Look&Feel%20Technology%20.mp4'
                        }
                    ]

                }, function (event, api, video) {
                    console.log('hello world');
                    $('div#current_video').text(index);
                    $('p#video_caption').text(caption);
                    $obj.addClass("current_play");
                }
            )
        }
        ,
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    });

    //$.post("/polls/gv/", {"VV": str, "csrfmiddlewaretoken": csrftoken}, function (result) {
    //    console.log(result);
    //    if (result != "error") {
    //        api.load(result, function (event, api, video) {
    //            $('div#current_video').text(index);
    //            $('p#video_caption').text(caption);
    //            $obj.addClass("current_play")
    //        })
    //    }
    //})
};
var ajax_test = function () {
    console.log('clicked');
    $.post("/polls/gv/", {"VV": "7"}, function (result) {
        console.log(result)
    })
};
var autoplay_switch = function () {
    $(this).removeClass('btn-default');
    $(this).removeClass('btn-primary');
    if ($(this).text().indexOf('ON') > -1) {
        $(this).text('自动播放-OFF');
        $(this).addClass('btn-default');
    }
    else {
        $(this).text('自动播放-ON');
        $(this).addClass('btn-primary');
    }
}
var video_play_finish = function (e, api) {
    var auto_play_next = $('button#autoplay_switch').eq(0).text().indexOf('ON') > -1;
    if (auto_play_next) {
        var next_index = parseInt($('div#current_video').text()) + 1;
        var strSel = "[data-index='" + next_index.toString() + "']";
        var ilen = $(strSel).length;
        if (ilen == 1) {
            $(strSel).eq(0).click();
        }
    }
}