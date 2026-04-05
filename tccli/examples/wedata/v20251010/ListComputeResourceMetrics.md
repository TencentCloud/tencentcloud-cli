**Example 1: 获取计算资源监控指标**



Input: 

```
tccli wedata ListComputeResourceMetrics --cli-unfold-argument  \
    --ResourceId 12 \
    --StartTime 1764819375549 \
    --EndTime 1764820375549
```

Output: 
```
{
    "Response": {
        "Data": {
            "Metrics": [
                {
                    "CUQuota": 100,
                    "CurrTime": "1764819255549",
                    "ResourceLoad": 0.25,
                    "UsedCU": 25
                },
                {
                    "CUQuota": 100,
                    "CurrTime": "1764819315549",
                    "ResourceLoad": 0.3,
                    "UsedCU": 30
                },
                {
                    "CUQuota": 100,
                    "CurrTime": "1764819375549",
                    "ResourceLoad": 0.2,
                    "UsedCU": 20
                },
                {
                    "CUQuota": 100,
                    "CurrTime": "1764819435549",
                    "ResourceLoad": 0.35,
                    "UsedCU": 35
                },
                {
                    "CUQuota": 100,
                    "CurrTime": "1764819495549",
                    "ResourceLoad": 0.28,
                    "UsedCU": 28
                }
            ]
        },
        "RequestId": "1d2f4aa6-a4a8-466d-8792-7e0796e5c3c9"
    }
}
```

