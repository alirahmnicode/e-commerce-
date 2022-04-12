const addBtn = $('#add-to-cart')
const messageBox = $('.message')
const close = $('.close')

addBtn.click(function () {
    move()
})

var i = 0;
function move() {
    if (i == 0) {
        i = 1;
        var elem = document.getElementById("myBar");
        var width = 1;
        var id = setInterval(frame, 50);
        function frame() {
            if (width >= 100) {
                clearInterval(id);
                messageBox.css('display','none')
                i = 0;
            } else {
                width++;
                elem.style.width = width + "%";
            }
        }
    }
}

close.click(function (e) {
    var close_div = e.target
    // close parent element
    close_div.parentElement.style.display = 'none'
})