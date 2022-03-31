const addBtn = $('#add-to-cart')
const messageBox = $('.message')
const close = $('.close')

addBtn.click(function () {
    closeMessage()
})


function closeMessage() {
    var width = messageBox.width()
    $(".message-time").css('width' , width)
    var id = setInterval(frame, 10)
    function frame() {
        width = width - 1
        $(".message-time").css('width', width)
        if (parseInt(width) <= 0) {
            clearInterval(id)
            messageBox.css('display','none')
        }
    }
}



close.click(function (e) {
    var close_div = e.target
    // close parent element
    close_div.parentElement.style.display = 'none'
})