var updateBtn = document.getElementsByClassName('update-cart')
for (i=0;i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('ProductId',productId,'active',action)
        console.log('user:',user)
        if(user === "AnonymousUser") {
            console.log('Not Login')
        } else {
            updateUserOrder(productId,action)
        }
    })
}

function updateUserOrder(productId,action) {
    console.log('User Login Success')
    var url = '/update_item/'
    fetch(url,{
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('success',data)
        location.reload()
    })
}