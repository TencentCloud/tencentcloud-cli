**Example 1: 重启推理服务（重启所有部署）**



Input: 

```
tccli dlc RestartInferenceService --cli-unfold-argument  \
    --ServiceId svc-20260615170317-kt6r
```

Output: 
```
{
    "Response": {
        "ApiKeyAuthEnabled": true,
        "ApiKeyAuthForceEnabled": true,
        "AppId": 260200066,
        "CreateTime": 1781514197876,
        "DeploymentCount": 2,
        "EndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443/service/qzzhu_061503",
        "HasRunningDeployment": false,
        "ModelIdentifier": "qzzhu_061503",
        "ModelName": "xgboost",
        "ModelType": "ML",
        "ModelUid": "m-xgboost-6a159272-99b2",
        "ModelVersion": "v1",
        "Name": "qzzhu_061503",
        "ResourceConfig": "{\"workerBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"workerSpec\":1,\"headBillingItem\":\"sv_dlc_standard_cu_standard_cu\",\"headSpec\":1,\"gpu\":\"\",\"gpuNum\":0,\"cpu\":1,\"mem\":4,\"headCpu\":1,\"headMem\":4}",
        "ServiceId": "svc-20260615170317-kt6r",
        "SkipTlsVerify": false,
        "Status": "Deploying",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UnifiedV2EndpointUrl": "https://tcray-gateway.ap-guangzhou.cloud.tencent.com:443",
        "UpdateTime": 1781523710617,
        "RequestId": "bf8066df-d560-49d0-8d44-cc65a87f2792"
    }
}
```

