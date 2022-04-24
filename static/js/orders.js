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

var btn = $('.opt')
var type = null
var obj_id = null

btn.click(function () {
    if (this.textContent === 'Confirme' || this.textContent === 'Reject') {
        type = 'status'
    } else {
        type = 'send'
    }
    obj_id = this.parentElement.parentElement.parentElement.id

    var url = `${window.location.origin}/order/order-verify/?type=${type}&id=${obj_id}`
    var curent_btn = this


    $.ajax({
        type: "POST",
        url: url,
        headers: { 'X-CSRFToken': csrftoken },
        success: function (response) {
            if (response.status && curent_btn.classList[2] == 'status') {
                curent_btn.innerHTML = 'Reject'
            } else if(response.status == false && curent_btn.classList[2] == 'status') {
                curent_btn.innerHTML = 'Confirme'
            }
            if (response.send == true && curent_btn.classList[2] == 'post') {
                curent_btn.innerHTML = 'Posted'
            } else if(response.send == false && curent_btn.classList[2] == 'post') {
                curent_btn.innerHTML = 'Post'
            }
        }
    })
})
