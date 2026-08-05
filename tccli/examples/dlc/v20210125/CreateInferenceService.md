**Example 1: 创建推理服务（含默认部署）**



Input: 

```
tccli dlc CreateInferenceService --cli-unfold-argument  \
    --Name xxxteste \
    --ModelUid m-qwen2-5-6a1d83a2-db4d \
    --Engine vllm \
    --Replicas 1 \
    --ResourcePartitionId dlc-p-mghaaeha \
    --Image ccr.ccs.tencentyun.com/emr-image/tcray:3.0.0.dev0-py311-cu125-extra-xgboost \
    --ModelIdentifier m-qwen2-5-1234567 \
    --Queue default
```

Output: 
```
{
    "Response": {
        "ApiKeyAuthEnabled": true,
        "ApiKeyAuthForceEnabled": true,
        "ApiKeyBindMessage": "success",
        "AppId": 260200066,
        "CreateTime": 1780731457322,
        "DeploymentCount": 1,
        "EndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443/service/xxxteste/v1",
        "HasRunningDeployment": false,
        "ModelIdentifier": "m-qwen2-5-1234567",
        "ModelName": "qwen2.5",
        "ModelType": "LLM",
        "ModelUid": "m-qwen2-5-6a1d83a2-db4d",
        "ModelVersion": "v1",
        "Name": "xxxteste",
        "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_gn7_gn75xlarge80\",\"workerSpec\":1,\"headBillingItem\":\"sv_dlc_gn7_gn75xlarge80\",\"headSpec\":1,\"gpu\":\"T4\",\"gpuNum\":1,\"cpu\":20,\"mem\":80,\"headCpu\":20,\"headMem\":80}",
        "ServiceId": "svc-20260606153737-53cr",
        "SkipTlsVerify": false,
        "Status": "Deploying",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UnifiedEndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443/v1",
        "UpdateTime": 1780731457580,
        "RequestId": "c7aaa137-69a2-4514-a8ed-29b977c9f040"
    }
}
```

