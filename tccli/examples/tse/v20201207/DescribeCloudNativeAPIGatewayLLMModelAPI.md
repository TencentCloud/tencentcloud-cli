**Example 1: 查询单个 LLM 模型 API 信息**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayLLMModelAPI --cli-unfold-argument  \
    --GatewayId gateway-04b00666 \
    --ModelAPIId 769ebd672acb4640b0a35a31bd429de9
```

Output: 
```
{
    "Response": {
        "RequestId": "48dddba4-5fa4-45ee-a026-d53333e275f0",
        "Result": {
            "BasePath": "/base",
            "CreateTime": "2025-11-26 10:16:16",
            "Description": "OpenAI 格式模型 API",
            "Id": "769ebd672acb4640b0a35a31bd429de9",
            "ModifyTime": "2025-11-26 10:16:16",
            "Name": "openai_chat_测试3",
            "RequestProtocol": "OpenAI",
            "RouteList": [
                {
                    "Paths": [
                        "/v1/chat/completions"
                    ]
                }
            ],
            "SceneType": "Chat",
            "StripPath": true
        }
    }
}
```

