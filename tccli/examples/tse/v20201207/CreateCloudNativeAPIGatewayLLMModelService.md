**Example 1: 创建模型服务**



Input: 

```
tccli tse CreateCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-aeb0be15 \
    --Name qwen \
    --ServiceType LLMService \
    --ModelProvider qwen \
    --ModelProtocol OpenAI-Qwen \
    --ModelSelector PassThrough \
    --SecretKeyIds secret-de0acbccee344b \
    --EnableModelParamCheck False \
    --UpstreamURL https://dashscope.aliyuncs.com \
    --SourceId cls-mn2lq8hp
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

**Example 2: 创建模型服务并关闭上游压缩协商**

为 deepseek 创建指定模型的 LLM 模型服务，并请求上游返回未压缩响应。

Input: 

```
tccli tse CreateCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-aeb0be15 \
    --Name deepseek-sse \
    --ServiceType LLMService \
    --ModelProvider deepseek \
    --ModelProtocol OpenAI/V1 \
    --ModelSelector Specify \
    --DefaultModel deepseek-chat \
    --UpstreamURL https://api.deepseek.com
```

Output: 
```
{
    "Response": {
        "Result": true,
        "ModelServiceId": "model-service-123",
        "RequestId": "req-123"
    }
}
```

