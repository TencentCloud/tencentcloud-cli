**Example 1: 查询 LLM 模型 API 列表**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayLLMModelAPIs --cli-unfold-argument  \
    --GatewayId gateway-04b00666 \
    --Limit 10 \
    --Offset None \
    --Filters.0.Name Name \
    --Filters.0.Values openai \
    --Keyword openai \
    --ConsumerId 048e0c69-ffb2-4ec7-aaaa-97c1e11f****
```

Output: 
```
{
    "Response": {
        "RequestId": "959caf3b-f74c-4cd1-9260-3b7713e55604",
        "Result": {
            "DataList": [
                {
                    "BasePath": "",
                    "CreateTime": "2025-11-26 10:16:59",
                    "Description": "OpenAI 格式模型 API",
                    "Id": "9ab0f08a1bab42699c85839fda1461c1",
                    "ModifyTime": "2025-11-26 10:16:59",
                    "Name": "openai_chat_测试4",
                    "RequestProtocol": "OpenAI",
                    "RouteList": [
                        {
                            "Name": "base",
                            "Paths": [
                                "/v1/chat/completions"
                            ]
                        }
                    ],
                    "SceneType": "Chat",
                    "StripPath": false
                },
                {
                    "BasePath": "/base",
                    "CreateTime": "2025-11-26 10:16:16",
                    "Description": "OpenAI 格式模型 API",
                    "Id": "769ebd672acb4640b0a35a31bd429de9",
                    "ModifyTime": "2025-11-26 10:16:16",
                    "Name": "openai_chat_测试3",
                    "RequestProtocol": "OpenAI",
                    "RouteList": [
                        {
                            "Name": "base",
                            "Paths": [
                                "/v1/chat/completions"
                            ]
                        }
                    ],
                    "SceneType": "Chat",
                    "StripPath": true
                },
                {
                    "BasePath": "",
                    "CreateTime": "2025-11-26 10:15:18",
                    "Description": "OpenAI 格式模型 API",
                    "Id": "66ae5965beed4196966876a778c28995",
                    "ModifyTime": "2025-11-26 10:15:18",
                    "Name": "openai_chat_测试2",
                    "RequestProtocol": "OpenAI",
                    "RouteList": [
                        {
                            "Name": "base",
                            "Paths": [
                                "/v1/chat/completions"
                            ]
                        }
                    ],
                    "SceneType": "Chat",
                    "StripPath": false
                },
                {
                    "BasePath": "",
                    "CreateTime": "2025-11-26 10:13:16",
                    "Description": "OpenAI 格式模型 API",
                    "Id": "b529dd8141ea4234a4c4d87930108f68",
                    "ModifyTime": "2025-11-26 10:13:16",
                    "Name": "openai_chat_测试",
                    "RequestProtocol": "OpenAI",
                    "RouteList": [
                        {
                            "Name": "base",
                            "Paths": [
                                "/v1/chat/completions"
                            ]
                        }
                    ],
                    "SceneType": "Chat",
                    "StripPath": false
                }
            ],
            "TotalCount": 4
        }
    }
}
```

