**Example 1: 查询通道组统计数据**

查询通道组统计数据

Input: 

```
tccli gaap DescribeProxyGroupStatistics --cli-unfold-argument  \
    --EndTime 2019-03-26 12:00:00 \
    --Granularity 300 \
    --GroupId lg-rfgt56hy \
    --StartTime 2019-03-25 12:00:00 \
    --MetricNames InputBandwidth
```

Output: 
```
{
    "Response": {
        "StatisticsData": [
            {
                "MetricName": "InputBandwidth",
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

