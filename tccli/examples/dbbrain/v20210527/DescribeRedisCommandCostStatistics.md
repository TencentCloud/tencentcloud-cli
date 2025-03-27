**Example 1: 查询命令延迟分布区间列表**



Input: 

```
tccli dbbrain DescribeRedisCommandCostStatistics --cli-unfold-argument  \
    --InstanceId crs-86lffr2l \
    --Product redis \
    --StartTime 2025-03-17T14:36:05+00:00 \
    --EndTime 2025-03-17T14:39:05+00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "85e37000-02fa-11f0-a09f-9b462124ee46",
        "CmdCostGroups": [
            {
                "Percent": 37.2,
                "CostUpperLimit": "1",
                "CostLowerLimit": "0",
                "Count": 62937
            },
            {
                "Percent": 31.4,
                "CostUpperLimit": "2",
                "CostLowerLimit": "1",
                "Count": 53073
            },
            {
                "Percent": 28.1,
                "CostUpperLimit": "5",
                "CostLowerLimit": "2",
                "Count": 47475
            },
            {
                "Percent": 0.5,
                "CostUpperLimit": "50",
                "CostLowerLimit": "20",
                "Count": 888
            },
            {
                "Percent": 1.2,
                "CostUpperLimit": "200",
                "CostLowerLimit": "100",
                "Count": 1990
            },
            {
                "Percent": 1.2,
                "CostUpperLimit": "more",
                "CostLowerLimit": "200",
                "Count": 1946
            },
            {
                "Percent": 0.1,
                "CostUpperLimit": "10",
                "CostLowerLimit": "5",
                "Count": 229
            },
            {
                "Percent": 0.3,
                "CostUpperLimit": "100",
                "CostLowerLimit": "50",
                "Count": 435
            },
            {
                "Percent": 0.1,
                "CostUpperLimit": "20",
                "CostLowerLimit": "10",
                "Count": 128
            }
        ]
    }
}
```

