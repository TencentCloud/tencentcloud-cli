**Example 1: 停止推理服务（停止所有部署）**



Input: 

```
tccli dlc StopInferenceService --cli-unfold-argument  \
    --ServiceId svc-20260606145826-3tlg
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
        "UpdateTime": 1780731592421,
        "RequestId": "f6f0df44-598b-47d7-8bc1-896f524fe26c"
    }
}
```

