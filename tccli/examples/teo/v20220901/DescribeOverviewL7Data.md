**Example 1: 根据标签查询时序流量数据**

根据标签的筛选条件获取请求数指标

Input: 

```
tccli teo DescribeOverviewL7Data --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Flow_request \
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
                        "Avg": 1564,
                        "Detail": [
                            {
                                "Timestamp": 1659139200,
                                "Value": 100
                            },
                            {
                                "Timestamp": 1659225600,
                                "Value": 34
                            }
                        ],
                        "Max": 8037,
                        "MetricName": "l7Flow_request",
                        "Sum": 48511
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 查询七层监控类时序流量数据**

查询七层监控数据的请求数指标

Input: 

```
tccli teo DescribeOverviewL7Data --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Flow_request \
    --ZoneIds zone-2mzegj4vln5f
```

Output: 
```
{
    "Response": {
        "RequestId": "6cc74d08-c174-413a-976b-abe7b851e010",
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "Avg": 1564,
                        "Detail": [
                            {
                                "Timestamp": 1659139200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1659225600,
                                "Value": 0
                            }
                        ],
                        "Max": 8037,
                        "MetricName": "l7Flow_request",
                        "Sum": 48511
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

