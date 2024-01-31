**Example 1: 查询单个服务**



Input: 

```
tccli tione DescribeModelService --cli-unfold-argument  \
    --ServiceId ms-xxxxxx-1
```

Output: 
```
{
    "Response": {
        "Service": {
            "ServiceGroupId": "ms-ndxkhtb2",
            "ServiceId": "ms-ndxkhtb2-1",
            "ServiceGroupName": "luis-test-timeout",
            "ServiceDescription": "",
            "ServiceInfo": {
                "Replicas": 0,
                "ImageInfo": {
                    "ImageType": "CCR",
                    "ImageUrl": "ccr.ccs.tencentyun.com/tiemsdev/hellotest:latest",
                    "RegistryRegion": "ap-guangzhou",
                    "RegistryId": ""
                },
                "Env": [],
                "Resources": {
                    "Cpu": 2000,
                    "Memory": 4096,
                    "Gpu": 0,
                    "RealGpu": 0,
                    "GpuType": "",
                    "RealGpuDetailSet": []
                },
                "InstanceType": "TI.S.MEDIUM.POST",
                "ModelInfo": null,
                "InferCodeInfo": null,
                "VolumeMount": null,
                "LogEnable": false,
                "LogConfig": null,
                "AuthorizationEnable": true,
                "ScaleMode": "MANUAL",
                "HorizontalPodAutoscaler": null,
                "CronScaleJobs": [],
                "ScaleStrategy": "",
                "ScheduledAction": null,
                "Status": {
                    "Replicas": 0,
                    "UpdatedReplicas": 0,
                    "ReadyReplicas": 0,
                    "AvailableReplicas": 0,
                    "UnavailableReplicas": 0,
                    "Status": "Stopped",
                    "Reason": "",
                    "Conditions": [
                        {
                            "Message": "Deployment has minimum availability.",
                            "Reason": "MinimumReplicasAvailable",
                            "Status": "True",
                            "Type": "Available",
                            "LastTransitionTime": "2023-12-27T16:21:02+08:00",
                            "LastUpdateTime": "2023-12-27T16:21:02+08:00"
                        },
                        {
                            "Message": "ReplicaSet \"ms-ndxkhtb2-1-8579fcbb7f\" has successfully progressed.",
                            "Reason": "NewReplicaSetAvailable",
                            "Status": "True",
                            "Type": "Progressing",
                            "LastTransitionTime": "2023-12-27T16:21:02+08:00",
                            "LastUpdateTime": "2023-12-27T16:22:54+08:00"
                        }
                    ]
                },
                "Weight": 0,
                "PodList": [],
                "Pods": null,
                "PodInfos": [],
                "ResourceTotal": {
                    "Cpu": 0,
                    "Memory": 0,
                    "Gpu": 0,
                    "RealGpu": 0,
                    "GpuType": "",
                    "RealGpuDetailSet": []
                },
                "OldReplicas": 1,
                "HybridBillingPrepaidReplicas": 0,
                "OldHybridBillingPrepaidReplicas": 0,
                "ServiceLimit": {
                    "EnableInstanceRpsLimit": false,
                    "InstanceRpsLimit": 1000000,
                    "EnableInstanceReqLimit": false,
                    "InstanceReqLimit": 1000000
                },
                "Command": "",
                "ModelHotUpdateEnable": false,
                "ModelTurboEnable": false,
                "ServiceEIP": null
            },
            "ClusterId": "manger",
            "Region": "ap-guangzhou",
            "Namespace": "infer-100005348929",
            "ChargeType": "POSTPAID_BY_HOUR",
            "ResourceGroupId": "",
            "ResourceGroupName": "",
            "Tags": [],
            "IngressName": "user-ingress-gz-6",
            "CreatedBy": "243224118",
            "CreateTime": "2023-12-27T08:20:48Z",
            "UpdateTime": "2023-12-27T09:18:59Z",
            "Uin": "100005348929",
            "SubUin": "",
            "AppId": 0,
            "BusinessStatus": "CREATE_SUCCEED",
            "CreateFailedReason": "CREATE_SUCCEED",
            "Status": "Stopped",
            "BillingInfo": "",
            "Weight": 100,
            "CreateSource": "DEFAULT",
            "Version": "1",
            "LatestVersion": "1",
            "ResourceGroupSWType": "",
            "ServiceLimit": null,
            "ScheduledAction": null
        },
        "RequestId": "841f61f9-daed-49aa-88a3-b3f860be5be4"
    }
}
```

