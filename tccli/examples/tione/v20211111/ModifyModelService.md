**Example 1: 更新在线服务**



Input: 

```
tccli tione ModifyModelService --cli-unfold-argument  \
    --ServiceId ms-h29wqz2b-1 \
    --ServiceAction STOP
```

Output: 
```
{
    "Response": {
        "Service": {
            "ServiceGroupId": "ms-skdg89rx",
            "ServiceId": "ms-skdg89rx-1",
            "ServiceGroupName": "demo-create",
            "ServiceDescription": "",
            "Uin": "100030513581",
            "SubUin": "100030513581",
            "CreatedBy": "100044299491",
            "ServiceInfo": {
                "Replicas": 1,
                "ImageInfo": {
                    "ImageType": "CCR",
                    "ImageUrl": "ccr.ccs.tencentyun.com/jiaqi-3581-test/mock_service:tione_20250509",
                    "RegistryRegion": "ap-guangzhou",
                    "RegistryId": ""
                },
                "Env": [],
                "Resources": {
                    "Cpu": 1000,
                    "Memory": 1024,
                    "Gpu": 0,
                    "RealGpu": 0,
                    "GpuType": "GPU-GN7",
                    "RealGpuDetailSet": [],
                    "EnableRDMA": false
                },
                "InstanceType": "TI.S.MEDIUM.POST",
                "ModelInfo": null,
                "LogEnable": false,
                "LogConfig": null,
                "AuthorizationEnable": false,
                "ScaleMode": "MANUAL",
                "HorizontalPodAutoscaler": null,
                "CronScaleJobs": [],
                "ScaleStrategy": "",
                "Status": null,
                "Weight": 100,
                "PodList": [],
                "Pods": null,
                "PodInfos": [],
                "ResourceTotal": null,
                "OldReplicas": 0,
                "HybridBillingPrepaidReplicas": 0,
                "OldHybridBillingPrepaidReplicas": 0,
                "ModelHotUpdateEnable": false
            },
            "ClusterId": "",
            "Region": "ap-guangzhou",
            "Namespace": "",
            "ChargeType": "POSTPAID_BY_HOUR",
            "ResourceGroupId": "",
            "ResourceGroupName": "",
            "Tags": [],
            "IngressName": "user-ingress-1",
            "CreateTime": "",
            "UpdateTime": "",
            "AppId": 10000000000,
            "BusinessStatus": "CREATING",
            "CreateFailedReason": "",
            "Status": "",
            "BillingInfo": "",
            "Weight": 100,
            "CreateSource": "DEFAULT",
            "Version": "",
            "LatestVersion": "",
            "ServiceLimit": {
                "EnableInstanceRpsLimit": false,
                "InstanceRpsLimit": 0,
                "EnableInstanceReqLimit": false,
                "InstanceReqLimit": 0
            },
            "ScheduledAction": {
                "ScheduleStop": false,
                "ScheduleStopTime": "2023-04-24T11:54:53+08:00"
            }
        },
        "RequestId": "b8f848e4-64ea-475c-864e-6d4b0c9ec6ea"
    }
}
```

