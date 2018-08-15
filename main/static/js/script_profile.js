var WAIT_TIME_AFTER_SEND_SMS = 60;
var iTimer = WAIT_TIME_AFTER_SEND_SMS;
var sms_input_correct = false;
var sms_sended = false;
var hOntimer;
$(function () {
    $('button#btnSms').bind('click', btnSmsOnClick);
    $('input#sms').bind('change', smsOnChange);

});
var smsOnChange = function () {
    console.log(sms_sended);
    if (sms_sended) {
        console.log('text');
        checkSms($('#h1_username').text().trim(),
            $('input#sms').val().trim());
    }
}

var btnSmsOnClick = function () {

    $.ajax({
        url: "/main/sendsms/",
        type: "post",
        dataType: "text",
        data: {
            "mobile": $('#h1_username').text()
        },
        success: function (result) {
            sms_sended = true;
        }
        ,
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    });
    $(this).addClass('disabled');
    hOntimer = setTimeout('Ontimer()', 1000);

};
var Ontimer = function () {
    iTimer = iTimer - 1;
    if (iTimer > 0) {
        $('button#btnSms').text(iTimer + '秒后重试');
        hOntimer = setTimeout('Ontimer()', 1000);
    }
    else {
        iTimer = WAIT_TIME_AFTER_SEND_SMS;
        $('button#btnSms').text('发送验证码');
        $('button#btnSms').removeClass('disabled');
        clearTimeout(hOntimer);
    }


};
function confirm() {
    console.log(vaildate());
    console.log(sms_input_correct);
    return (vaildate() && sms_input_correct);
};
function vaildate() {

    if ($('input#sms').val().trim()) {
        $('p#msgSms').css('display', 'none');
    }
    else {
        $('p#msgSms').css('display', 'block');
        $('p#msgsms').text('请输入正确的验证码');
        return false;
    }
    p1 = $('input#password_1').val().trim();
    p2 = $('input#password_2').val().trim();
    if (checkPassword(p1, p2)) {
        $('p#msgPassword').css('display', 'none');
    } else {
        $('p#msgPassword').text('密码不能为空并且俩次输入要一致');
        $('p#msgPassword').css('display', 'block');
        return false;
    }
    return true;
};


var checkPassword = function (p1, p2) {

    if (p1.length <= 0) {
        return false;
    }
    else if (!(p1 === p2)) {
        return false;
    }
    else {
        return true;
    }
}
var checkSms = function (sMobile, sSMS) {
    $.ajax({
        url: "/main/checkSms/",
        type: "post",
        dataType: "text",
        data: {
            "mobile": sMobile,
            "message": sSMS
        },
        success: function (result) {
            if (result == 'True') {
                $('p#msgSms').css('display', 'none');
                sms_input_correct = true;
            }
            else {
                $('p#msgSms').css('display', 'block');
                $('p#msgsms').text('错误的验证码，请重试');
                sms_input_correct = false;
                return false;
            }
        }
        ,
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
            console.log(textStatus);
        }
    });
};

