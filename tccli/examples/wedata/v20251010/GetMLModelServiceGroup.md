**Example 1: GetMLModelServiceGroup**



Input: 

```
tccli wedata GetMLModelServiceGroup --cli-unfold-argument  \
    --WorkspaceId 1464962169590902784 \
    --ServiceGroupId ef16f77c-fd0b-48a9-bc77-da8714f0d31e
```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthTokens": null,
            "AuthorizationEnable": false,
            "BillingInfo": null,
            "BusinessStatus": null,
            "CreateBy": "100044235093",
            "CreateTime": "2025-10-16T14:00:55",
            "Description": null,
            "InferenceTableCosBucket": "abe-test-1315051789",
            "InferenceTablePushEnable": true,
            "LatestVersion": "1",
            "LogConfig": {
                "LogsetId": "54ab04b8-1a1e-4303-bfc6-e1469577329a",
                "TopicId": "7dea72a8-10bd-40dd-9dae-c1bae94db044"
            },
            "LogEnable": true,
            "WorkspaceId": "1464962169590902784",
            "RunningServiceCount": null,
            "ServiceCount": 1,
            "ServiceGroupId": "ef16f77c-fd0b-48a9-bc77-da8714f0d31e",
            "ServiceGroupName": "blueszzhang-model-test-final",
            "ServiceType": "MACHINE_LEARNING",
            "Services": [
                {
                    "AuthorizationEnable": true,
                    "BillingInfo": "",
                    "BillingStatus": "",
                    "BillingUnits": [],
                    "ChargeType": "POSTPAID_BY_HOUR",
                    "Command": null,
                    "CreateBy": "100044235093",
                    "CreateTime": "2025-10-16T14:00:55",
                    "Description": null,
                    "Env": null,
                    "ImageInfo": null,
                    "InferenceTableCosBucket": "abe-test-1315051789",
                    "InferenceTablePushEnable": true,
                    "InstanceType": "TI.S6.LARGE8.POST",
                    "LogConfig": {
                        "LogsetId": "54ab04b8-1a1e-4303-bfc6-e1469577329a",
                        "TopicId": "7dea72a8-10bd-40dd-9dae-c1bae94db044"
                    },
                    "LogEnable": true,
                    "LogStatus": "ENABLING",
                    "MlModelInfo": {
                        "Id": "c96facaa03584d948f1f375a9e385839",
                        "ModelPath": "mlflow-artifacts:/7/c96facaa03584d948f1f375a9e385839/artifacts/model",
                        "Name": "iris_classifier_best_3_1464962169590902784",
                        "Version": "1"
                    },
                    "ModelSource": "MODEL",
                    "PodInfos": null,
                    "WorkspaceId": "1464962169590902784",
                    "Region": "ap-guangzhou",
                    "Replicas": 1,
                    "ResourceGroupId": null,
                    "ResourceGroupName": null,
                    "Resources": null,
                    "ScaleMode": "MANUAL",
                    "ScheduledAction": {
                        "ScheduleStop": false,
                        "ScheduleStopTime": "2025-10-16T14:30:18+08:00"
                    },
                    "ServiceEIPInfo": null,
                    "ServiceGroupId": "ef16f77c-fd0b-48a9-bc77-da8714f0d31e",
                    "ServiceId": "ef16f77c-fd0b-48a9-bc77-da8714f0d31e-1",
                    "ServiceLimit": {
                        "EnableInstanceReqLimit": false,
                        "EnableInstanceRpsLimit": false,
                        "InstanceReqLimit": 1,
                        "InstanceRpsLimit": 500
                    },
                    "ServiceName": "blueszzhang-model-test-final",
                    "ServicePort": null,
                    "ServiceType": "MACHINE_LEARNING",
                    "Status": "NEW",
                    "TiOneServiceGroupId": null,
                    "TiOneServiceId": null,
                    "UpdateTime": "2025-10-16T14:00:55",
                    "Version": 1,
                    "Weight": null,
                    "WorkloadStatus": null
                }
            ],
            "Status": "NEW",
            "TiOneServiceGroupId": null,
            "UpdateTime": "2025-10-16T14:00:55",
            "WeightUpdateStatus": null
        },
        "RequestId": "8cf81a59-d68a-4997-ad20-e244c47075fd"
    }
}
```

