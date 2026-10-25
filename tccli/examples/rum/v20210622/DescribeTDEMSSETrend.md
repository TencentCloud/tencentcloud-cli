**Example 1: 查询大模型体验趋势**



Input: 

```
tccli rum DescribeTDEMSSETrend --cli-unfold-argument  \
    --AppId 7 \
    --StartTime 1710000000000 \
    --EndTime 1710003600000 \
    --Filters [{"Key":"model_version","Op":"in","Values":["gpt-4o"]}] \
    --Metric token_throughput \
    --Dimension overall \
    --TopN 7
```

Output: 
```
{
    "Response": {
        "IntervalSec": 60,
        "Points": [
            {
                "Time": 1710000000000,
                "ConversationCount": 3,
                "Value": 18.5
            }
        ],
        "Series": [],
        "RequestId": "37858f63-fa66-42f2-86af-52a83f742841"
    }
}
```

