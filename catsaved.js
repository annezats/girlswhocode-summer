function addChildElements()
{
var newdiv=document.createElement("li");
var newtext=document.createTextNode("test");
newdiv.appendChild(newtext);
document.getElementById("scribble").appendChild(newdiv);
}
</script>

<script>
  function storeUserScribble(id) {
    var scribble = document.getElementById('scribble').children;
    localStorage.setItem('userScribble',scribble);
  }

  function getUserScribble() {
    if ( localStorage.getItem('userScribble')) {
      var scribble = localStorage.getItem('userScribble');
    }
    else {
      var newdiv=document.createElement("li");
      var newtext=document.createTextNode("test");
      newdiv.appendChild(newtext);
      document.getElementById("scribble").appendChild(newdiv);
    }
    document.getElementById('scribble').children = scribble;
  }
  function clearLocal() {
    clear: localStorage.clear();
    return false;
  }
