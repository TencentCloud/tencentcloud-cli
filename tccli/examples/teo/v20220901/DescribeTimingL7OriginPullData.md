**Example 1: 查询回源分析类时序数据**

	
查询指定站点 ID zone-2ntf1u8utpmz 下七层域名业务 2025-07-01 00:00:00 ~ 2025-07-15 00:00:00 时间内的回源请求数，查询时间粒度为“天”。

Input: 

```
tccli teo DescribeTimingL7OriginPullData --cli-unfold-argument  \
    --StartTime 2025-07-01T00:00:00+08:00 \
    --EndTime 2025-07-15T00:00:00+08:00 \
    --Interval day \
    --MetricNames l7Flow_request_hy \
    --ZoneIds zone-2ntf1u8utpmz
```

Output: 
```
{
    "Response": {
        "RequestId": "7cc73e86-092b-4aa2-b28a-c9c338834926",
        "TimingDataRecords": [
            {
                "TypeKey": "251008840",
                "TypeValue": [
                    {
                        "Avg": 1714316,
                        "Detail": [
                            {
                                "Timestamp": 1751299200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1751385600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1751472000,
                                "Value": 1471972
                            },
                            {
                                "Timestamp": 1751558400,
                                "Value": 2824464
                            },
                            {
                                "Timestamp": 1751644800,
                                "Value": 2815290
                            },
                            {
                                "Timestamp": 1751731200,
                                "Value": 2814852
                            },
                            {
                                "Timestamp": 1751817600,
                                "Value": 2815244
                            },
                            {
                                "Timestamp": 1751904000,
                                "Value": 11147558
                            },
                            {
                                "Timestamp": 1751990400,
                                "Value": 6
                            },
                            {
                                "Timestamp": 1752076800,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1752163200,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1752249600,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1752336000,
                                "Value": 0
                            },
                            {
                                "Timestamp": 1752422400,
                                "Value": 111050
                            }
                        ],
                        "Max": 11147558,
                        "MetricName": "l7Flow_request_hy",
                        "Sum": 24000436
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

