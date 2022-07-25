function clock() {
    var d = new Date();
    var month_num = d.getMonth()
    var day = d.getDate();
    var hours = d.getHours();
    var minutes = d.getMinutes();
    var seconds = d.getSeconds();

    month = new Array("января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря");

    if (day <= 9) day = "0" + day;
    if (hours <= 9) hours = "0" + hours;
    if (minutes <= 9) minutes = "0" + minutes;
    if (seconds <= 9) seconds = "0" + seconds;

    current_time = hours + ":" + minutes;
    current_date = day + " " + month[month_num] + " " + d.getFullYear();

    if (document.layers) {
        document.layers.current_time.document.write(current_time);
        document.layers.current_time.document.close();
        document.layers.current_date.document.write(current_date);
        document.layers.current_date.document.close();
    }
    else {
        document.getElementById("current_time").innerHTML = current_time;
        document.getElementById("current_date").innerHTML = current_date;
    }
    setTimeout("clock()", 1000);
}

