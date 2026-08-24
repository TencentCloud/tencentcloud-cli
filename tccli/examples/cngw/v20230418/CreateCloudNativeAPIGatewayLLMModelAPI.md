**Example 1: 创建模型API**



Input: 

```
tccli cngw CreateCloudNativeAPIGatewayLLMModelAPI --cli-unfold-argument  \
    --GatewayId gateway-bb346e76 \
    --Name modelapi \
    --SceneType Chat \
    --RequestProtocol openai \
    --ListModelServiceId c6549138344a463a87ae091127471bbe \
    --RouteList.0.Name base \
    --RouteList.0.Methods POST \
    --RouteList.0.Paths /v1/chat/completions \
    --BasePath /basepath \
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
        "ModelAPIId": "cae62c8faa894a93b48c4dcfe4a8c80e",
        "Result": true,
        "RequestId": "19c52064-af4e-477e-8353-9fc2cc6a0df7"
    }
}
```

