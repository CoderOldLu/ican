$(document).ready(function(){
	$("#demosMenu").change(function(){
	  window.location.href = $(this).find("option:selected").attr("id") + '.html';
	});
});
$(document).ready(function () {
    $('#fullpage').fullpage({
        verticalCentered: false
    });
});