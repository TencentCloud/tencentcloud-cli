**Example 1: 列举所有服务组**



Input: 

```
tccli tione DescribeModelServiceGroups --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ServiceGroups": [
            {
                "ServiceGroupId": "ms-9mm6npf7",
                "ServiceGroupName": "hgy-infer-preonline-bj-1",
                "CreatedBy": "xxxxxxxxx",
                "CreateTime": "2022-01-17T05:44:02Z",
                "UpdateTime": "2022-01-17T05:44:24Z",
                "Uin": "xxxxxxx",
                "ServiceCount": 1,
                "RunningServiceCount": 1,
                "Services": [
                    {
                        "ServiceGroupId": "ms-9mm6npf7",
                        "ServiceId": "ms-9mm6npf7-1",
                        "ServiceGroupName": "hgy-infer-preonline-bj-1",
                        "ServiceDescription": "",
                        "ServiceInfo": {
                            "Replicas": 1,
                            "ImageInfo": {
                                "ImageType": "",
                                "ImageUrl": "ccr.ccs.tencentyun.com/xxx/xxxxxx",
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
                            "ScaleMode": "",
                            "HorizontalPodAutoscaler": null,
                            "Status": {
                                "Replicas": 1,
                                "UpdatedReplicas": 1,
                                "ReadyReplicas": 1,
                                "AvailableReplicas": 1,
                                "UnavailableReplicas": 0,
                                "Status": "Normal",
                                "Conditions": [
                                    {
                                        "Message": "Deployment has minimum availability.",
                                        "Reason": "MinimumReplicasAvailable",
                                        "Status": "True",
                                        "Type": "Available",
                                        "LastTransitionTime": "2022-01-17T13:47:10+08:00"
                                    },
                                    {
                                        "Message": "ReplicaSet \"ms-9mm6npf7-1-548c6b4fdc\" has successfully progressed.",
                                        "Reason": "NewReplicaSetAvailable",
                                        "Status": "True",
                                        "Type": "Progressing",
                                        "LastTransitionTime": "2022-01-17T13:44:12+08:00"
                                    }
                                ]
                            },
                            "Weight": 0,
                            "PodList": [],
                            "ResourceTotal": null,
                            "OldReplicas": 1
                        },
                        "ClusterId": "",
                        "Region": "ap-beijing",
                        "Namespace": "infer-xxxxxx",
                        "ChargeType": "POSTPAID_BY_HOUR",
                        "ResourceGroupId": "",
                        "ResourceGroupName": "",
                        "Tags": [],
                        "CreatedBy": "xxxxxxxxx",
                        "CreateTime": "2022-01-17T05:44:02Z",
                        "UpdateTime": "2022-01-17T05:44:24Z",
                        "Uin": "xxxxxxx",
                        "SubUin": "",
                        "AppId": 0,
                        "BusinessStatus": "CREATE_SUCCEED",
                        "CreateFailedReason": "CREATE_SUCCEED",
                        "Weight": 100,
                        "Version": "1",
                        "LatestVersion": ""
                    }
                ],
                "Status": "Normal",
                "Tags": [],
                "BusinessStatus": "",
                "WeightUpdateStatus": "",
                "LatestVersion": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "698d2c95-afd2-4371-a9ad-701f40e39654"
    }
}
```

