import requests
from decouple import config
import json

class Bvn:

    url = "https://rgw.k8s.apis.ng/centric-platforms/uat/customer/identity/BVN"

    def __init__(self, bvn):
        self.bvn = bvn

    def verify(self):

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "ClientId": config('CLIENT_ID')
        }

        body = {
            "channel_code": "APISNG",
            "bvn": self.bvn
        }


        response = requests.post(self.url, headers=headers, data=body, verify=False)

        if response.status_code == 200:
            res = response.text
            print(res)
        else:
            print(response.status_code)
            print((response.json()))
