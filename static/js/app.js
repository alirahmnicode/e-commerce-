var menuBtn = $('.menu-btn')
var closePopup = $('.close-popup')

menuBtn.click(function () {
    $('.popup').css('top', 0)
})

closePopup.click(function () {
    $('.popup').css('top', '100%')
})
