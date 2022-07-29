**Example 1: 查询通道统计数据**

查询通道统计数据

Input: 

```
tccli gaap DescribeProxyStatistics --cli-unfold-argument  \
    --ProxyId link-rfgt56hy \
    --EndTime 2019-03-26 12:00:00 \
    --Granularity 300 \
    --StartTime 2019-03-25 12:00:00 \
    --MetricNames Concurrent
```

Output: 
```
{
    "Response": {
        "StatisticsData": [
            {
                "MetricName": "Concurrent",
                "MetricData": [
                    {
                        "Time": 1564734780,
                        "Data": 2000
                    },
                    {
                        "Time": 1564734720,
                        "Data": 2001
                    }
                ]
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

