**Example 1: 查询服务组**



Input: 

```
tccli tione DescribeModelServiceGroup --cli-unfold-argument  \
    --ServiceGroupId 1234567
```

Output: 
```
{
    "Response": {
        "ServiceGroup": {
            "ServiceGroupId": "abc",
            "ServiceGroupName": "abc",
            "CreatedBy": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc",
            "Uin": "abc",
            "ServiceCount": 1,
            "RunningServiceCount": 1,
            "Services": [
                {
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
                        "InferCodeInfo": {
                            "CosPathInfo": {
                                "Bucket": "abc",
                                "Region": "abc",
                                "Paths": [
                                    "abc"
                                ]
                            }
                        },
                        "VolumeMount": {
                            "VolumeSourceType": "abc",
                            "CFSConfig": {
                                "Id": "abc",
                                "Path": "abc",
                                "MountType": "abc",
                                "Protocol": "abc"
                            }
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
                                }
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
                }
            ],
            "Status": "abc",
            "Tags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "LatestVersion": "abc",
            "BusinessStatus": "abc",
            "BillingInfo": "abc",
            "CreateSource": "abc",
            "WeightUpdateStatus": "abc"
        },
        "RequestId": "abc"
    }
}
```

