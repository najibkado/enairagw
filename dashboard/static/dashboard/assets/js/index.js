document.addEventListener("DOMContentLoaded", () => {

    fetch(`https://rgw.k8s.apis.ng/centric-platforms/uat/customer/identity/BVN`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "ClientId": "50876ecab3de3dd29554eac993939470"
        },
        body: JSON.stringify({
            "channel_code": "APISNG",
            "bvn": "22227412134"
        })
    }).then(response => response.json())
    .then(result => {
        console.log(result)
    })
})