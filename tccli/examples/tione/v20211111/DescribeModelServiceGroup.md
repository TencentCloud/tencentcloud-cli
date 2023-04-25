**Example 1: 查询服务组**



Input: 

```
tccli tione DescribeModelServiceGroup --cli-unfold-argument  \
    --ServiceGroupId xx
```

Output: 
```
{
    "Response": {
        "ServiceGroup": {
            "ServiceGroupId": "test",
            "ServiceGroupName": "test",
            "CreatedBy": "xxxxx",
            "CreateTime": "2022-01-15T09:31:49Z",
            "UpdateTime": "2022-01-15T09:32:51Z",
            "Uin": "xxxx",
            "ServiceCount": 0,
            "RunningServiceCount": 0,
            "Services": [
                {
                    "ServiceGroupId": "ms-nx4m7zjh",
                    "ServiceId": "ms-nx4m7zjh-1",
                    "ServiceGroupName": "test",
                    "ServiceDescription": "",
                    "ServiceInfo": {
                        "Replicas": 0,
                        "ImageInfo": {
                            "ImageType": "",
                            "ImageUrl": "nignx",
                            "RegistryRegion": "",
                            "RegistryId": ""
                        },
                        "Env": [],
                        "Resources": {
                            "Cpu": 2000,
                            "Memory": 4096,
                            "Gpu": 0,
                            "GpuType": ""
                        },
                        "InstanceType": "TI.S.MEDIUM.POST",
                        "ModelInfo": null,
                        "LogEnable": false,
                        "LogConfig": null,
                        "AuthorizationEnable": false,
                        "ScaleMode": "MANUAL",
                        "HorizontalPodAutoscaler": null,
                        "Status": {
                            "Replicas": 0,
                            "UpdatedReplicas": 0,
                            "ReadyReplicas": 0,
                            "AvailableReplicas": 0,
                            "UnavailableReplicas": 0,
                            "Status": "Stopped",
                            "Conditions": [
                                {
                                    "Message": "Deployment has minimum availability.",
                                    "Reason": "MinimumReplicasAvailable",
                                    "Status": "True",
                                    "Type": "Available",
                                    "LastTransitionTime": "2022-01-15T17:32:52+08:00"
                                },
                                {
                                    "Message": "ReplicaSet \"ms-nx4m7zjh-1-8bd6f8459\" has successfully progressed.",
                                    "Reason": "NewReplicaSetAvailable",
                                    "Status": "True",
                                    "Type": "Progressing",
                                    "LastTransitionTime": "2022-01-15T17:32:00+08:00"
                                }
                            ]
                        },
                        "Weight": 0,
                        "PodList": [],
                        "ResourceTotal": {
                            "Cpu": 0,
                            "Memory": 0,
                            "Gpu": 0,
                            "GpuType": ""
                        },
                        "OldReplicas": 1
                    },
                    "ClusterId": "",
                    "Region": "ap-guangzhou",
                    "Namespace": "infer-xxxx",
                    "ChargeType": "POSTPAID_BY_HOUR",
                    "ResourceGroupId": "",
                    "ResourceGroupName": "",
                    "Tags": [],
                    "CreatedBy": "700000207674",
                    "CreateTime": "2022-01-15T09:31:49Z",
                    "UpdateTime": "2022-01-15T09:32:51Z",
                    "Uin": "xxxx",
                    "SubUin": "",
                    "AppId": 0,
                    "BusinessStatus": "CREATE_SUCCEED",
                    "CreateFailedReason": "CREATE_SUCCEED",
                    "Weight": 100,
                    "Version": "1",
                    "LatestVersion": ""
                }
            ],
            "Status": "",
            "Tags": [],
            "BusinessStatus": "",
            "WeightUpdateStatus": "UPDATED",
            "LatestVersion": "1"
        },
        "RequestId": "e0973750-4641-4c28-8040-27744b7723a0"
    }
}
```

