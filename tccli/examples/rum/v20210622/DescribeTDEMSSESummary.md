**Example 1: 查询大模型体验汇总**



Input: 

```
tccli rum DescribeTDEMSSESummary --cli-unfold-argument  \
    --AppId 7 \
    --StartTime 1710000000000 \
    --EndTime 1710003600000 \
    --Filters [{"Key":"model_version","Op":"in","Values":["gpt-4o"]}]
```

Output: 
```
{
    "Response": {
        "ConversationCount": 12,
        "TotalTokenCount": 3400,
        "TokenThroughput": 18.5,
        "FirstMessageDelay": 420,
        "ErrorRate": 8.3,
        "StallRate": 0,
        "Fluency": 76.2,
        "RequestId": "37858f63-fa66-42f2-86af-52a83f742841"
    }
}
```

