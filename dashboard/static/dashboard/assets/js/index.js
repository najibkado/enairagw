document.addEventListener("DOMContentLoaded", () => {

    document.querySelector("#enaira").addEventListener("keyup", (e) => {

        alias = e.target.value

            fetch(`https://rgw.k8s.apis.ng/centric-platforms/uat/enaira-user/GetUserDetailsByWalletAlias`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "ClientId": "50876ecab3de3dd29554eac993939470"
                },
                body: JSON.stringify({
                    "wallet_alias": "@"+alias,
                    "user_type": "MERCHANT",
                    "channel_code": "APISNG"
                  })
            }).then(response => response.json())
            .then(result => {
                console.log(result);
                if (result.response_code == 00){
                    document.querySelector("#enairac").value = result.response_data.business_name
                } else {
                    document.querySelector("#enairac").value = result.response_data.Data.error
                }
                
            })
    })

    document.querySelector("#bvn").addEventListener("keyup", (e) => {

        bvn = e.target.value

        if (bvn.length == 11){
            fetch(`https://rgw.k8s.apis.ng/centric-platforms/uat/customer/identity/BVN`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "ClientId": "50876ecab3de3dd29554eac993939470"
                },
                body: JSON.stringify({
                    "channel_code": "APISNG",
                    "bvn": bvn
                })
            }).then(response => response.json())
            .then(result => {
                if (result.response_code == 00){
                    document.querySelector("#bvnc").value = result.response_data.firstName + " " + result.response_data.middleName + " " + result.response_data.lastName
                } else {
                    document.querySelector("#bvnc").value = result.details.message
                }
                
            })
        } 

    })


})