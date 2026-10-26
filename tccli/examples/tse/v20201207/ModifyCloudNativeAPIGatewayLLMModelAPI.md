**Example 1: 修改成功**



Input: 

```
tccli tse ModifyCloudNativeAPIGatewayLLMModelAPI --cli-unfold-argument  \
    --GatewayId gateway-ad373895 \
    --ModelAPIId fa4525b78d364cd2ac4540fe3dbcb7f1 \
    --Name multi-weight \
    --BasePath /weight \
    --Description  \
    --ListModelServiceId 39bced9f01d3462e903d1a5ba8f9221e \
    --ModelServiceRoute.SelectedTypes Weighted \
    --ModelServiceRoute.WeightedConfig.0.ModelServiceId 39bced9f01d3462e903d1a5ba8f9221e \
    --ModelServiceRoute.WeightedConfig.0.Weight 10 \
    --ModelServiceRoute.WeightedConfig.0.StandardModelName claude-haiku-4-5 \
    --EnableCrossServiceFallback False \
    --LogConfig.EnableRequestLogPayloads False \
    --LogConfig.EnableResponseLogPayloads False \
    --SensitiveWordRoute.Enabled True \
    --SensitiveWordRoute.ModelServiceRefs b14f1d835fe240d593c9d0befd31aacc \
    --SensitiveWordRoute.StandardModelName claude-haiku-4-5 \
    --StandardModelName claude-haiku-4-5
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "5ce87fdb-9260-4cb8-8d83-7f2973ecab07"
    }
}
```

