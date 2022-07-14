### Kubernetes Python Client:


The Kubernetes Python client framework is an OpenAPI client, which means it uses a Swagger code generator (https://github.com/kubernetes-client/gen) to generate OpenAPI-compliant serializers to access core and extended API objects.


### Install Kubernetes Python Client:

`pip install kubernetes`

### Ingress Controller:


To utilize Kubernetes Ingress you will need to deploy an Ingress Controller. Now that an Ingress Controller has been set up, we can start using Ingress Resources which are another resource type defined by Kubernetes. Ingress Resources are used to update the configuration within the Ingress Controller. 


Inside the Manifest folder there are all yaml files which are needed to install an Ingress Controller.

In create.py file there is script for applying all the yaml files inside your cluster using Kubernetes Python Client. It will create all the k8s objects ins your cluster and will install ingress controller.

#### Give your cluster details:
```
cluster_details={
        "bearer_token":"Your_cluster_bearer_token",
        "api_server_endpoint":"Your_cluster_IP"
    }
```

### Run the File:
```
$ python3 create.py
```

Now, Ingress-Controller is succcessfully installed in your cluster.