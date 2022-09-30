
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



var slideIndex = 0;
var slides_timeout;


function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    //var dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
       slides[i].style.display = "none";  
    }

    if (slideIndex > slides.length-1) {slideIndex = 0}    
    // for (i = 0; i < dots.length; i++) {
    //     dots[i].className = dots[i].className.replace(" active", "");
    // }
    slides[slideIndex].style.display = "block";  
    //dots[slideIndex-1].className += " active";
    slideIndex++;
    slides_timeout = setTimeout(showSlides, 7000); // Change image every 2 seconds
    
}

function startSlides(){
    var slideIndex = 0;
    if (typeof slides_timeout != "undefined")
     { clearTimeout( slides_timeout)}
    showSlides()
}

var d1 = new Date();
var month_num1 = d.getMonth()
var year1 = d.getFullYear();

$( document ).ready(function(){

    clock();
    $("#button_reload_site").click(function(e) {
        e.preventDefault();
        month_num1=month_num1-1;
        $.ajax({
            type: "GET",
            url: "get_calendar/",
            data: { 
                
                'year':year1,
                'month':month_num1
             }})
             .done(function (response) {
                $('#placecalendar').html(response);

             });

            });
    });


    


    
    
