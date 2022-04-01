var number = 0
var page_url = window.location.href

$(window).scroll(function (event) {
    if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
        console.log(page_url)
        number += 5
        var url_slice = page_url.split('/')
        q = url_slice[url_slice.length-1]
        if(q[0] === '?'){
            var url = `${page_url}&n=${number}`
        }else{
            var url = `${page_url}?n=${number}`
        }
        $.ajax({
            type: "GET",
            url:url,
            success: function (response) {
                for (let i = 0; i < response.length; i++) {
                    var box = `<a href="/product/${response[i].pk}/${response[i].slug}">
                        <div class="product box-hover">
                            <div><img src="${response[i].img}" alt=""></div>
                            <div>
                                <h2>${response[i].name}</h2>
                            </div>
                        </div>
                    </a>`
                    $('.boxes').append(box)

                }
            }
        })
    }
})