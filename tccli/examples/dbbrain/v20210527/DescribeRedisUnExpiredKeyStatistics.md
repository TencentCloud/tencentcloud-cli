**Example 1: 查询指定任务的Key统计分布**



Input: 

```
tccli dbbrain DescribeRedisUnExpiredKeyStatistics --cli-unfold-argument  \
    --InstanceId crs-br63td53 \
    --Product redis \
    --Date 2026-01-04 \
    --AsyncRequestId 7200449 \
    --ShardIds 1
```

Output: 
```
{
    "Response": {
        "SeriesData": [
            {
                "Capacity": 192,
                "Count": 3
            }
        ],
        "RequestId": "77dda44c-15db-4f52-91df-8e60485adc0e"
    }
}
```

