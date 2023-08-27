**Example 1: 更新模型服务**

更新模型服务

Input: 

```
tccli tione ModifyModelService --cli-unfold-argument  \
    --ServiceDescription  \
    --InstanceType TI.S.MEDIUM.POST \
    --ImageInfo.ImageType  \
    --ImageInfo.ImageUrl ccr.ccs.tencentyun.com/xxxx/xxxxx \
    --ImageInfo.RegistryRegion  \
    --ImageInfo.RegistryId  \
    --ScaleMode MANUAL \
    --Replicas 1 \
    --LogEnable False \
    --Env.0.Name test \
    --Env.0.Value 1 \
    --ServiceId ms-xxxxx-1
```

Output: 
```
{
    "Response": {
        "Service": {
            "ServiceGroupId": "abc",
            "ServiceId": "abc",
            "ServiceGroupName": "abc",
            "ServiceDescription": "abc",
            "ServiceInfo": {
                "Replicas": 0,
                "ImageInfo": {
                    "ImageType": "abc",
                    "ImageUrl": "abc",
                    "RegistryRegion": "abc",
                    "RegistryId": "abc"
                },
                "Env": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "Resources": {
                    "Cpu": 1,
                    "Memory": 1,
                    "Gpu": 1,
                    "GpuType": "abc",
                    "RealGpu": 1,
                    "RealGpuDetailSet": [
                        {
                            "Name": "abc",
                            "Value": 1
                        }
                    ]
                },
                "InstanceType": "abc",
                "ModelInfo": {
                    "ModelId": "abc",
                    "ModelName": "abc",
                    "ModelVersionId": "abc",
                    "ModelVersion": "abc",
                    "ModelSource": "abc",
                    "CosPathInfo": {
                        "Bucket": "abc",
                        "Region": "abc",
                        "Paths": [
                            "abc"
                        ]
                    },
                    "AlgorithmFramework": "abc",
                    "ModelType": "abc",
                    "ModelFormat": "abc"
                },
                "LogEnable": true,
                "LogConfig": {
                    "LogsetId": "abc",
                    "TopicId": "abc"
                },
                "AuthorizationEnable": true,
                "ScaleMode": "abc",
                "HorizontalPodAutoscaler": {
                    "MinReplicas": 0,
                    "MaxReplicas": 0,
                    "HpaMetrics": [
                        {
                            "Name": "abc",
                            "Value": 0
                        }
                    ]
                },
                "CronScaleJobs": [
                    {
                        "Name": "abc",
                        "TargetReplicas": 0,
                        "MinReplicas": 0,
                        "MaxReplicas": 0,
                        "Schedule": "abc",
                        "ExcludeDates": [
                            "abc"
                        ]
                    }
                ],
                "ScaleStrategy": "abc",
                "ScheduledAction": "abc",
                "Status": {
                    "Replicas": 0,
                    "UpdatedReplicas": 0,
                    "ReadyReplicas": 0,
                    "AvailableReplicas": 0,
                    "UnavailableReplicas": 0,
                    "Status": "abc",
                    "StatefulSetCondition": [
                        {
                            "Message": "abc",
                            "Reason": "abc",
                            "Status": "abc",
                            "Type": "abc",
                            "LastTransitionTime": "abc"
                        }
                    ],
                    "Conditions": [
                        {
                            "Message": "abc",
                            "Reason": "abc",
                            "Status": "abc",
                            "Type": "abc",
                            "LastTransitionTime": "abc"
                        }
                    ],
                    "Reason": "abc"
                },
                "Weight": 1,
                "PodList": [
                    "abc"
                ],
                "Pods": {
                    "Name": "abc",
                    "Uid": "abc",
                    "ChargeType": "abc",
                    "Phase": "abc",
                    "IP": "abc",
                    "CreateTime": "abc",
                    "Containers": {
                        "Name": "abc",
                        "ContainerId": "abc",
                        "Image": "abc",
                        "Status": {
                            "RestartCount": 0,
                            "State": "abc",
                            "Ready": true,
                            "Reason": "abc",
                            "Message": "abc"
                        }
                    },
                    "ContainerInfos": [
                        {
                            "Name": "abc",
                            "ContainerId": "abc",
                            "Image": "abc",
                            "Status": {
                                "RestartCount": 0,
                                "State": "abc",
                                "Ready": true,
                                "Reason": "abc",
                                "Message": "abc"
                            }
                        }
                    ]
                },
                "PodInfos": [
                    {
                        "Name": "abc",
                        "Uid": "abc",
                        "ChargeType": "abc",
                        "Phase": "abc",
                        "IP": "abc",
                        "CreateTime": "abc",
                        "Containers": {
                            "Name": "abc",
                            "ContainerId": "abc",
                            "Image": "abc",
                            "Status": {
                                "RestartCount": 0,
                                "State": "abc",
                                "Ready": true,
                                "Reason": "abc",
                                "Message": "abc"
                            }
                        },
                        "ContainerInfos": [
                            {
                                "Name": "abc",
                                "ContainerId": "abc",
                                "Image": "abc",
                                "Status": {
                                    "RestartCount": 0,
                                    "State": "abc",
                                    "Ready": true,
                                    "Reason": "abc",
                                    "Message": "abc"
                                }
                            }
                        ]
                    }
                ],
                "ResourceTotal": {
                    "Cpu": 1,
                    "Memory": 1,
                    "Gpu": 1,
                    "GpuType": "abc",
                    "RealGpu": 1,
                    "RealGpuDetailSet": [
                        {
                            "Name": "abc",
                            "Value": 1
                        }
                    ]
                },
                "OldReplicas": 0,
                "HybridBillingPrepaidReplicas": 0,
                "OldHybridBillingPrepaidReplicas": 0,
                "ServiceLimit": {
                    "EnableInstanceRpsLimit": true,
                    "InstanceRpsLimit": 0
                },
                "ModelHotUpdateEnable": true,
                "ModelTurboEnable": true
            },
            "ClusterId": "abc",
            "Region": "abc",
            "Namespace": "abc",
            "ChargeType": "abc",
            "ResourceGroupId": "abc",
            "ResourceGroupName": "abc",
            "Tags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "IngressName": "abc",
            "CreatedBy": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc",
            "Uin": "abc",
            "SubUin": "abc",
            "AppId": 0,
            "BusinessStatus": "abc",
            "ServiceLimit": {
                "EnableInstanceRpsLimit": true,
                "InstanceRpsLimit": 0
            },
            "ScheduledAction": {
                "ScheduleStop": true,
                "ScheduleStopTime": "abc"
            },
            "CreateFailedReason": "abc",
            "Status": "abc",
            "BillingInfo": "abc",
            "Weight": 0,
            "CreateSource": "abc",
            "Version": "abc",
            "LatestVersion": "abc"
        },
        "RequestId": "abc"
    }
}
```

