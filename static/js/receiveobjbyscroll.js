var number = 0
var page_url = window.location.href

$(window).scroll(function (event) {
    if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
        number += 20
        $.ajax({
            type: "GET",
            url: `${page_url}?n=${number}`,
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