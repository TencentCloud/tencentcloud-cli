**Example 1: 查询指定机房交换机数据**

按指标名，查询统计数据。数据按1分钟间隔统计

Input: 

```
tccli edgezone DescribeZoneData --cli-unfold-argument  \
    --MetricName inbw \
    --Zone ap-guangzhou-1 \
    --StartTime 2026-04-23T07:00:00Z \
    --EndTime 2026-04-23T08:00:00Z
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Time": "2026-04-23T07:00:00Z",
                "Value": 1.1
            },
            {
                "Time": "2026-04-23T07:01:00Z",
                "Value": 2.1
            }
        ],
        "RequestId": "b5d7f3a2-c418-4b9e-9c72-4a1e6d3f8b90"
    }
}
```

