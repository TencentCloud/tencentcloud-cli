**Example 1: GetMLModelService**



Input: 

```
tccli wedata GetMLModelService --cli-unfold-argument  \
    --ServiceId f017d1ca-da4b-4521-9ecf-0f14827f5fb8
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
            "Description": "test_candou_0402",
            "Env": [
                {
                    "Name": "abd",
                    "Value": "1"
                }
            ],
            "ImageInfo": null,
            "InstanceType": "TI.S.MEDIUM.POST",
            "LogEnable": false,
            "MlModelInfo": {
                "Id": "917cf7f5d6eb4fc38a439b6c2c03790c",
                "ModelPath": "mlflow-artifacts:/1/917cf7f5d6eb4fc38a439b6c2c03790c/artifacts/svm_model",
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
            "ServiceId": "f017d1ca-da4b-4521-9ecf-0f14827f5fb8",
            "ServiceLimit": {
                "EnableInstanceReqLimit": false,
                "EnableInstanceRpsLimit": true,
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
        "RequestId": "88e76874-b429-422d-8f22-a6851e2c0699"
    }
}
```

