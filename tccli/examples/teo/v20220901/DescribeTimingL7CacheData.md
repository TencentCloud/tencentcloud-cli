**Example 1: 查询七层缓存分析类时序流量数据**



Input: 

```
tccli teo DescribeTimingL7CacheData --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Cache_outFlux
```

Output: 
```
{
    "Response": {
        "RequestId": "1c827ba2-7010-45d2-b16b-6d0c4d68a771",
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "Avg": 239058,
                        "Detail": [
                            {
                                "Timestamp": 1659139200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1661731200,
                                "Value": 0
                            }
                        ],
                        "Max": 2363561,
                        "MetricName": "l7Cache_outFlux",
                        "Sum": 7410804
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

