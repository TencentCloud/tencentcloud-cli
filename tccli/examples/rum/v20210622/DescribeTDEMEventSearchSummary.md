**Example 1: 查询探索事件汇总**



Input: 

```
tccli rum DescribeTDEMEventSearchSummary --cli-unfold-argument  \
    --AppId 11 \
    --StartTime 1787404860000 \
    --EndTime 1789996860000 \
    --Category error
```

Output: 
```
{
    "Response": {
        "CategoryCounts": [
            {
                "Key": "session",
                "Value": 1
            }
        ],
        "IntervalSec": 3600,
        "Series": [
            {
                "Count": 5,
                "Timestamp": 1789718400000
            }
        ],
        "Total": 5,
        "Users": 1,
        "Visitors": 1,
        "RequestId": "12301d55-901b-42b4-9755-a261e934477d"
    }
}
```

