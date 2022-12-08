**Example 1: 创建一个自定义镜像的后付费服务**



Input: 

```
tccli tione CreateModelService --cli-unfold-argument  \
    --ServiceGroupId  \
    --ServiceGroupName demo \
    --ServiceDescription  \
    --ChargeType POSTPAID_BY_HOUR \
    --InstanceType TI.S.MEDIUM.POST \
    --ImageInfo.ImageType CCR \
    --ImageInfo.ImageUrl ccr.ccs.tencentyun.com/tiemsdev/hellotest:latest \
    --ImageInfo.RegistryRegion  \
    --ImageInfo.RegistryId  \
    --ScaleMode MANUAL \
    --Replicas 1 \
    --AuthorizationEnable False \
    --LogEnable False
```

Output: 
```
{
    "Response": {
        "Service": {
            "ServiceGroupId": "ms-gqlzzr2f",
            "ServiceId": "ms-gqlzzr2f-1",
            "ServiceGroupName": "demo",
            "ServiceDescription": "",
            "ServiceInfo": {
                "Replicas": 1,
                "ImageInfo": {
                    "ImageType": "CCR",
                    "ImageUrl": "ccr.ccs.tencentyun.com/tiemsdev/hellotest:latest",
                    "RegistryRegion": "",
                    "RegistryId": ""
                },
                "Env": [],
                "Resources": {
                    "Cpu": 2000,
                    "Memory": 4096,
                    "Gpu": 0,
                    "GpuType": "none"
                },
                "InstanceType": "TI.S.MEDIUM.POST",
                "ModelInfo": null,
                "LogEnable": false,
                "LogConfig": null,
                "AuthorizationEnable": false,
                "HorizontalPodAutoscaler": null,
                "Status": null,
                "Weight": 100,
                "PodList": [],
                "ResourceTotal": null,
                "OldReplicas": 0
            },
            "ClusterId": "",
            "Region": "ap-beijing",
            "Namespace": "",
            "ChargeType": "POSTPAID_BY_HOUR",
            "ResourceGroupId": "",
            "ResourceGroupName": "",
            "Tags": [],
            "CreatedBy": "243224118",
            "CreateTime": "",
            "UpdateTime": "",
            "Uin": "100005348929",
            "SubUin": "243224118",
            "AppId": 1256580188,
            "BusinessStatus": "CREATING",
            "CreateFailedReason": "",
            "Weight": 0,
            "Version": "",
            "LatestVersion": ""
        },
        "RequestId": "5d067ec5-def2-44f9-bed2-9b1f75b7067d"
    }
}
```

