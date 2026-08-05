**Example 1: 列出推理服务**



Input: 

```
tccli dlc ListInferenceServices --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10 \
    --StartTime 1780934400000 \
    --EndTime 1781539199000
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ApiKeyAuthEnabled": true,
                "ApiKeyAuthForceEnabled": true,
                "AppId": 260200066,
                "CpuResourceSummary": {
                    "Replicas": 2,
                    "TotalCpuCores": 4,
                    "TotalMemoryGB": 16
                },
                "CreateTime": 1781514197876,
                "DeploymentCount": 2,
                "EndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443/service/qzzhu_061503",
                "GpuResourceSummary": [],
                "HasRunningDeployment": true,
                "ModelIdentifier": "qzzhu_061503",
                "ModelName": "xgboost",
                "ModelType": "ML",
                "ModelUid": "m-xgboost-6a159272-99b2",
                "ModelVersion": "v1",
                "Name": "qzzhu_061503",
                "RayDashboardUrl": "https://cls-p9d8s1gc.tcray-gateway.ap-guangzhou.cloud.tencent.com:443/dlc-p-zntmtydc/rayserve-20260615170317-5xex-dshzh/",
                "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"workerSpec\":1,\"headBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"headSpec\":1,\"gpu\":\"\",\"gpuNum\":0,\"cpu\":1,\"mem\":4,\"headCpu\":1,\"headMem\":4}",
                "ServiceId": "svc-20260615170317-kt6r",
                "SkipTlsVerify": false,
                "Status": "Running",
                "SubAccountUin": "700002655694",
                "Uin": "700002655694",
                "UnifiedV2EndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443",
                "UpdateTime": 1781514198038
            }
        ],
        "Page": 1,
        "PageSize": 10,
        "Total": 25,
        "TotalPages": 3,
        "RequestId": "35228c7d-f3a5-4fae-a9a0-bb43ab5130ac"
    }
}
```

