import httpx
import os

RANCHER_HOST = os.environ['RANCHER_HOST']
RANCHER_API_VERSION = 'v3'
SSL_VERIFY = False

# String will look something like this: https://<HOST_NAME>/v3/
RANCHER_URL = "https://{}/{}/".format(RANCHER_HOST, RANCHER_API_VERSION)

rancher_token = os.environ['BEARER_TOKEN']
headers = {"Authorization": "{} {}".format("Bearer", rancher_token), "Content-Type": "application/json"}

def rancher_api_call(api_endpoint, http_method='get', headers=headers):
    url = "{}{}".format(RANCHER_URL, api_endpoint)
    if http_method.lower() == "get":

        response = httpx.get(url, headers=headers, verify=SSL_VERIFY)
        print(response)
    # if http_method() == "post":
    #     response = httpx.post(url, auth=auth, json=user_hash)
    # if http_method.lower() == "delete":
    #     response = httpx.delete(url, auth=auth)
    # if http_method.lower() == "put":
    #     response = httpx.put(url, auth=auth, json=user_hash)


rancher_api_call("clusters")