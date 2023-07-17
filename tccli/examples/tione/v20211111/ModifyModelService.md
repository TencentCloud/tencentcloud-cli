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
            "ServiceGroupId": "ms-rtvbl7bv",
            "ServiceId": "ms-rtvbl7bv-1",
            "ServiceGroupName": "test",
            "ServiceDescription": "",
            "ServiceInfo": {
                "Replicas": 1,
                "ImageInfo": {
                    "ImageType": "",
                    "ImageUrl": "ccr.ccs.tencentyun.com/tiemsdev/hellotest",
                    "RegistryRegion": "",
                    "RegistryId": ""
                },
                "Env": [
                    {
                        "Name": "test",
                        "Value": "1"
                    }
                ],
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
                "ScaleMode": "MANUAL",
                "HorizontalPodAutoscaler": null,
                "Status": null,
                "Weight": 0,
                "PodList": [],
                "ResourceTotal": null,
                "OldReplicas": 0,
                "ModelHotUpdateEnable": null,
                "OldHybridBillingPrepaidReplicas": null,
                "HybridBillingPrepaidReplicas": null
            },
            "ClusterId": "",
            "Region": "ap-beijing",
            "Namespace": "infer-100005348929",
            "ChargeType": "POSTPAID_BY_HOUR",
            "ResourceGroupId": "",
            "ResourceGroupName": "",
            "Tags": [],
            "CreatedBy": "243224118",
            "CreateTime": "2022-01-18T11:22:29Z",
            "UpdateTime": "2022-01-18T11:22:51Z",
            "Uin": "100005348929",
            "SubUin": "",
            "AppId": 0,
            "BusinessStatus": "CREATE_SUCCEED",
            "CreateFailedReason": "CREATE_SUCCEED",
            "Weight": 100,
            "Version": "1",
            "LatestVersion": "",
            "CreateSource": null,
            "ServiceLimit": null,
            "BillingInfo": null,
            "Status": null,
            "IngressName": null,
            "ScheduledAction": null
        },
        "RequestId": "f8601dc9-1319-4642-9b24-ba49fb550779"
    }
}
```

