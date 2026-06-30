**Example 1: 修改模型服务**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-01f976d0 \
    --ModelServiceId 843a043a19d445a8a27e5be0fd182a0c \
    --Name qwen \
    --ModelSelector PassThrough \
    --EnableModelParamCheck False \
    --Description  \
    --UpstreamURL https://dashscope.aliyuncs.com
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "ec1c252b-1306-42d5-9ad1-368f76aade3f"
    }
}
```

