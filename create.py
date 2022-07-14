from kubernetes import client
import yaml
from os import path


def deploy_ingress_controller(cluster_details,manifest_path="manifest/ingress-controller",namespace="default"):
    configuration = client.Configuration()
    configuration.host = cluster_details["api_server_endpoint"]
    configuration.verify_ssl = False
    configuration.api_key = {"authorization": "Bearer " + cluster_details["bearer_token"]}
    client.Configuration.set_default(configuration)

    service_account_api = client.CoreV1Api()
    serviceaccount=("controller-serviceaccount.yaml","serviceaccount.yaml")
    for i in serviceaccount:
        serviceaccount_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), serviceaccount_file_path)) as f:
            yaml_file = yaml.safe_load(f)
            service_account_api.create_namespaced_service_account(body=yaml_file,namespace="default")

    cluster_role_api = client.RbacAuthorizationV1Api()
    cluster_role=("clusterrole.yaml","controller-clusterrole.yaml")
    for i in cluster_role:
        cluster_role_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), cluster_role_file_path)) as f:
            yaml_file = yaml.safe_load(f)
            cluster_role_api.create_cluster_role(yaml_file)

    cluster_role_binding_api = client.RbacAuthorizationV1Api()
    cluster_role_binding=("clusterrolebinding.yaml","controller-clusterrolebinding.yaml")
    for i in cluster_role_binding:
        cluster_role_binding_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), cluster_role_binding_file_path)) as f:
            yaml_file = yaml.safe_load(f)
            cluster_role_binding_api.create_cluster_role_binding(yaml_file)

    role_client_api = client.RbacAuthorizationV1Api()
    role=("controller-role.yaml","role.yaml")
    for i in role:
        role_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), role_file_path)) as f:
            yaml_file = yaml.safe_load(f)
            role_client_api.create_namespaced_role(body=yaml_file,namespace="default")

    rolebinding_api = client.RbacAuthorizationV1Api()
    role=("controller-rolebinding.yaml","rolebinding.yaml")
    for i in role:
        role_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), role_file_path)) as f:
            yaml_file = yaml.safe_load(f)
            rolebinding_api.create_namespaced_role_binding(body=yaml_file,namespace="default")

    job_api = client.BatchV1Api()
    job=("job-createSecret.yaml", "job-patchWebhook.yaml")
    for i in job:
        job_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), job_file_path)) as f:
            yaml_body= yaml.safe_load(f)
            job_api.create_namespaced_job(body=yaml_body,namespace="default")

    config_map_api = client.CoreV1Api()
    config_map=["controller-configmap.yaml"]
    for i in config_map:
        config_map_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), config_map_file_path)) as f:
            yaml_file = yaml.safe_load(f)
            config_map_api.create_namespaced_config_map(body=yaml_file,namespace="default")

    service_api = client.CoreV1Api()
    service=("controller-service.yaml","controller-service-webhook.yaml")
    for i in service:
        service_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), service_file_path)) as f:
            yaml_file = yaml.safe_load(f)
            service_api.create_namespaced_service(body=yaml_file,namespace="default")

    deployment_api = client.AppsV1Api()
    deployment=["controller-deployment.yaml"]
    for i in deployment:
        deployment_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), deployment_file_path)) as f:
            yaml_file = yaml.safe_load(f)
            deployment_api.create_namespaced_deployment(body=yaml_file,namespace="default")

    ingressclass_api = client.NetworkingV1Api()
    ingress_class=["controller-ingressclass.yaml"]
    for i in ingress_class:
        ingress_class_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), ingress_class_file_path)) as f:
            yaml_file = yaml.safe_load(f)
            ingressclass_api.create_ingress_class(body=yaml_file)

    webhook_api = client.AdmissionregistrationV1Api()
    webhook=["validating-webhook.yaml"]
    for i in webhook:
        webhook_file_path="{}/{}".format(manifest_path,i)
        with open(path.join(path.dirname(__file__), webhook_file_path)) as f:
            yaml_body= yaml.safe_load(f)
            webhook_api.create_validating_webhook_configuration(body=yaml_body)

if __name__ == '__main__':
    cluster_details={
        "bearer_token":"<YOUR_BEARER_TOKEN>",
        "api_server_endpoint":"<YOUR_API_SERVER_ENDPOINT>"
    }


deploy_ingress_controller(cluster_details)  