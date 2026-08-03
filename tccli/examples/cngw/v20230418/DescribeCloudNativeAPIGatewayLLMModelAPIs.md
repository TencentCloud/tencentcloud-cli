**Example 1: 查询 LLM 模型 API 列表**

查询网关下所有 LLM 模型 API，支持按名称模糊搜索和过滤。

Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMModelAPIs --cli-unfold-argument  \
    --GatewayId gateway-04b00666 \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Name Name \
    --Filters.0.Values openai \
    --Keyword openai
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
                    "Id": "gpt4-model-api-id-xxxxxxxxxx",
                    "ModifyTime": "2025-11-26 10:16:59",
                    "Name": "openai_chat_gpt4",
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
                    "Id": "claude-model-api-id-xxxxxxxxxx",
                    "ModifyTime": "2025-11-26 10:16:16",
                    "Name": "openai_chat_claude",
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
                    "Id": "gemini-model-api-id-xxxxxxxxxx",
                    "ModifyTime": "2025-11-26 10:15:18",
                    "Name": "openai_chat_gemini",
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
                    "Id": "deepseek-model-api-id-xxxxxxxxxx",
                    "ModifyTime": "2025-11-26 10:13:16",
                    "Name": "openai_chat_deepseek",
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

