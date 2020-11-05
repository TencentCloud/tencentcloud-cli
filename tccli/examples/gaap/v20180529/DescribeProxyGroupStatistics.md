**Example 1: Querying the Connection Group Statistics**

Query the connection group statistics.

Input: 

```
tccli gaap DescribeProxyGroupStatistics --cli-unfold-argument  \
    --GroupId lg-rfgt56hy\
    --MetricNames InputBandwidth\
    --StartTime '2019-03-25 12:00:00'\
    --EndTime '2019-03-26 12:00:00'\
    --Granularity 300
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

