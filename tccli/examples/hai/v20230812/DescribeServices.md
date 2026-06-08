**Example 1: 查询所有服务信息**



Input: 

```
tccli hai DescribeServices --cli-unfold-argument  \
    --Limit 20 \
    --Offset 20
```

Output: 
```
{
    "Response": {
        "ServiceInfoSet": [
            {
                "ComputeSet": [
                    {
                        "BundleType": "96G_A*1",
                        "CPU": "8",
                        "Count": 1,
                        "GPUCount": "1",
                        "GPUMemory": "96",
                        "GPUPerformance": "44",
                        "Memory": "80"
                    }
                ],
                "CreateTime": "2026-04-07 10:30:09",
                "DeploymentConfigs": [
                    {
                        "Container": {
                            "Envs": [
                                {
                                    "Name": "MODEL_DIRECTORY",
                                    "Value": "/data/model"
                                }
                            ],
                            "Image": {
                                "ImageRegistryUrl": "aicompute.tencentcloudcr.com/aibench/sglang:v0.5.3rc0-hml-mooncake-0.3.6"
                            },
                            "Port": "30000",
                            "Scripts": [],
                            "Storages": []
                        },
                        "ContainerCount": 1
                    }
                ],
                "HyperParam": {},
                "ModelName": "deepseek-r1 671b sglang",
                "RoleComputeSet": [
                    {
                        "BundleType": "96G_A*1",
                        "CPU": "8",
                        "Count": 1,
                        "GPUCount": "1",
                        "GPUMemory": "96",
                        "GPUPerformance": "44",
                        "Memory": "80"
                    }
                ],
                "RunningReplicas": 1,
                "SecurityType": "STANDARD",
                "ServiceId": "svc-a1b0nsvq",
                "ServiceName": "hai-autotest-final",
                "ServiceState": "UPDATING",
                "TotalReplicas": 1
            }
        ],
        "TotalCount": 38,
        "RequestId": "5d65c1f9-59c5-4597-98ed-6ac9c020b98c"
    }
}
```

