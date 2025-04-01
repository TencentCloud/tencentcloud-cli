**Example 1: 获取redis慢SQL模板列表**



Input: 

```
tccli dbbrain DescribeRedisSlowLogTopSqls --cli-unfold-argument  \
    --InstanceId crs-k1gjspdk \
    --StartTime 2025-03-27 02:00:00 \
    --EndTime 2025-03-27 02:20:00 \
    --Product redis
```

Output: 
```
{
    "Response": {
        "RequestId": "65f3eaaf-935c-4084-8eb5-0c04fbbda952",
        "Rows": [
            {
                "Cmd": "bgsave",
                "Detail": "bgsave",
                "ExecTimes": 1,
                "QueryTime": 0.01,
                "QueryTimeAvg": 0.01,
                "QueryTimeMax": 0.01,
                "QueryTimeMin": 0.01,
                "QueryTimeRatio": 100
            }
        ],
        "TotalCount": 1
    }
}
```

