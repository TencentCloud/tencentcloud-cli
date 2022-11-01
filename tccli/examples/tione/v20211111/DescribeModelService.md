**Example 1: 查询单个服务**



Input: 

```
tccli tione DescribeModelService --cli-unfold-argument  \
    --ServiceId ms-xxxxx-1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Service": {
            "UpdateTime": "xx",
            "ServiceGroupId": "xx",
            "CreatedBy": "xx",
            "ServiceInfo": {
                "Status": {
                    "Status": "xx",
                    "StatefulSetCondition": [
                        {
                            "Status": "xx",
                            "LastTransitionTime": "xx",
                            "Message": "xx",
                            "Type": "xx",
                            "Reason": "xx"
                        }
                    ],
                    "Replicas": 0,
                    "UpdatedReplicas": 0,
                    "AvailableReplicas": 0,
                    "UnavailableReplicas": 0,
                    "ReadyReplicas": 0
                },
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
                "Env": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "ResourceTotal": {
                    "Gpu": 1,
                    "Cpu": 1,
                    "GpuType": "xx",
                    "Memory": 1
                },
                "Weight": 1,
                "LogEnable": false,
                "AuthorizationEnable": false,
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
                    "HpaMetrics": [
                        {
                            "Name": "xx",
                            "Value": 0
                        }
                    ],
                    "MaxReplicas": 0
                },
                "LogConfig": {
                    "TopicId": "xx",
                    "LogsetId": "xx"
                },
                "InstanceType": "xx",
                "Resources": {
                    "Gpu": 1,
                    "Cpu": 1,
                    "GpuType": "xx",
                    "Memory": 1
                },
                "OldReplicas": 1
            },
            "Namespace": "xx",
            "Region": "xx",
            "ServiceGroupName": "xx",
            "ClusterId": "xx",
            "BusinessStatus": "xx",
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
    }
}
```

