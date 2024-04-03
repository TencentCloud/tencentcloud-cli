**Example 1: 查询指定标签的时序流量数据**



Input: 

```
tccli teo DescribeTimingL7CacheData --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Cache_outFlux \
    --Filters.0.Key tagKey \
    --Filters.0.Operator equals \
    --Filters.0.Value test1 \
    --Filters.1.Key tagValue \
    --Filters.1.Operator equals \
    --Filters.1.Value a.com b.com \
    --ZoneIds zone-2mzegj4vln5f
```

Output: 
```
{
    "Response": {
        "RequestId": "6cc74d08-c174-413a-976b-abe7b851e0121",
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "Avg": 239058,
                        "Detail": [
                            {
                                "Timestamp": 1659139200,
                                "Value": 8
                            },
                            {
                                "Timestamp": 1661731200,
                                "Value": 1
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

**Example 2: 查询指定状态码的时序流量数据**



Input: 

```
tccli teo DescribeTimingL7CacheData --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Cache_outFlux \
    --Filters.0.Key statusCode \
    --Filters.0.Operator equals \
    --Filters.0.Value 1XX 2XX \
    --ZoneIds zone-2mzegj4vln5f
```

Output: 
```
{
    "Response": {
        "RequestId": "1c827ba2-7010-45d2-123b-6d0c4d34ihsx",
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "Avg": 239058,
                        "Detail": [
                            {
                                "Timestamp": 1659139200,
                                "Value": 10
                            },
                            {
                                "Timestamp": 1661731200,
                                "Value": 10
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

**Example 3: 查询七层缓存分析类时序流量数据**



Input: 

```
tccli teo DescribeTimingL7CacheData --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Cache_outFlux \
    --ZoneIds zone-2mzegj4vln5f
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

