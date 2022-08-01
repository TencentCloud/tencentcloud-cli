**Example 1: 查询已绑定源站健康检查统计数据**

查询已绑定源站健康检查统计数据

Input: 

```
tccli gaap DescribeRealServerStatistics --cli-unfold-argument  \
    --WithinTime 3 \
    --RealServerId rs-rfgt56hy \
    --ListenerId listener-gucvb6d
```

Output: 
```
{
    "Response": {
        "RsStatisticsData": [
            {
                "MetricData": [
                    {
                        "Data": 0.0,
                        "Time": 1
                    },
                    {
                        "Data": 0.0,
                        "Time": 1
                    }
                ],
                "MetricName": "xx"
            },
            {
                "MetricData": [
                    {
                        "Data": 0.0,
                        "Time": 1
                    },
                    {
                        "Data": 0.0,
                        "Time": 1
                    }
                ],
                "MetricName": "xx"
            }
        ],
        "RequestId": "xx",
        "StatisticsData": [
            {
                "Data": 0.0,
                "Time": 1
            }
        ]
    }
}
```

