from urllib import response
import requests
from decouple import config

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

        # proxies = {
        #     'http': 'http://10.10.10.10:8000',
        #     'https': 'http://10.10.10.10:8000',
        # }

        # cafile = 'dashboard/adaptors/certs.pem'

        response = requests.post(self.url, headers=headers, data=body)

        if response.status_code == 200:
            res = response.json()
            print(res)
        else:
            print(response.status_code)
            print(response.json())
