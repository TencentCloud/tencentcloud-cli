**Example 1: 获取 AI 呼叫时延信息**

获取 AI 呼叫时延信息

Input: 

```
tccli ccc DescribeAILatency --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SessionId adcf61b8-dbb9-4c20-87bf-c0744c04bade \
    --StartTime 1737350008 \
    --EndTime 1737356008
```

Output: 
```
{
    "Response": {
        "AILatencyStatistics": {
            "ASRLatency": {
                "MiddleLatency": 308,
                "MinLatency": 267,
                "P90Latency": 338
            },
            "ETELatency": {
                "MiddleLatency": 1327,
                "MinLatency": 1209,
                "P90Latency": 1540
            },
            "LLMLatency": {
                "MiddleLatency": 754,
                "MinLatency": 642,
                "P90Latency": 912
            },
            "TTSLatency": {
                "MiddleLatency": 267,
                "MinLatency": 146,
                "P90Latency": 366
            }
        },
        "RequestId": "ca9c3062-202b-4401-a930-3728d1ef7886"
    }
}
```

