**Example 1: 创建模型服务**



Input: 

```
tccli tse CreateCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-******** \
    --Name qwen \
    --ServiceType LLMService \
    --ModelProvider qwen \
    --ModelProtocol OpenAI-Qwen \
    --ModelSelector PassThrough \
    --SecretKeyIds secret-de0acbccee344b \
    --EnableModelParamCheck False \
    --UpstreamURL https://dashscope.aliyuncs.com \
    --SourceId cls-********
```

Output: 
```
{
    "Response": {
        "ModelServiceId": "843a043a19d445a8a27e5be0fd182a0c",
        "Result": true,
        "RequestId": "d7e3ffad-4d6d-42fd-b2f5-6c3c81f294a0"
    }
}
```

