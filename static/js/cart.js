// get client cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// get btns
var add = $('#add-to-cart')
var plus_btn = $('.plus')
var minus_btn = $('.minus')
var total = $('.total-price')
var productCount = $('.product-count')

// add to cart
add.click(function (e) {
    product_id = JSON.parse(document.getElementById('product_id').textContent)
    add_to_cart('add', null, product_id, null)
})

// Increase exist product in cart
plus_btn.click(function (event) {
    cartBtnCount(1)
    element = event.target
    // get current quantity div
    var quantity_div = element.nextElementSibling
    // get product id
    const product_id = productId(element)
    // get price div
    const price = element.parentElement.parentElement.lastElementChild.children[0]
    add_to_cart('plus', quantity_div, product_id, price)
})

// Decrease exist product in cart
minus_btn.click(function (event) {
    cartBtnCount(-1)
    element = event.target
    // get current quantity div
    var quantity_div = element.previousElementSibling
    // get product id
    const product_id = productId(element)
    // get price div
    const price = element.parentElement.parentElement.lastElementChild.children[0]
    add_to_cart('minus', quantity_div, product_id, price)
})


// send ajax request
function add_to_cart(act, quantity_div, product_id, price) {
    var quantity = act
    var url = `${window.location.origin}/cart/add/${product_id}/${quantity}/`
    $.ajax({
        type: "POST",
        url: url,
        headers: { 'X-CSRFToken': csrftoken },
        success: function (response) {
            // add product
            if (act === 'add') {
                cartBtnCount(1)
                var message = $('.message')
                var product_name = $('h1')[0].textContent
                var text_message = $('.text-message')
                text_message.empty()
                // message text
                var text = `<div class="text-message">
                    <p>${response.quantity} ${product_name} added to your cart</p>
                    <p>total prise : $${response.total_price}</p>
                    <p><a href="/cart/">see cart</a></p>
                    <p><a href="/order/payment/">check out</a></p>
                </div>
                `
                message.append(text)
                message.css('display', 'block')
            } else {
                // increase or decrease product
                quantity_div.textContent = response.quantity
                price.textContent = priceFilter(String(response.price))
                total.text(priceFilter(String(response.total_price)))
                productCount.text(response.count)
                if (response.remove) {
                    quantity_div.textContent = "deleted"
                    price.textContent = `$0`
                    total.text(priceFilter(String(response.total_price)))
                    productCount.text('0')
                }
            }

        }
    })
}


// get product id
function productId(element) {
    // get link
    var a = element.parentElement.parentElement.previousElementSibling.firstElementChild.pathname
    const product_id = a.split('/')[2]
    return product_id
}


var cartBtn = $('.cart-count')

function cartBtnCount(i) {
    var count = parseInt(cartBtn[0].textContent) + i
    cartBtn[0].textContent = count
}


// price filter
function priceFilter(p) {
    console.log(p)
    var price = p.split('')
    var numbers = price.filter(function (value, index, arr) {
        return value !== "" && value !== '$';
    });
    var new_price = ''
    var n = 0
    for (var i = numbers.length - 1; i >= 0; i--) {
        n++
        if (n % 3 == 0 && n < numbers.length) {
            new_price += `${numbers[i]}'`
        } else {
            new_price += numbers[i]
        }
    }
    return `$${new_price.split("").reverse().join("")}`
}