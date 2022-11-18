**Example 1: 增量修改模型服务**



Input: 

```
tccli tione ModifyModelServicePartialConfig --cli-unfold-argument  \
    --ServiceId xx \
    --ScheduledAction.ScheduleStop True \
    --ScheduledAction.ScheduleStopTime xx \
    --ServiceLimit.EnableInstanceRpsLimit True \
    --ServiceLimit.InstanceRpsLimit 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Service": {
            "BusinessStatus": "xx",
            "Namespace": "xx",
            "Version": "xx",
            "SubUin": "xx",
            "Status": "xx",
            "UpdateTime": "xx",
            "ServiceGroupId": "xx",
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
                "ModelHotUpdateEnable": true,
                "Env": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "ResourceTotal": {
                    "RealGpu": 1,
                    "Cpu": 1,
                    "Memory": 1,
                    "Gpu": 1,
                    "RealGpuDetailSet": [
                        {
                            "Name": "xx",
                            "Value": 1
                        }
                    ],
                    "GpuType": "xx"
                },
                "Weight": 1,
                "LogEnable": true,
                "HybridBillingPrepaidReplicas": 0,
                "OldReplicas": 0,
                "OldHybridBillingPrepaidReplicas": 0,
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
                    "ModelType": "xx",
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
                    "RealGpu": 1,
                    "Cpu": 1,
                    "Memory": 1,
                    "Gpu": 1,
                    "RealGpuDetailSet": [
                        {
                            "Name": "xx",
                            "Value": 1
                        }
                    ],
                    "GpuType": "xx"
                },
                "AuthorizationEnable": true
            },
            "ClusterId": "xx",
            "IngressName": "xx",
            "ResourceGroupId": "xx",
            "LatestVersion": "xx",
            "ScheduledAction": {
                "ScheduleStop": true,
                "ScheduleStopTime": "xx"
            },
            "ChargeType": "xx",
            "BillingInfo": "xx",
            "CreateSource": "xx",
            "Region": "xx",
            "ServiceGroupName": "xx",
            "ServiceDescription": "xx",
            "ServiceLimit": {
                "EnableInstanceRpsLimit": true,
                "InstanceRpsLimit": 0
            },
            "Weight": 0,
            "Uin": "xx",
            "ServiceId": "xx",
            "CreatedBy": "xx",
            "AppId": 0,
            "CreateTime": "xx"
        }
    }
}
```

