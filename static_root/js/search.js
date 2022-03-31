var searchBox = $('#search')
var popup = $('.popup')

searchBox.keyup(function () {
    popup.empty()
    const query = searchBox[0].value
    var url = `${window.location.origin}/products/search/?q=${query}`
    if (query !== '') {
        $('.close-popup').css('display' , 'block')
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
                response.category.forEach(search_result);
                console.log(response)
                if(response.product.length == 0 && response.category.length == 0) {
                    var alert = '<div class="danger alert">nothing find...</div>'
                    popup.append(alert)
                } 
            }
        })
        $('html, body').css({
            overflow: 'hidden',
            height: '100%'
        });
    } else {
        $('.close-popup').css('display' , 'none')
        popup.css('top', '100%')
        popup.empty()
        $('html, body').css({
            overflow: 'auto',
            height: 'auto'
        });
    }
})


function search_result(item, index) {
    if(item.price == undefined) {
        var box = `<div>Category of ${item.name}</div>`
    } else {
        var box = `<div>
                        <span>${item.name}</span>
                        <span>${item.price}</span>
                    </div>`
    }
    var htmlCode = `
            <div class="result">
                <a href="/product/${item.pk}/${item.slug}">
                    <div>
                        <img src="${item.image}" alt="">
                        ${box}
                    </div>
                </a>
            </div>
                    `
    popup.append(htmlCode)
}