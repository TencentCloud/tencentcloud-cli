**Example 1: 查询 LLM 模型 API 列表**

查询网关下所有 LLM 模型 API，支持按名称模糊搜索和过滤。

Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMModelAPIs --cli-unfold-argument  \
    --GatewayId gateway-9a766f25 \
    --SecretKeyId secret-8fe776ce194dab
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "BasePath": "/x",
                    "CreateTime": "2026-08-14 21:29:19",
                    "Description": "",
                    "EnableCrossServiceFallback": false,
                    "Id": "c733a200d1c14f53b9fa81a3bb6008fa",
                    "LogConfig": {
                        "EnableRequestLogPayloads": false,
                        "EnableResponseLogPayloads": false,
                        "RequestLogPayloadMaxSize": 8192,
                        "RequestLogPayloadMode": "raw",
                        "RequestLogPayloadTruncationPolicy": "Bounded",
                        "ResponseLogPayloadMaxSize": 8192,
                        "ResponseLogPayloadMode": "raw",
                        "ResponseLogPayloadTruncationPolicy": "Bounded"
                    },
                    "MaxDocumentsConfig": {
                        "EnableMaxDocuments": false,
                        "MaxDocumentValue": 0
                    },
                    "ModelServiceId": "c7e480f4bea0437085b224d1b7db23d2",
                    "ModelServiceName": "deep-x02",
                    "ModelServiceRoute": {
                        "SelectedTypes": [
                            "Weighted"
                        ],
                        "WeightedConfig": [
                            {
                                "ModelServiceId": "5168ae1f1ba440e396251a95ea61e4e9",
                                "Weight": 30
                            }
                        ]
                    },
                    "ModifyTime": "2026-08-14 21:33:16",
                    "Name": "deep-x",
                    "RequestProtocol": "openai",
                    "RouteList": [
                        {
                            "Methods": [
                                "POST"
                            ],
                            "Name": "base",
                            "Paths": [
                                "/v1/chat/completions"
                            ]
                        }
                    ],
                    "SceneType": "Chat",
                    "SecretKeyModelScopes": [
                        {
                            "EffectiveModelNames": [
                                "deepseek-v4-flash"
                            ],
                            "ModelScope": {
                                "AllowList": [
                                    "deepseek-v4-flash"
                                ],
                                "ScopeType": "ALLOWLIST"
                            },
                            "PrincipalId": "secret-8fe776ce194dab",
                            "PrincipalName": "deep-sk"
                        }
                    ],
                    "StripPath": true
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "4d827ae9-c629-42f2-9992-f00c1d83c722"
    }
}
```

