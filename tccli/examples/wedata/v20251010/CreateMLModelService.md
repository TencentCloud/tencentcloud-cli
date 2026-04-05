**Example 1: 创建模型服务**



Input: 

```
tccli wedata CreateMLModelService --cli-unfold-argument  \
    --WorkspaceId 1464962169590902784 \
    --Replicas 1 \
    --AuthorizationEnable True \
    --LogEnable False \
    --ScheduledAction.ScheduleStop False \
    --ScheduledAction.ScheduleStopTime 2025-10-20T18:07:25+08:00 \
    --ChargeType POSTPAID_BY_HOUR \
    --ServiceLimit.EnableInstanceRpsLimit False \
    --ServiceLimit.InstanceRpsLimit 500 \
    --ServiceLimit.EnableInstanceReqLimit False \
    --ServiceLimit.InstanceReqLimit 1 \
    --InstanceType TI.S6.LARGE8.POST \
    --ServiceGroupId bba5f74f-3ef6-4a7a-b938-eea75ec401bc \
    --NewVersion True \
    --MlModelInfo.Id c96facaa03584d948f1f375a9e385839 \
    --MlModelInfo.Name iris_classifier_best_3_1464962169590902784 \
    --MlModelInfo.Version 1 \
    --MlModelInfo.ModelPath mlflow-artifacts:/7/c96facaa03584d948f1f375a9e385839/artifacts/model \
    --ServiceName lyric-test-v2 \
    --ServiceDescription test1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthorizationEnable": true,
            "BillingInfo": "",
            "BillingStatus": "",
            "BillingUnits": [],
            "ChargeType": "POSTPAID_BY_HOUR",
            "Command": null,
            "CreateBy": "100029411056",
            "CreateTime": "null",
            "Description": "test1",
            "Env": null,
            "ImageInfo": null,
            "InferenceTableCosBucket": "0-1315051789",
            "InferenceTablePushEnable": false,
            "InstanceType": "TI.S6.LARGE8.POST",
            "LogConfig": {
                "LogsetId": "bc6e5c63-d498-4129-99d4-33237ef88237",
                "TopicId": "f19f3dae-d15c-4de5-8bfe-4ac858a1b605"
            },
            "LogEnable": false,
            "LogStatus": "NOT_ENABLED",
            "MlModelInfo": {
                "Id": "c96facaa03584d948f1f375a9e385839",
                "ModelPath": "mlflow-artifacts:/7/c96facaa03584d948f1f375a9e385839/artifacts/model",
                "Name": "iris_classifier_best_3_1464962169590902784",
                "Version": "1"
            },
            "ModelSource": null,
            "PodInfos": null,
            "WorkspaceId": "1464962169590902784",
            "Region": "ap-beijing",
            "Replicas": 1,
            "ResourceGroupId": null,
            "ResourceGroupName": null,
            "Resources": null,
            "ScaleMode": "MANUAL",
            "ScheduledAction": {
                "ScheduleStop": false,
                "ScheduleStopTime": "2025-10-20T18:07:25+08:00"
            },
            "ServiceEIPInfo": null,
            "ServiceGroupId": "bba5f74f-3ef6-4a7a-b938-eea75ec401bc",
            "ServiceId": "bba5f74f-3ef6-4a7a-b938-eea75ec401bc-2",
            "ServiceLimit": {
                "EnableInstanceReqLimit": false,
                "EnableInstanceRpsLimit": false,
                "InstanceReqLimit": 1,
                "InstanceRpsLimit": 500
            },
            "ServiceName": "lyric-test-v2",
            "ServicePort": null,
            "ServiceType": "MACHINE_LEARNING",
            "Status": "NEW",
            "TiOneServiceGroupId": null,
            "TiOneServiceId": null,
            "UpdateTime": "null",
            "Version": 2,
            "Weight": null,
            "WorkloadStatus": null
        },
        "RequestId": "f7a2f0d0-6ca9-44f0-b35f-3f4126e8894c"
    },
    "requestId": "9c38c039-5aa5-4f0b-a183-4bcfd0874e93"
}
```

