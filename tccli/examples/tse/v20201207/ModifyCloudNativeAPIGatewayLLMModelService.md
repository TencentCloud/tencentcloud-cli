**Example 1: 修改模型服务**



Input: 

```
tccli tse ModifyCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-9a766f25 \
    --ModelServiceId 9f3d5fe7413a489cb9f13c84d10d5fd9 \
    --Name dp-test-x \
    --DefaultModel deepseek-v4-pro \
    --ModelSelector Specify \
    --EnableModelFallback False \
    --EnableModelParamCheck False \
    --UpstreamURL https://api.deepseek.com \
    --ConnectTimeout 10000 \
    --WriteTimeout 60000 \
    --ReadTimeout 60000 \
    --UpstreamUrlMode AutoConcat \
    --KeyRotationEnabled True \
    --KeyRotationPeriodDays 9
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "153b86f2-7fb8-48dd-8e85-c697f68c9977"
    }
}
```

