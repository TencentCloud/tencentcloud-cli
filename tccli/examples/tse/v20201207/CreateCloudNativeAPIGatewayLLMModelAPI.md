**Example 1: 正常**



Input: 

```
tccli tse CreateCloudNativeAPIGatewayLLMModelAPI --cli-unfold-argument  \
    --GatewayId gateway-ad373895 \
    --Name klklklklkdfadfasdfa \
    --SceneType Chat \
    --RequestProtocol openai \
    --ListModelServiceId 950a45404f214b779224861333471ba4 \
    --RouteList.0.Name base \
    --RouteList.0.Methods POST \
    --RouteList.0.Paths /v1/chat/completions \
    --BasePath /klklklfadfadsfadsf \
    --EnableCrossServiceFallback False \
    --LogConfig.EnableRequestLogPayloads False \
    --LogConfig.EnableResponseLogPayloads False \
    --SensitiveWordRoute.Enabled False \
    --SensitiveWordRoute.StandardModelName claude-haiku-4-5 \
    --PriorityScheduleConfig.Enabled True \
    --ModelNameRoute.ModelNames claude-haiku-4-5 \
    --StandardModelName claude-haiku-4-5
```

Output: 
```
{
    "Response": {
        "ModelAPIId": "de9adcc59aa54394ae7318bdf11a77c9",
        "Result": true,
        "RequestId": "97e2a048-2f31-4ec7-b513-70beef815519"
    }
}
```

