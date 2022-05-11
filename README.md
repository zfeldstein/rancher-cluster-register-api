# rancher-cluster-register-api

rancher-cluster-register-api is a REST API that is built with the python FastAPI library. The API exposes a /register endpoint and takes a cluster name as path parameter. You can call the API and pass it a cluster name, the API will import the cluster into RANCHER and provide you the yaml file needed to apply on the cluster that is being imported. 

## Installation

The rancher-cluster-register-api can be ran via docker container either using docker or Kubernetes. The container requires two environment variables to be passed:

- RANCHER_HOST
- BEARER_TOKEN

The RANCHER_HOST environment variable is the hostname of your rancher server. Do not include http(s) when specificying this. If your rancher host was running on `https://example.com` then the RANCHER_HOST variable would be set to `example.com`. 

The BEARER_TOKEN is a valid token for the rancher host you speicfied above. Refer to this [page](https://rancher.com/docs/rancher/v2.5/en/user-settings/api-keys/) on how to retrieve a valid token  
```
docker run -e RANCHER_HOST='<hostNameGoesHere>' -e BEARER_TOKEN='<TOKEN_GOES_HERE>' -d --name mycontainer-test -p 7777:80 zfeldstein/rancher-register:kubectl
```

## Usage

Once the container is running, it will expose a /register endpoint on the port specified in the above command. To register a cluster named `my-cluster` to your rancher server you run the following

```
curl http://localhost:7777/register/my-cluster
```

This will import your cluster to Rancher and return the path to the yaml needed to apply on the imported cluster. 

## Disclaimer
This is proof of concept code. This is not intended for production use (yet). 
