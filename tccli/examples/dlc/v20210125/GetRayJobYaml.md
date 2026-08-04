**Example 1: 获取RayJob的YAML内容**



Input: 

```
tccli dlc GetRayJobYaml --cli-unfold-argument  \
    --Id rayjob-5k01-1772774904
```

Output: 
```
{
    "Response": {
        "Yaml": "Error getting RayJob yaml: Failure executing: GET at: https://169.254.128.105:60002/apis/ray.io/v1/namespaces/kuberay-system/rayjobs/rayjob-5k01-1772774904. Message: rayjobs.ray.io \"rayjob-5k01-1772774904\" is forbidden: User \"system:serviceaccount:ns-prj64sxb-4423535-dev-test:default\" cannot get resource \"rayjobs\" in API group \"ray.io\" in the namespace \"kuberay-system\". Received status: Status(apiVersion=v1, code=403, details=StatusDetails(causes=[], group=ray.io, kind=rayjobs, name=rayjob-5k01-1772774904, retryAfterSeconds=null, uid=null, additionalProperties={}), kind=Status, message=rayjobs.ray.io \"rayjob-5k01-1772774904\" is forbidden: User \"system:serviceaccount:ns-prj64sxb-4423535-dev-test:default\" cannot get resource \"rayjobs\" in API group \"ray.io\" in the namespace \"kuberay-system\", metadata=ListMeta(_continue=null, remainingItemCount=null, resourceVersion=null, selfLink=null, additionalProperties={}), reason=Forbidden, status=Failure, additionalProperties={}).",
        "RequestId": "07be2b2e-1e50-4eb7-9ca8-46ca6a08273d"
    }
}
```

