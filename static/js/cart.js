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
add = $('#add-to-cart')
plus_btn = $('.plus')
minus_btn = $('.minus')

total = $('.total-price')

// add to cart
add.click(function (e) {
    product_id = JSON.parse(document.getElementById('product_id').textContent)
    add_to_cart('add', null, product_id, null)
})

// Increase exist product in cart
plus_btn.click(function (event) {
    element = event.target
    // get current quantity div
    var quantity_div = element.nextElementSibling
    // get product id
    const product_id = productId(element)
    // get price div
    const price = element.offsetParent.nextElementSibling.nextElementSibling.nextElementSibling
    add_to_cart('plus', quantity_div, product_id, price)
})

// Decrease exist product in cart
minus_btn.click(function (event) {
    element = event.target
    // get current quantity div
    var quantity_div = element.previousElementSibling
    // get product id
    const product_id = productId(element)
    // get price div
    const price = element.offsetParent.nextElementSibling.nextElementSibling.nextElementSibling
    add_to_cart('minus', quantity_div, product_id, price)
})


// send ajax request
function add_to_cart(act, quantity_div, product_id, price) {
    var quantity = act
    var text = ''
    $.ajax({
        type: "POST",
        url: `http://localhost:8000/cart/add/${product_id}/${quantity}/`,
        headers: { 'X-CSRFToken': csrftoken },
        success: function (response) {
            // add product
            if (act === 'add') {
                var message = $('.message')
                var product_name = $('h1')[0].textContent
                // message text
                text = `<div>
                    <p>${response.quantity} ${product_name} added to your cart</p>
                    <p>total prise : $${response.total_price}</p>
                    <p>see <a href="/cart/">cart</a></p>
                    <p><a href="">check out</a></p>
                </div>
                `
                message.append(text)
                message.css('display','block')
            } else {
                // increase or decrease product
                quantity_div.textContent = response.quantity
                price.textContent = `$${response.price}`
                total.text(`$ ${response.total_price}`)
                if (response.remove) {
                    quantity_div.textContent = "deleted"
                    price.textContent = `$0`
                    total.text(`$${response.total_price}`)
                }
            }

        }
    })
}


// get product id
function productId(element) {
    // get link
    var a = element.offsetParent.previousElementSibling.previousElementSibling.childNodes[1].pathname
    const product_id = a.split('/')[2]
    return product_id
}



// close btn
var close = $('.close')

close.click(function(e){
    var close_div = e.target
    // close parent element
    console.log(close_div.parentElement.style.display='none')
})