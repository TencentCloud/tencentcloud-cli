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
                            "CanBeInterrupted": true,
                            "LatencyMetrics": {
                                "AsrLatency": -1,
                                "LLMFirstTokenLatency": 29,
                                "TTSLatency": 295,
                                "TotalLatency": 329
                            },
                            "SpokenText": "xiaopan为您服务，售前请说 123，售后请说 456",
                            "SpokenType": "Script"
                        },
                        "Timestamp": 1774931367634
                    }
                ],
                "Paths": [
                    {
                        "NodeName": "对话 1",
                        "NodeType": "DIALOGUE",
                        "Timestamp": 1774931367607
                    }
                ],
                "RoundId": "6418f9b0-fbbc-4063-8b6f-ec11f7599c14",
                "RoundIndex": 1
            }
        ],
        "RequestId": "bb532c51-cfa4-41f3-a9e9-bd8506ec26f1"
    }
}
```

