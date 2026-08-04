**Example 1: 创建 PassThrough 模式的 LLM 模型服务**

创建一个透传模式的 LLM 模型服务，ModelSelector 为 PassThrough，开启模型参数校验

Input: 

```
tccli cngw CreateCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-aeb0be15 \
    --Name openai-service \
    --ServiceType LLMService \
    --ModelProvider OpenAI \
    --ModelProtocol OpenAI/v1 \
    --ModelSelector PassThrough \
    --SecretKeyIds secret-f4e97d19d1e876 \
    --EnableModelParamCheck True \
    --ModelParamCheckRule.AllowModelList gpt-5.1 gpt-5-mini \
    --ModelParamCheckRule.ModelValidationFailureStrategy Return404 \
    --Description OpenAI 透传模型服务 \
    --UpstreamURL https://api.openai.com \
    --ConnectTimeout 10000 \
    --WriteTimeout 60000 \
    --ReadTimeout 60000 \
    --Retries 0
```

Output: 
```
{
    "Response": {
        "Result": true,
        "ModelServiceId": "ms-84cnfq44",
        "RequestId": "550e8400-e29b-41d4-a716-446655440000"
    }
}
```

**Example 2: 创建 Specify 模式的 LLM 模型服务（含模型降级）**

创建一个指定模型模式的 LLM 模型服务，配置默认模型和模型降级规则

Input: 

```
tccli cngw CreateCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-aeb0be15 \
    --Name anthropic-claude-service \
    --ServiceType LLMService \
    --ModelProvider Anthropic \
    --ModelProtocol Anthropic/v1 \
    --ModelSelector Specify \
    --DefaultModel claude-sonnet-4-20250514 \
    --EnableModelFallback True \
    --ModelFallbackRule.FallbackModels claude-3-5-haiku-20241022 claude-opus-4-20250514 \
    --Description Anthropic Claude 模型服务 \
    --UpstreamURL https://api.anthropic.com \
    --ConnectTimeout 10000 \
    --WriteTimeout 60000 \
    --ReadTimeout 60000 \
    --Retries 1 \
    --QuotaLimit.RPMLimit 0 \
    --QuotaLimit.TPMLimit 0 \
    --QuotaLimit.ConcurrentCountLimit 20
```

Output: 
```
{
    "Response": {
        "Result": true,
        "ModelServiceId": "ms-abcdef123456",
        "RequestId": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
    }
}
```

