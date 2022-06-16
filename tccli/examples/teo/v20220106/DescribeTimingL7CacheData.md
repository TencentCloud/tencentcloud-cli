**Example 1: 七层缓存分析类时序流量数据**



Input: 

```
tccli teo DescribeTimingL7CacheData --cli-unfold-argument  \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --MetricNames xx \
    --Interval xx \
    --ZoneIds xx \
    --Filters.0.Operator xx \
    --Filters.0.Value xx \
    --Filters.0.Key xx \
    --EndTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "Type": "xx",
        "Interval": "xx",
        "Data": [
            {
                "TypeKey": "xx",
                "TypeValue": [
                    {
                        "Max": 0,
                        "Sum": 0,
                        "Detail": [
                            {
                                "Timestamp": 0,
                                "Value": 0
                            }
                        ],
                        "DetailData": [
                            0
                        ],
                        "Avg": 0,
                        "MetricName": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

