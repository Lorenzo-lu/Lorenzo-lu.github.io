function highlight_navbar(){
    //var url = (window.location.href);
    function compare_url(){
      var url = document.getElementById('subweb').src;
      var container = document.getElementsByClassName("container")[0];
      
      var ul = container.getElementsByTagName("ul")[0];
      var links = ul.getElementsByTagName("li");
      var lb, lia;
      var ul_height =window.innerHeight / 3;// get element height
          
//      var li_height = parseFloat(window.getComputedStyle(links[0], null).getPropertyValue('height'));   
//      
//      var padding = (ul_height / links.length - li_height)/2;
//      padding = padding / window.innerHeight * 100;
      var li_height = window.innerHeight / 100 * 2.5;
      var padding = (ul_height / links.length - li_height)/2;
      padding = padding / ul_height * 100;
      
      var i=0;     
      for(i;i<links.length;i++){
        links[i].style.padding = `${padding}% 0px`;
        links[i].className = "noncurrent";
        try{
          lia = links[i].getElementsByTagName("a")[0];
          lb = lia.getAttribute("iframe_url");       
          
          if (url.includes(lb)){ 
            /*lb is the link, url is the actual link, so if put it under some web, url should include lb*/
            links[i].className = "current";
            /*if (i != 0){
              links[0].className = "noncurrent";
            }*/
          }
        }  
        catch(err){
          console.log(err);
        }      
      }   
    }   

    var myVar = setInterval(function(){
    try{    
      compare_url();
      clearInterval(myVar);
      console.log('Fully loaded!');
    }
    catch(e){    
      //console.log('Reload: awaiting page loaded.');
      console.log(e);
    }
  }, 100); 
};


function refresh_iframe(a){ 
  lb = a.getAttribute("iframe_url");
  document.getElementById('subweb').src = lb;
  highlight_navbar();
}