**Example 1: 查询四层时序并发连接数指标时序数据**

查询 ZoneId = zone-28kw53cmc6ky 的站点下，全部四层实例在 2025-10-01T08:00:00+08:00 ~ 2025-10-01T10:00:00+08:00 期间的并发连接数时序数据。

Input: 

```
tccli teo DescribeTimingL4Data --cli-unfold-argument  \
    --ZoneIds zone-28kw53cmc6ky \
    --StartTime 2025-10-01T08:00:00+08:00 \
    --EndTime 2025-10-01T10:00:00+08:00 \
    --Interval hour \
    --MetricNames l4Flow_connections
```

Output: 
```
{
    "Response": {
        "RequestId": "e12e0659-ae34-4140-9878-4a61db0c3639",
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "Avg": 16,
                        "Detail": [
                            {
                                "Timestamp": 1759276800,
                                "Value": 15
                            },
                            {
                                "Timestamp": 1759280400,
                                "Value": 17
                            },
                            {
                                "Timestamp": 1759284000,
                                "Value": 0
                            }
                        ],
                        "Max": 17,
                        "MetricName": "l4Flow_connections",
                        "Sum": 32
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 根据四层代理转发规则 ID 查询访问总流量时序数据**

查询 ZoneId = zone-28kw53cmc6ky 的站点下， RuleId = rule-033950bf-6fc4-11ed-8ab2-525400a22580 的四层实例转发规则 在 2025-10-01T08:00:00+08:00 ~ 2025-10-01T10:00:00+08:00 期间的访问总流量时序数据。

Input: 

```
tccli teo DescribeTimingL4Data --cli-unfold-argument  \
    --ZoneIds zone-28kw53cmc6ky \
    --StartTime 2025-10-01T08:00:00+08:00 \
    --EndTime 2025-10-01T10:00:00+08:00 \
    --Interval hour \
    --MetricNames l4Flow_flux \
    --Filters.0.Key ruleId \
    --Filters.0.Operator equals \
    --Filters.0.Value rule-033950bf-6fc4-11ed-8ab2-525400a22580
```

Output: 
```
{
    "Response": {
        "RequestId": "962792de-3bfe-483d-99a7-3cfde0467495",
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "Avg": 5640,
                        "Detail": [
                            {
                                "Timestamp": 1671669600,
                                "Value": 3900
                            },
                            {
                                "Timestamp": 1671669900,
                                "Value": 7400
                            },
                            {
                                "Timestamp": 1671670800,
                                "Value": 5620
                            }
                        ],
                        "Max": 7400,
                        "MetricName": "l4Flow_flux",
                        "Sum": 16920
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 3: 根据四层实例 ID 查询新建连接数速率时序数据**

查询 ZoneId = zone-28kw53cmc6ky 的站点下， ProxyId = sid-3kr5me8zidha 的四层实例 在 2025-10-01T08:00:00+08:00 ~ 2025-10-01T10:00:00+08:00 期间的新建连接数速率时序数据。
注意：因为本次查询的指标 MetricNames 中 l4Flow_newConnectionsRate 的值类型为 Float，所以从 Data.N.FloatTypeValue 返回 l4Flow_newConnectionsRate 指标对应的时序数据。

Input: 

```
tccli teo DescribeTimingL4Data --cli-unfold-argument  \
    --ZoneIds zone-28kw53cmc6ky \
    --StartTime 2025-10-01T08:00:00+08:00 \
    --EndTime 2025-10-01T10:00:00+08:00 \
    --Interval hour \
    --MetricNames l4Flow_newConnectionsRate \
    --Filters.0.Key proxyId \
    --Filters.0.Operator equals \
    --Filters.0.Value sid-3kr5me8zidha
```

Output: 
```
{
    "Response": {
        "RequestId": "962792de-3bfe-483d-99a7-3cfde0467495",
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [],
                "FloatTypeValue": [
                    {
                        "Avg": 1.56,
                        "Detail": [
                            {
                                "Timestamp": 1671669600,
                                "Value": 1.08
                            },
                            {
                                "Timestamp": 1671669900,
                                "Value": 2.05
                            },
                            {
                                "Timestamp": 1671670800,
                                "Value": 1.56
                            }
                        ],
                        "Max": 2.05,
                        "MetricName": "l4Flow_newConnectionsRate",
                        "Sum": 4.69
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

