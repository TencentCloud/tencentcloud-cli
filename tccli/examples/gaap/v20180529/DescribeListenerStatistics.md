**Example 1: 查询监听器统计数据**

查询监听器统计数据

Input: 

```
tccli gaap DescribeListenerStatistics --cli-unfold-argument  \
    --EndTime 2019-03-26 12:00:00 \
    --Granularity 300 \
    --ListenerId listener-rfgt56hy \
    --StartTime 2019-03-25 12:00:00 \
    --MetricNames OutputBandwidth InputBandwidth
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
                        "Time": 1564736040,
                        "Data": 2000
                    },
                    {
                        "Time": 1564735980,
                        "Data": 2001
                    }
                ]
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

