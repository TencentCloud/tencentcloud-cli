**Example 1: 查询大模型体验多维分析**



Input: 

```
tccli rum DescribeTDEMSSEDimensions --cli-unfold-argument  \
    --AppId 7 \
    --StartTime 1710000000000 \
    --EndTime 1710003600000 \
    --Filters [{"Key":"model_version","Op":"in","Values":["gpt-4o"]}] \
    --Metric first_message_delay \
    --Dimension region
```

Output: 
```
{
    "Response": {
        "Rows": [
            {
                "DimensionValue": "中国 / 广东",
                "ConversationCount": 8,
                "Value": 510
            }
        ],
        "RequestId": "37858f63-fa66-42f2-86af-52a83f742841"
    }
}
```

