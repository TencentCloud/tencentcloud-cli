**Example 1: 获取指定会话的会话交互结果**



Input: 

```
tccli ccc DescribeAICallInteractionRecords --cli-unfold-argument  \
    --SdkAppId 1500098925 \
    --SessionId ac0726e8-018b-4f9d-9d15-004a4c349cd5
```

Output: 
```
{
    "Response": {
        "InteractionEventList": [
            {
                "Messages": [
                    {
                        "AISpeak": {
                            "CanBeInterrupted": false,
                            "LatencyMetrics": {
                                "AsrLatency": -1,
                                "LLMFirstTokenLatency": 41,
                                "TTSLatency": 255,
                                "TotalLatency": 306
                            },
                            "SpokenText": "您好，我是腾讯汽车的，这边儿看到您在关注腾讯比亚迪车型，刚好这两天店里有试驾活动，您看这周或下周有空来门店试驾详谈吗？",
                            "SpokenType": "Script"
                        },
                        "Timestamp": 1784166669089
                    }
                ],
                "Paths": [
                    {
                        "NodeName": "开场白",
                        "NodeType": "DIALOGUE",
                        "Timestamp": 1784166668940
                    }
                ],
                "RoundId": "95bcce08-5c94-43c3-8ed5-e678db41d9bf",
                "RoundIndex": 1
            },
            {
                "Messages": [
                    {
                        "Timestamp": 1784166685178,
                        "UserReply": {
                            "ASRTranscript": "嗯，好的",
                            "BranchType": "Intent",
                            "ExtractedSlots": "[{\"TagName\":\"city\",\"TagValue\":\"深圳\",\"TagType\":3}]",
                            "MatchedIntent": "客户给出了方便看车的时间或者同意到店看车"
                        }
                    },
                    {
                        "AISpeak": {
                            "CanBeInterrupted": true,
                            "LatencyMetrics": {
                                "AsrLatency": 727,
                                "LLMFirstTokenLatency": 954,
                                "TTSLatency": 258,
                                "TotalLatency": 2127
                            },
                            "SpokenText": "好的，看到您是想在深圳看车，我们让这边儿的门店和您联系，可以吧？",
                            "SpokenType": "Other"
                        },
                        "Timestamp": 1784166687141
                    }
                ],
                "Paths": [
                    {
                        "NodeName": "开场白",
                        "NodeType": "DIALOGUE",
                        "Timestamp": 1784166685942
                    },
                    {
                        "NodeName": "确认方便的时间与城市",
                        "NodeType": "DIALOGUE",
                        "Timestamp": 1784166685942
                    },
                    {
                        "APICall": {
                            "Async": false,
                            "Attempts": [
                                {
                                    "CostMS": 3000,
                                    "ErrorType": "timeout",
                                    "Index": 1,
                                    "Request": {
                                        "Headers": "{\"Authorization\":\"***456789\",\"Content-Type\":\"application/json\"}",
                                        "Method": "POST",
                                        "Params": "{\"city\":\"深圳\"}",
                                        "URL": "https://example.com/api/store/assign"
                                    },
                                    "Status": "unreachable",
                                    "Summary": "timeout：context deadline exceeded",
                                    "Timestamp": 1784166687200
                                },
                                {
                                    "CostMS": 155,
                                    "Index": 2,
                                    "Request": {
                                        "Headers": "{\"Authorization\":\"***456789\",\"Content-Type\":\"application/json\"}",
                                        "Method": "POST",
                                        "Params": "{\"city\":\"深圳\"}",
                                        "URL": "https://example.com/api/store/assign"
                                    },
                                    "Response": {
                                        "Body": "{\"code\":0,\"data\":{\"storeName\":\"深圳南山店\"}}",
                                        "Headers": "{\"Content-Type\":\"application/json\"}",
                                        "StatusCode": 200
                                    },
                                    "Status": "success",
                                    "StatusCode": 200,
                                    "Timestamp": 1784166690300
                                }
                            ],
                            "CostMS": 3155,
                            "RetryCount": 1,
                            "Status": "success",
                            "StatusCode": 200
                        },
                        "NodeName": "分配门店",
                        "NodeType": "API_CALL",
                        "Timestamp": 1784166687190
                    }
                ],
                "RoundId": "1522ea24-5102-475a-9a5e-f08ecaa07cc8",
                "RoundIndex": 2
            }
        ],
        "RequestId": "de6e0a7d-0723-4e79-86ea-1faf25e5fe69"
    }
}
```

