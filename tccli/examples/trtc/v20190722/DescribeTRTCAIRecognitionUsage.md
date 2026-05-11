**Example 1: 查询指定时间范围内AI 实时对话用量**

查询指定时间范围内AI 实时对话用量

Input: 

```
tccli trtc DescribeTRTCAIRecognitionUsage --cli-unfold-argument  \
    --StartTime 2026-04-01 00:00:00 \
    --EndTime 2026-04-02 00:00:00 \
    --AuType conversation \
    --SdkAppId 1400763596
```

Output: 
```
{
    "Response": {
        "TotalUsage": [
            0
        ],
        "UsageKey": [
            "Conversation"
        ],
        "UsageList": [
            {
                "TimeKey": "2026-04-01 00:00:00",
                "UsageValue": [
                    0
                ]
            }
        ],
        "RequestId": "f6333ebf-b53b-4be4-82c3-81b70f91f55a"
    }
}
```

