**Example 1: 创建示例**

创建一个基于自定义镜像的服务

Input: 

```
tccli tione CreateModelService --cli-unfold-argument  \
    --ServiceGroupId  \
    --ServiceGroupName demo-create \
    --ServiceDescription  \
    --ChargeType POSTPAID_BY_HOUR \
    --InstanceType TI.S.MEDIUM.POST \
    --ImageInfo.ImageType CCR \
    --ImageInfo.ImageUrl ccr.ccs.tencentyun.com/test-ccr/hellotest \
    --ImageInfo.RegistryRegion ap-guangzhou \
    --ImageInfo.RegistryId  \
    --LogEnable False \
    --ScaleMode MANUAL \
    --Replicas 1 \
    --AuthorizationEnable False \
    --ModelHotUpdateEnable False \
    --ServiceLimit.EnableInstanceRpsLimit False \
    --ServiceLimit.InstanceRpsLimit 500 \
    --ScheduledAction.ScheduleStop False \
    --ScheduledAction.ScheduleStopTime 2023-04-24T11:54:53+08:00
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
            "ServiceInfo": {
                "Replicas": 1,
                "ImageInfo": {
                    "ImageType": "CCR",
                    "ImageUrl": "ccr.ccs.tencentyun.com/test-ccr/hellotest",
                    "RegistryRegion": "ap-guangzhou",
                    "RegistryId": ""
                },
                "Env": [],
                "Resources": {
                    "Cpu": 2000,
                    "Memory": 4096,
                    "Gpu": 0,
                    "RealGpu": 0,
                    "GpuType": "none",
                    "RealGpuDetailSet": []
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
            "CreatedBy": "10000000000",
            "CreateTime": "",
            "UpdateTime": "",
            "Uin": "10000000000",
            "SubUin": "10000000000",
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
                "InstanceRpsLimit": 500
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

