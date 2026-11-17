**Example 1: 查询排队任务数**



Input: 

```
tccli dlc DescribePartitionMonitorOverview --cli-unfold-argument  \
    --MetricKeys pending_workloads \
    --PartitionCode dlc-p-vboauljz
```

Output: 
```
{
    "Response": {
        "Metrics": [
            {
                "MetricKey": "pending_workloads",
                "Unit": "count",
                "ResourceType": "kueue",
                "Value": 0
            }
        ],
        "RequestId": "1ed50a8c-1ffb-4023-b906-7a9c1730d51f"
    }
}
```

