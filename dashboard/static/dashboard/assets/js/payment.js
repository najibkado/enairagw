document.addEventListener("DOMContentLoaded", () => {

    getToken()

})

function getToken(){
    reference = create_UUID()
    fetch(`https://rgw.k8s.apis.ng/centric-platforms/uat/CAMLLogin`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "ClientId": "50876ecab3de3dd29554eac993939470"
        },
        body: JSON.stringify({
            "user_id": "najibkado@gmail.com",
            "password": "eNairaGateway1!",
            "allow_tokenization": "Y",
            "user_type": "MERCHANT",
            "channel_code": "APISNG"
        })
    }).then(response => response.json())
    .then(result => {
        pay(result.response_data.token, reference);
    })
}

function create_UUID(){
    var dt = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (dt + Math.random()*16)%16 | 0;
        dt = Math.floor(dt/16);
        return (c=='x' ? r :(r&0x3|0x8)).toString(16);
    });
    return uuid.slice(0, 10);
}

function pay(token, ref) {
    fetch(`https://rgw.k8s.apis.ng/centric-platforms/uat/CreateDeposit`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "ClientId": "50876ecab3de3dd29554eac993939470"
        },
        body: JSON.stringify({
            "user_id": "najibkado@gmail.com",
            "user_type": "MERCHANT",
            "user_email": "najibkado@gmail.com",
            "user_token": token,
            "account_no": "0760261888",
            "amount": "1000.00",
            "reference": ref,
            "narration": "Merchant Order Deposit",
            "channel_code": "APISNG"
            })
    }).then(response => response.json())
    .then(result => {
        console.log(result)
    })
}