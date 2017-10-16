// toggle between adding and removing the responsive class to topnav when the user clicks on the icon
function navCollapse() {
    var nav = document.getElementById("collapse");
    if (nav.className === "topnav") {
        nav.className += " responsive";
    } else {
        nav.className = "topnav";
    }
}