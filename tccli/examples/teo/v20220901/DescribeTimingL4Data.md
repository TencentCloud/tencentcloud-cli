**Example 1: 查询四层时序流量数据**



Input: 

```
tccli teo DescribeTimingL4Data --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l4Flow_inFlux
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
                        "Avg": 740563,
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
                        "Max": 6319079,
                        "MetricName": "l4Flow_inFlux",
                        "Sum": 22957455
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 根据转发规则ID查询四层流量数据**



Input: 

```
tccli teo DescribeTimingL4Data --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l4Flow_inFlux \
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
                "TypeKey": "zone-28kw53cmc6ky",
                "TypeValue": [
                    {
                        "Avg": 267,
                        "Detail": [
                            {
                                "Timestamp": 1671669600,
                                "Value": 390
                            },
                            {
                                "Timestamp": 1671669900,
                                "Value": 740
                            },
                            {
                                "Timestamp": 1671670200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671670500,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671670800,
                                "Value": 562
                            },
                            {
                                "Timestamp": 1671671100,
                                "Value": 690
                            },
                            {
                                "Timestamp": 1671671400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671671700,
                                "Value": 1353
                            },
                            {
                                "Timestamp": 1671672000,
                                "Value": 1291
                            },
                            {
                                "Timestamp": 1671672300,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671672600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671672900,
                                "Value": 300
                            },
                            {
                                "Timestamp": 1671673200,
                                "Value": 453
                            },
                            {
                                "Timestamp": 1671673500,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671673800,
                                "Value": 19
                            },
                            {
                                "Timestamp": 1671674100,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671674400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671674700,
                                "Value": 204
                            },
                            {
                                "Timestamp": 1671675000,
                                "Value": 530
                            },
                            {
                                "Timestamp": 1671675300,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671675600,
                                "Value": 975
                            },
                            {
                                "Timestamp": 1671675900,
                                "Value": 777
                            },
                            {
                                "Timestamp": 1671676200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671676500,
                                "Value": 530
                            },
                            {
                                "Timestamp": 1671676800,
                                "Value": 320
                            },
                            {
                                "Timestamp": 1671677100,
                                "Value": 303
                            },
                            {
                                "Timestamp": 1671677400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671677700,
                                "Value": 183
                            },
                            {
                                "Timestamp": 1671678000,
                                "Value": 320
                            },
                            {
                                "Timestamp": 1671678300,
                                "Value": 670
                            },
                            {
                                "Timestamp": 1671678600,
                                "Value": 131
                            },
                            {
                                "Timestamp": 1671678900,
                                "Value": 804
                            },
                            {
                                "Timestamp": 1671679200,
                                "Value": 131
                            }
                        ],
                        "Max": 31540,
                        "MetricName": "l4Flow_outFlux",
                        "Sum": 147864
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 3: 根据四层代理ID查询四层流量数据**



Input: 

```
tccli teo DescribeTimingL4Data --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l4Flow_inFlux \
    --Filters.0.Key proxyId \
    --Filters.0.Operator equals \
    --Filters.0.Value sid-2c2uug8ubfmn
```

Output: 
```
{
    "Response": {
        "RequestId": "962792de-3bfe-483d-99a7-3cfde0467495",
        "Data": [
            {
                "TypeKey": "zone-28kw53cmc6ky",
                "TypeValue": [
                    {
                        "Avg": 267,
                        "Detail": [
                            {
                                "Timestamp": 1671669600,
                                "Value": 390
                            },
                            {
                                "Timestamp": 1671669900,
                                "Value": 740
                            },
                            {
                                "Timestamp": 1671670200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671670500,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671670800,
                                "Value": 562
                            },
                            {
                                "Timestamp": 1671671100,
                                "Value": 690
                            },
                            {
                                "Timestamp": 1671671400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671671700,
                                "Value": 1353
                            },
                            {
                                "Timestamp": 1671672000,
                                "Value": 1291
                            },
                            {
                                "Timestamp": 1671672300,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671672600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671672900,
                                "Value": 300
                            },
                            {
                                "Timestamp": 1671673200,
                                "Value": 453
                            },
                            {
                                "Timestamp": 1671673500,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671673800,
                                "Value": 19
                            },
                            {
                                "Timestamp": 1671674100,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671674400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671674700,
                                "Value": 204
                            },
                            {
                                "Timestamp": 1671675000,
                                "Value": 530
                            },
                            {
                                "Timestamp": 1671675300,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671675600,
                                "Value": 975
                            },
                            {
                                "Timestamp": 1671675900,
                                "Value": 777
                            },
                            {
                                "Timestamp": 1671676200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671676500,
                                "Value": 530
                            },
                            {
                                "Timestamp": 1671676800,
                                "Value": 320
                            },
                            {
                                "Timestamp": 1671677100,
                                "Value": 303
                            },
                            {
                                "Timestamp": 1671677400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671677700,
                                "Value": 183
                            },
                            {
                                "Timestamp": 1671678000,
                                "Value": 320
                            },
                            {
                                "Timestamp": 1671678300,
                                "Value": 670
                            },
                            {
                                "Timestamp": 1671678600,
                                "Value": 131
                            },
                            {
                                "Timestamp": 1671678900,
                                "Value": 804
                            },
                            {
                                "Timestamp": 1671679200,
                                "Value": 131
                            }
                        ],
                        "Max": 31540,
                        "MetricName": "l4Flow_outFlux",
                        "Sum": 147864
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

