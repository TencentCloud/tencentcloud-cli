**Example 1: DescribeServices**



Input: 

```
tccli hai DescribeServices --cli-unfold-argument  \
    --ServiceIds svc-dde3hd4i \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ServiceInfoSet": [
            {
                "ComputeSet": [
                    {
                        "BundleType": "96G_A*8",
                        "CPU": "384",
                        "Count": 1,
                        "GPUCount": "8",
                        "GPUMemory": "768",
                        "GPUPerformance": "352",
                        "Memory": "2304"
                    }
                ],
                "CreateTime": "2026-02-13 17:28:31",
                "DeploymentConfigs": [],
                "HyperParam": {},
                "ModelName": "GLM-4.7-FP8",
                "RunningReplicas": 0,
                "ServiceId": "svc-dde3hd4i",
                "ServiceName": "glm4.7-fp8",
                "ServiceState": "RUNNING",
                "TotalReplicas": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "02632e20-8bc6-4a27-b26a-92a44da57456"
    }
}
```

