**Example 1: 查询大模型体验分位**



Input: 

```
tccli rum DescribeTDEMSSEPercentile --cli-unfold-argument  \
    --AppId 7 \
    --StartTime 1710000000000 \
    --EndTime 1710003600000 \
    --Filters [{"Key":"model_version","Op":"in","Values":["gpt-4o"]}] \
    --Metric first_message_delay
```

Output: 
```
{
    "Response": {
        "IntervalSec": 3600,
        "Average": 420,
        "P50": 380,
        "P75": 510,
        "P95": 2400,
        "P99": 8000,
        "Points": [
            {
                "Time": 1710000000000,
                "Average": 400,
                "P50": 360,
                "P75": 500,
                "P95": 2100,
                "P99": 7600
            }
        ],
        "RequestId": "37858f63-fa66-42f2-86af-52a83f742841"
    }
}
```

