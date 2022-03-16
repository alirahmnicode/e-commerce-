const addBtn = $('#add-to-cart')

addBtn.click(function () {
    closeMessage()
})


function closeMessage() {
    var width = $(".message-time").width()
    var id = setInterval(frame, 10)
    function frame() {
        width = width - 1
        $(".message-time").css('width', width)
        if (parseInt(width) <= 0) {
            clearInterval(id)
        }
        console.log(width)
    }
}