$(document).ready(function() {

$("#button_reload_site").click(function(e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "/needreload/set/1/",
        data: { csrfmiddlewaretoken: getCookie('csrftoken') }
    });
});
});
