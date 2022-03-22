var searchBox = $('#search')
var popup = $('.popup')

searchBox.keyup(function () {
    popup.empty()
    const query = searchBox[0].value
    var url = `${window.location.origin}/products/search/?q=${query}`
    if (query !== '') {
        var closeBtn = '<div class="close-popup">&times;</div>'
        popup.append(closeBtn)
        $.ajax({
            type: 'GET',
            url: url,
            success: function (response) {
                if ($(window).width() <= 350) {
                    popup.css('top', '15%')
                } else {
                    popup.css('top', '10%')
                }
                response.product.forEach(search_result);
            }
        })
        $('html, body').css({
            overflow: 'hidden',
            height: '100%'
        });
    } else {
        popup.css('top', '100%')
        popup.empty()
        $('html, body').css({
            overflow: 'auto',
            height: 'auto'
        });
    }
})


function search_result(item, index) {
    var htmlCode = `
            <div class="result">
                <a href="/product/${item.pk}/${item.slug}">
                    <div>
                        <img src="${item.image}" alt="">
                        <div>
                            <span>${item.name}</span>
                            <span>${item.price}</span>
                        </div>
                    </div>
                </a>
            </div>
                    `
    popup.append(htmlCode)
}