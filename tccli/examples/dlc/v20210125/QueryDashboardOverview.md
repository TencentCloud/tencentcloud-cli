**Example 1: 给定时间范围内监控大盘指标示例**



Input: 

```
tccli dlc QueryDashboardOverview --cli-unfold-argument  \
    --StartTime 1780402821 \
    --EndTime 1780403121
```

Output: 
```
{
    "Response": {
        "AverageP99LatencyMs": 0,
        "ErrorRate": 0,
        "TotalRequestsPerSecond": 0,
        "RequestId": "8c1c5bee-a7b6-4c6f-95f1-30280c787511"
    }
}
```

