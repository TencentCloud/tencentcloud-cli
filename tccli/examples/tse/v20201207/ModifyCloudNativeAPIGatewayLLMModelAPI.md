**Example 1: 修改模型 API**

修改模型 API

Input: 

```
tccli tse ModifyCloudNativeAPIGatewayLLMModelAPI --cli-unfold-argument  \
    --GatewayId gateway-2abb07bf \
    --ModelAPIId 323e58bceacf4128823c60c93bbe9ca1 \
    --Name test1 \
    --BasePath /test1 \
    --Description  \
    --EnableCrossServiceFallback True \
    --CrossServiceFallbackConfig.TriggerConditions ServiceUnavailable \
    --CrossServiceFallbackConfig.FallbackServiceChain.0.ModelServiceId 3dcaac5d48cc4d39a8ed79937fe720c6
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "9b9acb5f-9230-4a4b-abcb-180211952df0"
    }
}
```

