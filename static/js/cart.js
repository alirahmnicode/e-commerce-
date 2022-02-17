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
plus_btn = $('.plus')
minus_btn = $('.minus')

total = $('.total-price')


plus_btn.click(function (event) {
    element = event.target
    // get current quantity div
    var quantity_div = element.nextElementSibling
    // get product id
    const product_id = productId(element)
    // get price div
    const price = element.offsetParent.nextElementSibling.nextElementSibling.nextElementSibling
    change_quantity('plus', quantity_div, product_id, price)
})


minus_btn.click(function (event) {
    element = event.target
    // get current quantity div
    var quantity_div = element.previousElementSibling
    // get product id
    const product_id = productId(element)
    // get price div
    const price = element.offsetParent.nextElementSibling.nextElementSibling.nextElementSibling
    change_quantity('minus', quantity_div, product_id, price)
})


// send ajax request
function change_quantity(act, quantity_div, product_id, price) {
    var quantity = act
    $.ajax({
        type: "POST",
        url: `http://localhost:8000/cart/add/${product_id}/${quantity}/`,
        headers: { 'X-CSRFToken': csrftoken },
        success: function (response) {
            quantity_div.textContent = response.quantity
            price.textContent = `$${response.price}`
            total.text(`$ ${response.total_price}`)
            // reload cart for remove product box tha deleted from cart
            if (response.remove) {
                quantity_div.textContent = "deleted"
                price.textContent = `$0`
                total.text(`$${response.total_price}`)
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

