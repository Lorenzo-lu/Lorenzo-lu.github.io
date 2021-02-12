function show(){
//var xx=window.frames("myframe").
var xx = document.getElementById("template_header").innerHTML;
//document.innerHTML=xx;
document.getElementByClassName('header').innerHTML = xx;
}//