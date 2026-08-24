**Example 1: 创建成功**



Input: 

```
tccli tse CreateCloudNativeAPIGatewayLLMModelAPI --cli-unfold-argument  \
    --GatewayId gateway-50c27c7d \
    --Name test-qwen-openai-2-anthropic-1 \
    --SceneType Chat \
    --RequestProtocol openai \
    --ListModelServiceId e2cf2576114348ec9cc6fbf52358e180 \
    --RouteList.0.Name base \
    --RouteList.0.Methods POST \
    --RouteList.0.Paths /v1/chat/completions \
    --BasePath /qwen1 \
    --EnableCrossServiceFallback False \
    --LogConfig.EnableRequestLogPayloads False \
    --LogConfig.EnableResponseLogPayloads False
```

Output: 
```
{
    "Response": {
        "ModelAPIId": "c565b61e67c64c35b9e4600758bb3f4c",
        "Result": true,
        "RequestId": "9eb31679-b192-40df-90c6-2fbfb1e0527c"
    }
}
```

