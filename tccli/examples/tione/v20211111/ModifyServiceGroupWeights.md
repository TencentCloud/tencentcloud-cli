**Example 1: test**



Input: 

```
tccli tione ModifyServiceGroupWeights --cli-unfold-argument  \
    --ServiceGroupId xx \
    --Weights.0.ServiceId xx \
    --Weights.0.Weight 1
```

Output: 
```
{
    "Response": {
        "ServiceGroup": {
            "Status": "xx",
            "UpdateTime": "xx",
            "ServiceGroupId": "xx",
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "ServiceCount": 1,
            "ServiceGroupName": "xx",
            "Uin": "xx",
            "RunningServiceCount": 1,
            "CreatedBy": "xx",
            "Services": [
                {
                    "UpdateTime": "xx",
                    "ServiceGroupId": "xx",
                    "CreatedBy": "xx",
                    "ServiceInfo": {
                        "Status": "xx",
                        "ImageInfo": {
                            "ImageUrl": "xx",
                            "RegistryRegion": "xx",
                            "RegistryId": "xx",
                            "ImageType": "xx"
                        },
                        "PodList": [
                            "xx"
                        ],
                        "Replicas": 0,
                        "ResourceTotal": {
                            "Gpu": 0,
                            "Cpu": 0,
                            "GpuType": "xx",
                            "Memory": 0
                        },
                        "Weight": 1,
                        "LogEnable": true,
                        "AuthorizationEnable": true,
                        "ModelInfo": {
                            "CosPathInfo": {
                                "Paths": [
                                    "xx"
                                ],
                                "Region": "xx",
                                "Bucket": "xx"
                            },
                            "AlgorithmFramework": "xx",
                            "ModelVersion": "xx",
                            "ModelSource": "xx",
                            "ModelName": "xx",
                            "ModelVersionId": "xx",
                            "ModelId": "xx"
                        },
                        "HorizontalPodAutoscaler": {
                            "MinReplicas": 0,
                            "HpaMetrics": {
                                "Name": "xx",
                                "Value": [
                                    0
                                ]
                            },
                            "MaxReplicas": 0
                        },
                        "LogConfig": {
                            "TopicId": "xx",
                            "LogsetId": "xx"
                        },
                        "InstanceType": "xx",
                        "Resources": {
                            "Gpu": 0,
                            "Cpu": 0,
                            "GpuType": "xx",
                            "Memory": 0
                        }
                    },
                    "Namespace": "xx",
                    "Region": "xx",
                    "ServiceGroupName": "xx",
                    "ClusterId": "xx",
                    "Uin": "xx",
                    "ResourceGroupId": "xx",
                    "ServiceId": "xx",
                    "Version": "xx",
                    "ChargeType": "xx",
                    "AppId": 0,
                    "LatestVersion": "xx",
                    "SubUin": "xx",
                    "CreateTime": "xx",
                    "ServiceDescription": "xx"
                }
            ],
            "LatestVersion": "xx",
            "CreateTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

