**Example 1: 修改模型API**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayLLMModelAPI --cli-unfold-argument  \
    --GatewayId gateway-bb346e76 \
    --ModelAPIId cae62c8faa894a93b48c4dcfe4a8c80e \
    --Name modelapi \
    --BasePath /basepath2 \
    --Description  \
    --ListModelServiceId c6549138344a463a87ae091127471bbe \
    --ModelServiceRoute.SelectedTypes ModelName \
    --ModelServiceRoute.ModelNameConfig.0.ModelServiceId c6549138344a463a87ae091127471bbe \
    --ModelServiceRoute.ModelNameConfig.0.MatchModelName * \
    --EnableCrossServiceFallback False \
    --LogConfig.EnableRequestLogPayloads False \
    --LogConfig.EnableResponseLogPayloads False
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "a8f3bd5a-253a-45c8-b208-e8e13d96f580"
    }
}
```

