**Example 1: 创建 AI 网关模型 API**



Input: 

```
tccli tse CreateCloudNativeAPIGatewayLLMModelAPI --cli-unfold-argument  \
    --GatewayId gateway-4eb46023 \
    --Name ModelAPI-Hunyuan \
    --SceneType Chat \
    --RequestProtocol OpenAI \
    --ListModelServiceId 1006154d-8770-xx \
    --RouteList.0.Name base \
    --RouteList.0.Paths /v1/chat/completions \
    --BasePath /qq \
    --Description OpenAI协议LLM接口
```

Output: 
```
{
    "Response": {
        "RequestId": "b9b49623-c235-4839-b1d6-1f6f23ae8dcd",
        "Result": true,
        "ModelAPIId": "9006154d-8770-xx"
    }
}
```

