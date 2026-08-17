**Example 1: 示例**



Input: 

```
tccli dlc GetInferenceService --cli-unfold-argument  \
    --ServiceId svc-20260731164626-fgja
```

Output: 
```
{
    "Response": {
        "ApiKeyAuthEnabled": true,
        "ApiKeyAuthForceEnabled": true,
        "AppId": 260200066,
        "CpuResourceSummary": {
            "Replicas": 2,
            "TotalCpuCores": 6,
            "TotalMemoryGB": 24
        },
        "CreateTime": 1785487586929,
        "DeploymentCount": 2,
        "DeploymentMode": "ModelHub",
        "EndpointUrl": "https://cls-p9d8s1gc.tcray-gateway.ap-guangzhou.cloud.tencent.com:443/service/m-chronos-2-6a2812f7-5ed6-2026073116-svc",
        "GpuResourceSummary": [],
        "HasRunningDeployment": true,
        "IsCustom": false,
        "ModelIdentifier": "m-chronos-2-6a2812f7-5ed6-2026073116-v1",
        "ModelName": "Chronos-2",
        "ModelType": "TimeSeries",
        "ModelUid": "m-chronos-2-6a2812f7-5ed6",
        "ModelVersion": "v1",
        "Name": "m-chronos-2-6a2812f7-5ed6-2026073116-svc",
        "RayDashboardUrl": "https://cls-p9d8s1gc.tcray-gateway.ap-guangzhou.cloud.tencent.com:443/dlc-p-jhzmcfna/rayserve-20260805203359-r2b7-9jkhq/",
        "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"workerSpec\":2,\"headBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"headSpec\":1,\"gpu\":\"\",\"gpuNum\":0,\"cpu\":2,\"mem\":8,\"headCpu\":1,\"headMem\":4}",
        "ResourceTags": [],
        "ServiceId": "svc-20260731164626-fgja",
        "SkipTlsVerify": false,
        "Status": "Running",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UnifiedV2EndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443",
        "UpdateTime": 1785487587084,
        "RequestId": "6279f479-8710-418a-ac18-76a5cc8be3db"
    }
}
```

