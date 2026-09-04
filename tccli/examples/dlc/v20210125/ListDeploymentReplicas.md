**Example 1: ListDeploymentReplicas**



Input: 

```
tccli dlc ListDeploymentReplicas --cli-unfold-argument  \
    --DeploymentId deploy-20260608120438-6ctf
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CpuLimit": "1",
                "CpuRequest": "400m",
                "CreateTime": 1780891479000,
                "DeploymentId": 77,
                "GpuCount": 0,
                "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:3.0.0.dev0-py311-cu125-extra-xgboost",
                "MemoryLimit": "4Gi",
                "MemoryRequest": "1.6Gi",
                "Name": "rayserve-20260608120438-185z-mt9m9-default-worker-worker-rnb9v",
                "Namespace": "dlc-p-mghaaeha",
                "NodeIp": "30.0.0.113",
                "NodeName": "30.0.0.113",
                "NodeType": "worker",
                "PodIp": "30.0.0.132",
                "RestartCount": 0,
                "StartTime": 1780891485000,
                "Status": "Running"
            }
        ],
        "Page": 1,
        "PageSize": 200,
        "Total": 2,
        "TotalPages": 1,
        "RequestId": "b031eb75-2ee3-44c9-8cb2-2ef3ce3f7b20"
    }
}
```

