//function getCookie(name) {
//    var cookieValue = null;
//    if (document.cookie && document.cookie != '') {
//        var cookies = document.cookie.split(';');
//        for (var i = 0; i < cookies.length; i++) {
//            var cookie = jQuery.trim(cookies[i]);
//            // Does this cookie string begin with the name we want?
//            if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                break;
//            }
//        }
//    }
//    return cookieValue;
//};
//var csrftoken = getCookie('csrftoken');
//
//
//function csrfSafeMethod(method) {
//    // these HTTP methods do not require CSRF protection
//    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//};
//
//$.ajaxSetup({
//    beforeSend: function (xhr, settings) {
//        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//            xhr.setRequestHeader("X-CSRFToken", csrftoken);
//        }
//    }
//});
var array_colors = new Array([11]);
array_colors[0] = "#f22932";
array_colors[1] = "#ff6d37";
array_colors[2] = "#ffc442";
array_colors[3] = "#a8cc53";
array_colors[4] = "#90d17a";
array_colors[5] = "#3dcec6";
array_colors[6] = "#31bed2";
array_colors[7] = "#1f9fd3";
array_colors[8] = "#333496";
array_colors[9] = "#990796";
array_colors[10] = "#cb3666";
$(function () {
    // set_catetory_color();
    // $('a.menu_ins').bind('click', filter_class_by_industry);
    // set_current_state();
})
var set_catetory_color = function () {
    var i = 0;
    $('div.category').each(function () {
        $(this).css('border-color', array_colors[i]);
        i = i + 1;
        if (i > 10)
            i = 0;
    })
}
var filter_class_by_industry = function () {
    var ins = $(this).attr('data-index');
    if (ins == 'all') {
        $('div#up_tutor').css('display', 'block');
        $('div#down_tutor').css('display', 'none');
    }
    else {
        $('div#up_tutor').css('display', 'none');
        $('div#down_tutor').css('display', 'block');
        $('div.category').css('display', 'none');
        $('div.category').first().css('display', 'block');
        $('div.category[data-ins="' + ins + '"]').css('display', 'block');
    }

}
var on_window_resize = function () {
    $('div#bottom').removeClass("my_fix_bottom");
    if ($(window).height() >= $(document).height()) {
        $('div#bottom').addClass('my_fix_bottom');
    }
}
var set_current_state = function () {
    var id_ins = $('div#current_ins_id').text().trim();
    $('li.menu_ins').removeClass('active');
    $('li.menu_ins[data-index="' + id_ins + '"]').addClass('active');

    var id_cat = $('div#current_cat_id').text().trim();
    $('div.category').removeClass('selected');
    $('div.category[data-cat="' + id_cat + '"]').addClass('selected');

}
