**Example 1: UpdateMLModelService**



Input: 

```
tccli wedata UpdateMLModelService --cli-unfold-argument  \
    --ServiceId f0121 \
    --ChargeType POSTPAID_BY_HOUR \
    --MlModelInfo.Id 9c \
    --MlModelInfo.Name iris-model \
    --MlModelInfo.Version 1 \
    --MlModelInfo.ModelPath mlflow-artifacts:/1model \
    --Replicas 1 \
    --InstanceType TI.S.MEDIUM.POST \
    --ScaleMode MANUAL \
    --ServicePort 8000 \
    --ServiceLimit.EnableInstanceRpsLimit False \
    --ServiceLimit.InstanceRpsLimit 5001 \
    --ServiceLimit.EnableInstanceReqLimit False \
    --ServiceLimit.InstanceReqLimit 1 \
    --LogEnable False \
    --AuthorizationEnable False \
    --Status NEW
```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthorizationEnable": false,
            "ChargeType": "POSTPAID_BY_HOUR",
            "Command": null,
            "CreateBy": "100028649379",
            "CreateTime": "2025-04-02T10:24:17",
            "Description": null,
            "ImageInfo": null,
            "InstanceType": "TI.S.MEDIUM.POST",
            "LogEnable": false,
            "MlModelInfo": {
                "Id": "917cf7f0c",
                "ModelPath": "dddd",
                "Name": "iris-model",
                "Version": "1"
            },
            "PodInfos": null,
            "Region": "ap-guangzhou",
            "Replicas": 1,
            "Resources": null,
            "ScaleMode": "MANUAL",
            "ScheduledAction": null,
            "ServiceEIPInfo": null,
            "ServiceId": "fd27f5fb8",
            "ServiceLimit": {
                "EnableInstanceReqLimit": false,
                "EnableInstanceRpsLimit": false,
                "InstanceReqLimit": 1,
                "InstanceRpsLimit": 5001
            },
            "ServiceName": "test_candou_0402",
            "ServicePort": 8000,
            "Status": "NEW",
            "TiOneServiceGroupId": null,
            "TiOneServiceId": null,
            "WorkloadStatus": null
        },
        "RequestId": "15775d"
    }
}
```

