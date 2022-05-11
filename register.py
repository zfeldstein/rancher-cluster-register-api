import httpx
import os
import json

RANCHER_HOST = os.environ["RANCHER_HOST"]
RANCHER_API_VERSION = "v3"
SSL_VERIFY = False

# String will look something like this: https://<HOST_NAME>/v3/
RANCHER_URL = "https://{}/{}/".format(RANCHER_HOST, RANCHER_API_VERSION)

rancher_token = os.environ["BEARER_TOKEN"]
headers = {
    "Authorization": "{} {}".format("Bearer", rancher_token),
    "Content-Type": "application/json",
}

def rancher_api_call(
    rancher_url, request_payload=None, http_method="get", headers=headers
):
    rancher_url = "{}{}".format(RANCHER_URL, rancher_url)
    # GET requests to Rancher API
    if http_method.lower() == "get":
        response = httpx.get(
            rancher_url, headers=headers, verify=SSL_VERIFY
        )
        return response.content
    # POST requests to Rancher API
    if http_method.lower() == "post":
        response = httpx.post(
            rancher_url, headers=headers, json=request_payload, verify=SSL_VERIFY
        )
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
            return response.status_code

        return response.content
    
    # UnComment if needed for other calls
    
    # if http_method.lower() == "delete":
    #     response = httpx.delete(url, auth=auth)
    # if http_method.lower() == "put":
    #     response = httpx.put(url, auth=auth, json=user_hash)


def register_cluster(cluster_name):
    # Rancher API endpoint to call
    endpoint = "cluster"
    # http Params to pass to endpoint
    http_params = "_replace=true"
    rancher_url = "{}?{}".format(endpoint, http_params)
    request_payload = {
        "dockerRootDir": "/var/lib/docker",
        "enableClusterAlerting": "false",
        "enableClusterMonitoring": "false",
        "enableNetworkPolicy": "false",
        "windowsPreferedCluster": "false",
        "type": "cluster",
        "name": cluster_name,
        "agentEnvVars": [],
        "labels": {},
        "annotations": {},
    }

    # response = rancher_api_call(rancher_url, request_payload=request_payload, http_method='post')
    # response = json.loads(response)
    response = {"id": "c-cq4c7"}
    # # This will get the registration Token ID
    registration_payload = {"type":"clusterRegistrationToken","clusterId": response['id']}
    # URL will look something like https://<HOST_GOES_HERE>/v3/clusters/<ID>/clusterregistrationtokens"
    registration_url = "clusterregistrationtokens"
    registration_resp = rancher_api_call(registration_url, request_payload=registration_payload, http_method='post')
    print(registration_resp)
    registration_resp = json.loads(registration_resp)
    registratio_id = registration_resp['id']
    
    # This will get the k8s manifests
    registration_manifest_url = "clusterRegistrationTokens/{}".format(registratio_id)
    registration_manifest_resp = rancher_api_call(registration_manifest_url,  http_method='get')
    registration_manifest_resp = json.loads(registration_manifest_resp)
    print(registration_manifest_resp['manifestUrl'])


register_cluster("test-import")
