**Example 1: 获取单个推理服务详情**



Input: 

```
tccli dlc GetInferenceService --cli-unfold-argument  \
    --ServiceId svc-20260609105932-vebf
```

Output: 
```
{
    "Response": {
        "ApiKeyAuthEnabled": true,
        "ApiKeyAuthForceEnabled": true,
        "AppId": 260200066,
        "CreateTime": 1780973972980,
        "DeploymentCount": 1,
        "EndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443/service/m-bge-v2-m3-test/v1",
        "GpuResourceSummary": [],
        "HasRunningDeployment": true,
        "ModelIdentifier": "m-bge-v2-m3",
        "ModelName": "bge-reranker-v2-m3",
        "ModelType": "Reranker",
        "ModelUid": "m-bge-reranker-v2-m3-6a223aba-2e20",
        "ModelVersion": "v1",
        "Name": "m-bge-v2-m3-test",
        "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_gn7_gn75xlarge80\",\"workerSpec\":1,\"headBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"headSpec\":1,\"gpu\":\"T4\",\"gpuNum\":1,\"cpu\":20,\"mem\":80,\"headCpu\":1,\"headMem\":4}",
        "ServiceId": "svc-20260609105932-vebf",
        "SkipTlsVerify": false,
        "Status": "Running",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UnifiedEndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443/v1",
        "UpdateTime": 1780989802316,
        "RequestId": "c51e5952-83eb-4ec4-a74a-eea345dc99a5"
    }
}
```

