**Example 1: 查询四层连接数列表**



Input: 

```
tccli teo DescribeTimingL4AccessData --cli-unfold-argument  \
    --MetricNames l4Flow_connections \
    --Interval hour \
    --StartTime 2020-09-21T00:00:00+00:00 \
    --EndTime 2020-09-23T00:00:00+00:00 \
    --Area mainland
```

Output: 
```
{
    "Response": {
        "RequestId": "58c8cef0-3e0a-4fde-bac2-90cf05ab3152",
        "TimingDataRecords": [
            {
                "TypeKey": "1252177752",
                "TypeValue": [
                    {
                        "Avg": 1568,
                        "Detail": [
                            {
                                "Timestamp": 1661904000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1661990400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662076800,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662163200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662249600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662336000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662422400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662508800,
                                "Value": 31377
                            },
                            {
                                "Timestamp": 1662595200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662681600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662768000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662854400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1662940800,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1663027200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1663113600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1663200000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1663286400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1663372800,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1663459200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1663545600,
                                "Value": 0
                            }
                        ],
                        "Max": 31377,
                        "MetricName": "l4Flow_connections",
                        "Sum": 31377
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 根据转发规则ID查询四层连接数**



Input: 

```
tccli teo DescribeTimingL4AccessData --cli-unfold-argument  \
    --MetricNames l4Flow_connections \
    --Interval hour \
    --StartTime 2020-09-21T00:00:00+00:00 \
    --EndTime 2020-09-23T00:00:00+00:00 \
    --Area mainland \
    --QueryConditions.0.Key ruleId \
    --QueryConditions.0.Operator equals \
    --QueryConditions.0.Value rule-033950bf-6fc4-11ed-8ab2-525400a22580
```

Output: 
```
{
    "Response": {
        "RequestId": "395cb39c-8057-4d4e-b4d4-8bbbf3806f08",
        "TimingDataRecords": [
            {
                "TypeKey": "1310708577",
                "TypeValue": [
                    {
                        "Avg": 5,
                        "Detail": [
                            {
                                "Timestamp": 1671683100,
                                "Value": 1
                            },
                            {
                                "Timestamp": 1671683400,
                                "Value": 7
                            },
                            {
                                "Timestamp": 1671683700,
                                "Value": 7
                            },
                            {
                                "Timestamp": 1671684000,
                                "Value": 8
                            },
                            {
                                "Timestamp": 1671684300,
                                "Value": 5
                            },
                            {
                                "Timestamp": 1671684600,
                                "Value": 8
                            },
                            {
                                "Timestamp": 1671684900,
                                "Value": 5
                            },
                            {
                                "Timestamp": 1671685200,
                                "Value": 6
                            },
                            {
                                "Timestamp": 1671685500,
                                "Value": 6
                            },
                            {
                                "Timestamp": 1671685800,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671686100,
                                "Value": 5
                            },
                            {
                                "Timestamp": 1671686400,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671686700,
                                "Value": 4
                            },
                            {
                                "Timestamp": 1671687000,
                                "Value": 5
                            },
                            {
                                "Timestamp": 1671687300,
                                "Value": 9
                            },
                            {
                                "Timestamp": 1671687600,
                                "Value": 3
                            }
                        ],
                        "Max": 24,
                        "MetricName": "l4Flow_connections",
                        "Sum": 388
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 3: 根据四层代理实例ID查询四层连接数**



Input: 

```
tccli teo DescribeTimingL4AccessData --cli-unfold-argument  \
    --MetricNames l4Flow_connections \
    --Interval hour \
    --StartTime 2020-09-21T00:00:00+00:00 \
    --EndTime 2020-09-23T00:00:00+00:00 \
    --Area mainland \
    --QueryConditions.0.Key proxyId \
    --QueryConditions.0.Operator equals \
    --QueryConditions.0.Value sid-2c2uug8ubfmn
```

Output: 
```
{
    "Response": {
        "RequestId": "395cb39c-8057-4d4e-b4d4-8bbbf3806f08",
        "TimingDataRecords": [
            {
                "TypeKey": "1310708577",
                "TypeValue": [
                    {
                        "Avg": 5,
                        "Detail": [
                            {
                                "Timestamp": 1671683100,
                                "Value": 1
                            },
                            {
                                "Timestamp": 1671683400,
                                "Value": 7
                            },
                            {
                                "Timestamp": 1671683700,
                                "Value": 7
                            },
                            {
                                "Timestamp": 1671684000,
                                "Value": 8
                            },
                            {
                                "Timestamp": 1671684300,
                                "Value": 5
                            },
                            {
                                "Timestamp": 1671684600,
                                "Value": 8
                            },
                            {
                                "Timestamp": 1671684900,
                                "Value": 5
                            },
                            {
                                "Timestamp": 1671685200,
                                "Value": 6
                            },
                            {
                                "Timestamp": 1671685500,
                                "Value": 6
                            },
                            {
                                "Timestamp": 1671685800,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671686100,
                                "Value": 5
                            },
                            {
                                "Timestamp": 1671686400,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671686700,
                                "Value": 4
                            },
                            {
                                "Timestamp": 1671687000,
                                "Value": 5
                            },
                            {
                                "Timestamp": 1671687300,
                                "Value": 9
                            },
                            {
                                "Timestamp": 1671687600,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671687900,
                                "Value": 4
                            },
                            {
                                "Timestamp": 1671688200,
                                "Value": 8
                            },
                            {
                                "Timestamp": 1671688500,
                                "Value": 17
                            },
                            {
                                "Timestamp": 1671688800,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671689100,
                                "Value": 11
                            },
                            {
                                "Timestamp": 1671689400,
                                "Value": 10
                            },
                            {
                                "Timestamp": 1671689700,
                                "Value": 4
                            },
                            {
                                "Timestamp": 1671690000,
                                "Value": 2
                            },
                            {
                                "Timestamp": 1671690300,
                                "Value": 6
                            },
                            {
                                "Timestamp": 1671690600,
                                "Value": 9
                            },
                            {
                                "Timestamp": 1671690900,
                                "Value": 2
                            },
                            {
                                "Timestamp": 1671691200,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671691500,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671691800,
                                "Value": 9
                            },
                            {
                                "Timestamp": 1671692100,
                                "Value": 7
                            },
                            {
                                "Timestamp": 1671692400,
                                "Value": 6
                            },
                            {
                                "Timestamp": 1671692700,
                                "Value": 2
                            },
                            {
                                "Timestamp": 1671693000,
                                "Value": 4
                            },
                            {
                                "Timestamp": 1671693300,
                                "Value": 6
                            },
                            {
                                "Timestamp": 1671693600,
                                "Value": 1
                            },
                            {
                                "Timestamp": 1671693900,
                                "Value": 4
                            },
                            {
                                "Timestamp": 1671694200,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671694500,
                                "Value": 2
                            },
                            {
                                "Timestamp": 1671694800,
                                "Value": 3
                            },
                            {
                                "Timestamp": 1671695100,
                                "Value": 12
                            },
                            {
                                "Timestamp": 1671695400,
                                "Value": 4
                            },
                            {
                                "Timestamp": 1671695700,
                                "Value": 24
                            },
                            {
                                "Timestamp": 1671696000,
                                "Value": 1
                            }
                        ],
                        "Max": 24,
                        "MetricName": "l4Flow_connections",
                        "Sum": 388
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

