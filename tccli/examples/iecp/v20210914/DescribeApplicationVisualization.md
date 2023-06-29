**Example 1: test**

可视化配置

Input: 

```
tccli iecp DescribeApplicationVisualization --cli-unfold-argument  \
    --ApplicationId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e85dcda2-a3cb-4bea-a6e3-e5250bc43baf",
        "BasicInfo": {
            "Name": "teset1213",
            "ManageUrl": "",
            "Description": "",
            "CreateTime": "2021-11-23 20:29:17"
        },
        "BasicConfig": {
            "Name": "teset1213",
            "Namespace": "default",
            "Labels": [
                {
                    "Key": "qcloud-app",
                    "Value": "teset1213"
                },
                {
                    "Key": "k8s-app",
                    "Value": "teset1213"
                }
            ],
            "WorkflowKind": "Deployment",
            "GridUniqKey": "",
            "NodeSelector": null,
            "EnableServiceLinks": true,
            "Replicas": 1,
            "AvailableReplicas": null
        },
        "Volumes": [],
        "InitContainers": null,
        "Containers": [
            {
                "Name": "test",
                "ImageName": "123",
                "ImageVersion": "test",
                "ImagePullPolicy": "IfNotPresent",
                "VolumeMounts": null,
                "CpuRequest": "0.25",
                "CpuLimit": "0.5",
                "GpuLimit": "0",
                "ResourceMapCloud": null,
                "MemoryRequest": "256",
                "MemoryLimit": "1024",
                "MemoryUnit": "MiB",
                "Envs": null,
                "WorkingDir": "",
                "Commands": null,
                "Args": null,
                "SecurityContext": {
                    "Privilege": false
                },
                "ReadinessProbe": null
            }
        ],
        "Service": null,
        "Job": null,
        "CronJob": null,
        "RestartPolicy": null,
        "HorizontalPodAutoscaler": null,
        "ImagePullSecrets": null
    }
}
```

