// content.js
//works but not what i need
var firstHref = $("a[href^='http']").eq(0).attr("href")
document.getElementById("test").innerHTML =firstHref;
//kind of works but not exactly

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
      var firstHref = $("a[href^='http']").eq(0).attr("href");

      console.log(firstHref);
      //document.cookie = "url =" + firstHref ;

      //save cookie to list
     //print list in website


/*function saveChanges() {
  chrome.storage.sync.set({'value': firstHref}, function() {
          // Notify that we saved.
          message('Settings saved');
        });
      }
*/

//document.cookie = "url = " + "green; expires=Thu, 18 Dec 2020 12:00:00 UTC;"

function setCookie(cname, cvalue, exdays) {
  //alert("setting cookie")
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + "," + expires + ",path=/";
}

function getCookie(cname) {
    //alert("getting cookie")
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(',');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}


function checkCookie() {
    var user=getCookie("username"); //HERE IS THE PROBLEM
    if (user != "") {
        alert("Welcome again " + user);
    } else {
       user = prompt("Please enter your name:","");
       if (user != "" && user != null) {
         console.log("here");
           //setCookie("username", user, 30);
           document.cookie = "username=" + user;
       }
    }
}
//
}
}
);
