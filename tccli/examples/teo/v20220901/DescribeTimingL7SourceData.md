**Example 1: 查询指定源站的回源分析时序数据**

查询源站值为119.28.108.213的各项回源指标数据

Input: 

```
tccli teo DescribeTimingL7SourceData --cli-unfold-argument  \
    --StartTime 2022-12-14T07:32:00+08:00 \
    --EndTime 2022-12-21T00:00:00+08:00 \
    --ZoneIds zone-2cfc5kesov7g \
    --Filters.0.Key origin \
    --Filters.0.Operator equals \
    --Filters.0.Value 119.28.108.213 \
    --Interval hour \
    --Area overseas \
    --MetricNames l7Flow_outFlux_hy l7Flow_inFlux_hy l7Flow_request_hy l7Flow_outBandwidth_hy l7Flow_inBandwidth_hy
```

Output: 
```
{
    "Response": {
        "RequestId": "02c49505-c740-4ee8-8128-dbe3ce0bf34e",
        "TimingDataRecords": [
            {
                "TypeKey": "251231751_cheney_test1",
                "TypeValue": [
                    {
                        "Avg": 2,
                        "Detail": [
                            {
                                "Timestamp": 1672002000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672005600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672009200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672092000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672095600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672099200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672102800,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672106400,
                                "Value": 306
                            },
                            {
                                "Timestamp": 1672110000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672113600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672117200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672120800,
                                "Value": 307
                            },
                            {
                                "Timestamp": 1672124400,
                                "Value": 239
                            },
                            {
                                "Timestamp": 1672128000,
                                "Value": 0
                            }
                        ],
                        "Max": 25812,
                        "MetricName": "l7Flow_outFlux_hy",
                        "Sum": 26973
                    },
                    {
                        "Avg": 0,
                        "Detail": [
                            {
                                "Timestamp": 1671980400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671984000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671987600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671991200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671994800,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671998400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672002000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672005600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672009200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672012800,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672016400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672128000,
                                "Value": 0
                            }
                        ],
                        "Max": 394,
                        "MetricName": "l7Flow_inBandwidth_hy",
                        "Sum": 418
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 查询指定源站组的回源分析时序数据**

查询源站组名称为origin-2be4c888-82a1-11ed-b61e-525400931057的各项回源指标数据

Input: 

```
tccli teo DescribeTimingL7SourceData --cli-unfold-argument  \
    --StartTime 2022-12-21T00:00:00+08:00 \
    --EndTime 2022-12-27T16:28:00+08:00 \
    --ZoneIds zone-2cfc5kesov7g \
    --Filters.0.Key originGroup \
    --Filters.0.Operator equals \
    --Filters.0.Value origin-2be4c888-82a1-11ed-b61e-525400931057 \
    --Interval hour \
    --Area overseas \
    --MetricNames l7Flow_outFlux_hy l7Flow_inFlux_hy l7Flow_request_hy l7Flow_outBandwidth_hy l7Flow_inBandwidth_hy
```

Output: 
```
{
    "Response": {
        "RequestId": "cfc96e9b-99bd-4800-8335-d195346c0218",
        "TimingDataRecords": [
            {
                "TypeKey": "251231751_cheney_test1",
                "TypeValue": [
                    {
                        "Avg": 2,
                        "Detail": [
                            {
                                "Timestamp": 1672117200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672120800,
                                "Value": 8
                            },
                            {
                                "Timestamp": 1672124400,
                                "Value": 6
                            },
                            {
                                "Timestamp": 1672128000,
                                "Value": 0
                            }
                        ],
                        "Max": 346,
                        "MetricName": "l7Flow_outBandwidth_hy",
                        "Sum": 376
                    },
                    {
                        "Avg": 179,
                        "Detail": [
                            {
                                "Timestamp": 1671796800,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671800400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671804000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672128000,
                                "Value": 0
                            }
                        ],
                        "Max": 27817,
                        "MetricName": "l7Flow_inFlux_hy",
                        "Sum": 28834
                    },
                    {
                        "Avg": 167,
                        "Detail": [
                            {
                                "Timestamp": 1672084800,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672088400,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672092000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1672128000,
                                "Value": 0
                            }
                        ],
                        "Max": 25812,
                        "MetricName": "l7Flow_outFlux_hy",
                        "Sum": 26973
                    },
                    {
                        "Avg": 0,
                        "Detail": [
                            {
                                "Timestamp": 1671552000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671555600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671559200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1671868800,
                                "Value": 0
                            }
                        ],
                        "Max": 394,
                        "MetricName": "l7Flow_inBandwidth_hy",
                        "Sum": 418
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 3: 查询回源分析类时序数据**

查询最近三十天的回源请求数据

Input: 

```
tccli teo DescribeTimingL7SourceData --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Flow_request_hy
```

Output: 
```
{
    "Response": {
        "RequestId": "141a7ccd-9713-43a2-91d5-1b47692d0609",
        "TimingDataRecords": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "Avg": 803,
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
                        "Max": 7921,
                        "MetricName": "l7Flow_request_hy",
                        "Sum": 24918
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

