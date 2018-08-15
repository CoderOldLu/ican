var WAIT_TIME_AFTER_SEND_SMS = 60;
var iTimer = WAIT_TIME_AFTER_SEND_SMS;
var mobile_not_exists = false;
var sms_input_correct = false;
var sms_sended = false;
var hOntimer;
$(function () {
    $('button#btnSms').bind('click', btnSmsOnClick);
    $('input#username').bind('change', mobileOnChange);
    $('input#sms').bind('change', smsOnChange);

});

var smsOnChange = function () {
    if (sms_sended) {
        if (checkMobile($('input#username').val())) {
            $('p#msgUsername').css('display', 'none');
        } else {
            $('p#msgUsername').text("请输入正确的手机号码");
            $('p#msgUsername').css('display', 'block');
            return false;
        }
        checkSms($('input#username').val().trim(),
            $('input#sms').val().trim());
    }
}
var mobileOnChange = function () {

    if (checkMobile($('input#username').val())) {
        $('p#msgUsername').css('display', 'none');
    } else {
        $('p#msgUsername').text("请输入正确的手机号码");
        $('p#msgUsername').css('display', 'block');
        return false;
    }
    checkMobileExists($('input#username').val());

}
var btnSmsOnClick = function () {
    if (checkMobile($('input#username').val())) {
        $('p#msgUsername').css('display', 'none');
    } else {
        $('p#msgUsername').text("请输入正确的手机号码");
        $('p#msgUsername').css('display', 'block');
        return false;
    }
    if (!mobile_not_exists) {
        $('p#msgUsername').text("手机号码已经被注册，请更换，否则无法发送注册码完成注册");
        $('p#msgUsername').css('display', 'block');
        return false;
    }
    $.ajax({
        url: "/main/sendsms/",
        type: "post",
        dataType: "text",
        data: {
            "mobile": $('input#username').val()
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
    return (vaildate() && mobile_not_exists && sms_input_correct);
};
function vaildate() {


    if (checkMobile($('input#username').val())) {
        $('p#msgUsername').css('display', 'none');
    } else {
        $('p#msgUsername').text("请输入正确的手机号码");
        $('p#msgUsername').css('display', 'block');
        return false;
    }

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


var checkMobile = function (sMobile) {
    if (!(/^1(3|4|5|7|8)\d{9}$/.test(sMobile))) {
        return false;
    }
    else {
        return true;
    }
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
var checkMobileExists = function (mobile) {
    $.ajax({
        url: "/main/checkMobileExists/",
        type: "post",
        dataType: "text",
        data: {
            "mobile": mobile
        },
        success: function (result) {
            if (result == 'True') {
                $('p#msgUsername').css('display', 'none');
                mobile_not_exists = true;
            } else {
                $('p#msgUsername').text("该手机号码已经被注册");
                $('p#msgUsername').css('display', 'block');
                mobile_not_exists = false;
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
