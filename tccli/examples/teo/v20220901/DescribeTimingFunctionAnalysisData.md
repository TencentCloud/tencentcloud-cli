**Example 1: 根据函数名称查询边缘函数请求数时序数据**



Input: 

```
tccli teo DescribeTimingFunctionAnalysisData --cli-unfold-argument  \
    --ZoneIds zone-2o7b38ba1hvr \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --MetricNames function_requestCount \
    --Interval day \
    --Area mainland \
    --Filters.0.Key function-name \
    --Filters.0.Operator equals \
    --Filters.0.Value test051301-zone-2o7b38ba1hvr-13000000
```

Output: 
```
{
    "Response": {
        "RequestId": "141a7ccd-9713-43a2-91d5-1b47692d0609",
        "Data": [
            {
                "TypeKey": "13000000",
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
                        "MetricName": "function_requestCount",
                        "Sum": 24918
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

