function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
    x.style.display = 'block'
  } else {
    x.className = "topnav";
    x.style.display = 'flex'
  }
}
