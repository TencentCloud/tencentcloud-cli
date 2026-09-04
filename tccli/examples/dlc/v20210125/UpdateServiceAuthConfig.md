**Example 1: 更新推理服务的 API-Key 鉴权配置**



Input: 

```
tccli dlc UpdateServiceAuthConfig --cli-unfold-argument  \
    --ServiceId svc-20260606145826-3tlg \
    --ApiKeyAuthEnabled True
```

Output: 
```
{
    "Response": {
        "ApiKeyAuthEnabled": true,
        "ApiKeyAuthForceEnabled": true,
        "AppId": 260200066,
        "CreateTime": 1780729106761,
        "DeploymentCount": 1,
        "EndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443/service/test-qwen35/v1",
        "HasRunningDeployment": false,
        "ModelIdentifier": "qwen35-4b",
        "ModelName": "Qwen3.5-4B",
        "ModelType": "LLM",
        "ModelUid": "m-qwen3-5-4b-6a223aba-951c",
        "ModelVersion": "v1",
        "Name": "test-qwen35",
        "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_gn7_gn75xlarge80\",\"workerSpec\":1,\"headBillingItem\":\"sv_dlc_postpay_cu_standard_cu\",\"headSpec\":1,\"gpu\":\"T4\",\"gpuNum\":1,\"cpu\":20,\"mem\":80,\"headCpu\":1,\"headMem\":4}",
        "ServiceId": "svc-20260606145826-3tlg",
        "SkipTlsVerify": false,
        "Status": "Stopped",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UnifiedEndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443/v1",
        "UpdateTime": 1780731592425,
        "RequestId": "98dc439b-5f14-4bd4-be62-605c51609f23"
    }
}
```

