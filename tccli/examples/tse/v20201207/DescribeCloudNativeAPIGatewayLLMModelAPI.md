**Example 1: 查询单个 LLM 模型 API 信息**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayLLMModelAPI --cli-unfold-argument  \
    --GatewayId gateway-4eb46023 \
    --ModelAPIId a1b2c3d4e5f6789012345678901234ab
```

Output: 
```
{
    "Response": {
        "Result": {
            "Id": "a1b2c3d4e5f6789012345678901234ab",
            "CreateTime": "2026-05-19T15:00:00+08:00",
            "ModifyTime": "2026-05-19T15:00:00+08:00",
            "Name": "openai_chat",
            "SceneType": "Chat",
            "RequestProtocol": "openai",
            "RouteList": [
                {
                    "Name": "openai_chat_route_1",
                    "Methods": [
                        "POST"
                    ],
                    "Paths": [
                        "/v1/chat/completions"
                    ]
                }
            ],
            "BasePath": "/v1/openai",
            "StripPath": false,
            "Description": "大模型统一聊天 API",
            "ModelServiceId": "d0742b86605340438a8018c658156622",
            "ModelServiceName": "openai_test",
            "MatchHeaders": [],
            "EnableCrossServiceFallback": false
        },
        "RequestId": "f1234567-89ab-cdef-0123-456789abcdef"
    }
}
```

