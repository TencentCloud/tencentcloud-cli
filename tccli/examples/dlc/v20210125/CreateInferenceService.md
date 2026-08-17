**Example 1: 示例**



Input: 

```
tccli dlc CreateInferenceService --cli-unfold-argument  \
    --Name aaasss \
    --ModelUid thisismodelUid \
    --Engine xgboost \
    --Replicas 1 \
    --ResourcePartitionId dlc-p-jhzmcfna \
    --Image aasssss \
    --ModelIdentifier thisismodelUid \
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
        "CreateTime": 1786007739628,
        "DeploymentCount": 1,
        "DeploymentMode": "ModelHub",
        "EndpointUrl": "https://cls-p9d8s1gc.tcray-gateway.ap-guangzhou.cloud.tencent.com:443/service/aaasss",
        "HasRunningDeployment": false,
        "IsCustom": false,
        "ModelIdentifier": "thisismodelUid",
        "ModelName": "capi_test_123",
        "ModelType": "ML",
        "ModelUid": "thisismodelUid",
        "ModelVersion": "v1",
        "Name": "aaasss",
        "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"workerSpec\":1,\"headBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"headSpec\":1,\"gpu\":\"\",\"gpuNum\":0,\"cpu\":1,\"mem\":4,\"headCpu\":1,\"headMem\":4}",
        "ResourceTags": [],
        "ServiceId": "svc-20260806171539-3iwd",
        "SkipTlsVerify": false,
        "Status": "Deploying",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UnifiedV2EndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443",
        "UpdateTime": 1786007739788,
        "RequestId": "7bcb5817-ad24-42e8-a5f3-e78e25714e80"
    }
}
```

