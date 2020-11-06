**Example 1: Querying the health check statistics of bound origin server**

This example shows you how to query the health check statistics of a bound origin server.

Input: 

```
tccli gaap DescribeRealServerStatistics --cli-unfold-argument  \
    --RealServerId rs-rfgt56hy \
    --ListenerId listener-gucvb6d \
    --WithinTime 3
```

Output: 
```
{
    "Response": {
        "StatisticsData": [
            {
                "MetricName": "80",
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
            },
            {
                "MetricName": "8080",
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

