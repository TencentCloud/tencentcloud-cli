**Example 1: 查询七层数据分析类时序流量数据**



Input: 

```
tccli teo DescribeTimingL7AnalysisData --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Flow_request
```

Output: 
```
{
    "Response": {
        "RequestId": "141a7ccd-9713-43a2-91d5-1b47692d0609",
        "Data": [
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
                        "MetricName": "l7Flow_request",
                        "Sum": 24918
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

