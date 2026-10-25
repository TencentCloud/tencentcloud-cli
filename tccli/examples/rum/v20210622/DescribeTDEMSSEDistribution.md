**Example 1: 查询大模型体验分布**



Input: 

```
tccli rum DescribeTDEMSSEDistribution --cli-unfold-argument  \
    --AppId 7 \
    --StartTime 1710000000000 \
    --EndTime 1710003600000 \
    --Filters [{"Key":"model_version","Op":"in","Values":["gpt-4o"]}] \
    --Metric fluency
```

Output: 
```
{
    "Response": {
        "Bins": [
            {
                "Start": 0,
                "End": 1,
                "Overflow": false,
                "Count": 4,
                "Rate": 33.3
            }
        ],
        "RequestId": "37858f63-fa66-42f2-86af-52a83f742841"
    }
}
```

